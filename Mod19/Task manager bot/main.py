from datetime import datetime

import peewee
from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from peewee import IntegrityError
from config import bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from db_config import *
from aiogram.types import BotCommand, BotCommandScopeDefault
from typing import List

default_router = Router()

class UserState(StatesGroup):
    new_task_title = State()
    new_task_due_date = State()
    tasks_make_done = State()


def cancel_kb():
    inline_kb_cancel = [
        [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_cancel)


async def set_commands():
    commands = [BotCommand(command='newtask', description='Создать задачу'),
                BotCommand(command='tasks', description='Последние 10 задач'),
                BotCommand(command='today', description='Задачи на сегодня')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


@default_router.callback_query(F.data == 'cancel')
async def cancel_router(call: CallbackQuery, state: FSMContext):
    await state. clear()
    await bot.send_message(call.from_user.id, 'Действие отменено')


@default_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    name = message.from_user.first_name
    last_name = message.from_user.last_name

    try:
        User.create(
            user_id=user_id,
            username=username,
            name=name,
            last_name=last_name,
        )
        await message.answer("Добро пожаловать в менеджер задач!")
    except IntegrityError:
        await message.answer(f"Рад вас снова видеть, {name}!")

@default_router.message(Command(commands=['newtask']))
async def cmd_newtask(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if User.get_or_none(User.user_id == user_id) is None:
        await message.reply('Вы не зарегистрированы, нажмите /start')
        return

    await bot.send_message(user_id, 'Введите название задачи', reply_markup=cancel_kb())
    await state.set_state(UserState.new_task_title)
    await state.update_data(new_task={'user_id': user_id})

@default_router.message(F.text, UserState.new_task_title)
async def process_task_title(message: Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    data['new_task']['title'] = message.text
    await bot.send_message(message.from_user.id, 'Введите дату (ДД.ММ.ГГГГ): ', reply_markup=cancel_kb())
    await state.set_state(UserState.new_task_due_date)

@default_router.message(UserState.new_task_due_date)
async def process_task_due_date(message: Message, state: FSMContext):
    due_date_string = message.text
    try:
        due_date = datetime.strptime(due_date_string, DATE_FORMAT)
    except ValueError:
        await bot.send_message(message.from_user.id, 'Введите дату (ДД.ММ.ГГГГ):', reply_markup=cancel_kb())
        return
    data = await state.get_data()
    print(data)
    data['new_task']['due_date'] = due_date

    new_task = Task(**data['new_task'])
    new_task.save()
    await bot.send_message(message.from_user.id, f'Задача добавлена\n{new_task}')
    await state.clear()

@default_router.message(Command(commands=['tasks']))
async def my_tasks(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)
    if user is None:
        await bot.send_message(message.from_user.id, 'Вы не зарегистрированы. Напишите /start')
        return

    tasks: List[Task] = user.tasks.order_by(-Task.due_date, -Task.task_id).limit(10)
    result = []
    result.extend(map(str, reversed(tasks)))
    if not result:
        await bot.send_message(message.from_user.id, 'У вас ещё нет задач, чтобы добавить задачу'
                                                     'введите /newtask')
        return

    result.append('\nВведите номер задачи, чтобы изменить её статус')
    await bot.send_message(message.from_user.id, '\n'.join(result))
    await state.set_state(UserState.tasks_make_done)

@default_router.message(F.text)
async def change_task_status(message: Message, state: FSMContext):
    task_id = int(message.text)
    task = Task.get_or_none(Task.task_id == task_id)
    if task is None:
        await bot.send_message(message.from_user.id, 'Задачи с таким номером нет')
        return

    if task.user_id != message.from_user.id:
        await bot.send_message(message.from_user.id, 'Вы не являетесь автором этой задачи')
        return

    task.is_done = not task.is_done
    task.save()

    await bot.send_message(message.from_user.id, str(task))

@default_router.message(Command(commands=['today']))
async def today_tasks(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = Task.get_or_none(User.user_id == user_id)

    if user is None:
        await bot.send_message(message.from_user.id, 'Вы не зарегистрированы, введите /start')
        return

    tasks: List[Task] = user.tasks.where(Task.due_date == datetime.today())

    result = []
    result.extend(map(str, tasks))

    if not result:
        await bot.send_message(message.from_user.id, 'У вас ещё нет задач, '
                                                     'чтобы добавить задачу введите /newtask')
        return

    result.append('\nВведите номер задачи, чтобы изменить её статус')
    await bot.send_message(message.from_user.id, '\n'.join(result))
    await state.set_state(UserState.tasks_make_done)

