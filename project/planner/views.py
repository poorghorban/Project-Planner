from . import app 
from .models import * 
from flask import request , jsonify


# web page 
@app.route('/register', methods=['GET' , 'POST'])
def register():
    if request.method == 'POST':
        pass
    else:
        pass



@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        pass



# mobile app 
@app.route('/m/register', methods=['POST'])
def m_register():
    pass 

@app.route('/m/login' , methods=['POST'])
def m_login():
    pass