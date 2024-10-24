from config import dp, bot
import asyncio
from main import default_router, set_commands, create_models

async def main():
    create_models()
    dp.include_router(default_router)
    await set_commands()
    await dp.start_polling(bot)

try:
    if __name__ == '__main__':
        asyncio.run(main())
except KeyboardInterrupt as e:
    print(str(e))

