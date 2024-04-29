from app.env import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


DATABASE = "mysql://%s:%s@%s/%s?charset=utf8" % (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME,
)

engine = create_engine(DATABASE, echo=True)

Base = declarative_base()
