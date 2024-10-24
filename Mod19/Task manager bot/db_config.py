from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField, DateField, \
    BooleanField, AutoField


db = SqliteDatabase('bot_database.db')

DATE_FORMAT = '%d.%m.%Y'


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    username = CharField()
    name = CharField()
    last_name = CharField(null=True)

class Task(BaseModel):
    task_id = AutoField()
    user = ForeignKeyField(User, backref='tasks')
    title = CharField()
    due_date = DateField()
    is_done = BooleanField(default=False)

    def __str__(self):
        return (f'{self.task_id}. {"[V]" if self.is_done else "[ ]"} '
                f' {self.title}. {self.due_date.strftime(DATE_FORMAT)}')

def create_models():
    db.create_tables(BaseModel.__subclasses__())
