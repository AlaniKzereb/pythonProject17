from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

# from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))

    group = relationship("Group")


class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    users = relationship("User")


db.create_all()

group_1 = Group(id=1, name="Group #1")
user_1 = User(id=1, name="John", age=35, group=group_1)

with db.session.begin():
    db.session.add(user_1)


user_1 = User(id=1, name="Alice", age=35, group=group_1)
group_1 = Group(id=1, name="Group #1")

print(user_john, user_alice)

if __name__ == '__main__':
    app.run(debug=True)
