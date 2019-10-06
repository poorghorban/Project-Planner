from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



app = Flask(__name__)
engine = create_engine('mysql+mysqlconnector://root:software1393@localhost/db_plan' , encoding="utf8")
Base = declarative_base()
Session = sessionmaker(bind=engine)


from .views import * 
