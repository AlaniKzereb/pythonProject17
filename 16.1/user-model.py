from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)

db.create_all()

user_john = User(id=1, name="John", age=30)
user_alice = User(id=2, name="Alice", age=18)

print(user_john, user_alice)

if __name__ == '__main__':
    app.run(debug=True)
