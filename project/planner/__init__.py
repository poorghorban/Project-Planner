from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session , sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import timedelta

# create app and config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'

# config database
engine = create_engine('mysql+mysqlconnector://root:software1393@localhost/db_planner?charset=utf8' , encoding="utf8")
db = scoped_session(sessionmaker(autocommit=False , autoflush=False , bind=engine))

Base = declarative_base()
Base.query = db.query_property()

'''
def init_db():
    from .models import *
   Base.metadata.create_all(bind=engine)
'''

# config upload image 
UPLOAD_FOLDER = "planner//static//upload_image"
ALLOWED_EXTENSIONS = set(['png' , 'jpg' , 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# config session
app.permanent_session_lifetime = timedelta(minutes=5)

from .views import *