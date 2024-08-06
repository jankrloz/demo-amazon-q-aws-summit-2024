from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = "myuser"
DB_PASSWORD = "mypassword"
DB_HOST = "db"
DB_PORT = "3306"
DB_NAME = "mydatabase"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"charset": "utf8"},
)

Base = declarative_base()

Session = sessionmaker(bind=engine)
