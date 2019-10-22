from . import app , db , ALLOWED_EXTENSIONS
from flask import render_template , request ,redirect , url_for, jsonify , session
from .models import *
from werkzeug.utils import secure_filename
import os
import re


# handle session db
def shutdown_session(exception=None):
    db.remove()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def validation_on_submit_register(name , phone , email , image , password):
    errors = []

    # check validation name 
    if name == '':
        errors.append('فیلد نام خالی است.')
    
    # check validation phone
    if phone == '':
        errors.append('فیلد شماره تماس خالی است.')
    else:
        if len(phone) < 11 or len(phone) > 11:
            errors.append('فیلد شماره تماس را به صورت 09xx xxx xx xx وارد نمایید.')


    # check validation email
    if email != '':
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not (re.search(regex , email)):
            errors.append('ایمیل به فرمت example@example.com وارد نمایید.')

    # check validation image 
    if image.filename == '':
        errors.append('فیلد عکس خالی است.')
    else:
        if not allowed_file(image.filename):
            errors.append('عکس ورودی به فرمت های jpeg،jpg،png وارد نمایید.')

    # check validation password 
    if password == '':
        errors.append('فیلد رمزعبور خالی است.')
    else:
        if len(password) < 10 :
            errors.append('رمزعبور ضعیف است.')

    return errors
    

# web pages
@app.route('/')
def index():
    #check session 
    if 'user' in session:
        return redirect(url_for('member_panel'))
    else:
        return render_template('index.html')
        
@app.route('/register' , methods=['GET' , 'POST'])
def register():
    if request.method == 'POST':
        # get data from form 
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        image = request.files['image']
        password = request.form['password']

        # validation data 
        list_errors_valid_data = validation_on_submit_register(name ,phone , email , image , password)
        if len(list_errors_valid_data):
            return render_template('register.html' , status='failed' , errors=list_errors_valid_data)
        else:
            # check exsist user 
            if Member.get_by_phone(phone) is None and Member.get_by_name(name) is None:
                
                # save user on database
                member = Member(name= name , phone = phone , email = email , password = password)
                flag = member.save()
                
                if flag:
                    
                    # save image profile on upload folder
                    image_name = secure_filename(image.filename)
                    new_image_name = phone + '.' + image_name.split('.')[1]
                    image.save(os.path.join(app.config['UPLOAD_FOLDER'] , new_image_name))

                    return redirect(url_for('index'))

                else:
                    return render_template('register.html' ,status='failed', errors = ['ثبت نام شما با خطا مواجه شد.لطفا دوباره تکرار نمایید.'])

            else:
                return render_template('register.html' ,status='failed', errors = ['کاربری با این مشخصات وجود دارد.'])
        
    else:
        return render_template('register.html')

@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        # get data from form 
        phone = request.form['phone']
        password = request.form['password']

        errors = []

        # check valid data 
        if phone == '':
            errors.append('فیلد شماره تماس خالی است.')
        if password == '':
            errors.append('فیلد رمزعبور خالی است.')

        if len(errors):
            return render_template('login.html' ,status='failed', errors = errors)
        else:
            # check exsist user 
            member = Member.get_by_phone(phone)

            if member is not None and member.check_password(password):
                session.permanent = True
                session['user'] = member.name
                return redirect(url_for('member_panel'))   
            else:
                return  render_template('login.html' , status='failed' , errors = ['شماره تماس یا رمزعبور نادرست است.'])
            
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user' , None)
        return redirect(url_for('index'))

@app.route('/member/panel')
def member_panel():
    #check session 
    if 'user' in session:
        return render_template('member_panel.html')
    else:
        return redirect(url_for('login'))



# mobile app
@app.route('/m/register')
def m_register():
    #get json file 
    data = request.get_json()

    name = data['name']
    phone = data['phone']
    email = data['email']
    image = data['image']
    password = data['password']

    # check exsist user 
    if Member.get_by_phone(phone) is None and Member.get_by_name(name) is None:
                
        # save user on database
        member = Member(name= name , phone = phone , email = email , password = password)
        flag = member.save()
                
        if flag:
                    
            # save image profile on upload folder
            image_name = secure_filename(image.filename)
            new_image_name = phone + '.' + image_name.split('.')[1]
            image.save(os.path.join(app.config['UPLOAD_FOLDER'] , new_image_name))

            return jsonify({'status': "success" , 'user_name':member.name})
        else:
            return jsonify({'status':"failed" , 'error':"ثبت نام شما با خطا مواجه شد.لطفا دوباره تکرار نمایید."})

    else:
        return jsonify({'status':"failed", 'error':"کاربری با این مشخصات وجود دارد."})


@app.route('/m/login')
def m_login():
    # get json file 
    data = request.get_json()

    # check exsist user 
    member = Member.get_by_phone(data['phone'])

    if member is not None and member.check_password(data['password']):
        return jsonify({'user_id':member.id , 'status':"success"})
    else:
        return jsonify({'status':'failed' , 'error':'شماره تماس یا رمزعبور نادرست است.'})
