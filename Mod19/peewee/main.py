from peewee import SqliteDatabase, Model, CharField, IntegerField
db = SqliteDatabase('../database.db')

class User(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db

db.connect()
db.drop_tables([User], safe=True)
db.create_tables([User], safe=True)

user1 = User(name='Dmitry', age=25)
user1.save()
user2 = User(name='Sonya', age=21)
user2.save()

user1.name = 'Dimok'
user1.save()


users = User.select()
for user in users:
    print(user.name, user.age)

user1.delete_instance()
user1.save()

users = User.select()
for user in users:
    print(user.name, user.age)