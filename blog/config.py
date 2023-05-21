import os


class Config:
    # SQLACHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = "mysql://flask:flask@127.0.0.1:3306/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
