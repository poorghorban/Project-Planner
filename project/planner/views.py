from . import app 
from .models import * 
from flask import request , jsonify , redirect , url_for , render_template

# web page 
@app.route('/register', methods=['GET' , 'POST'])
def register():
    if request.method == 'POST':
    
        member_by_cellphone = Member.get_by_cellphone_number(request.form['phone']).first()
        member_by_name= Member.get_by_name(request.form['name']).first()

        if member_by_cellphone is None and  member_by_name is None:

            member = Member(name=request.form['name'] , cellphone_number=request.form['phone'] ,email= request.form['email'],password = request.form['password'])
            flag = member.save()
            
            if flag:
               return render_template('register.html' , message='ثبت نام شما با موفقیت انجام شد.')
            else:
               return render_template('register.html' , message='ثبت نام شما با خطا مواجه شد.')
        else:
            return render_template('register.html' , message='کاربری با این مشخصات وجود دارد.')

    else:
        return render_template('register.html' , message='')


@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        member = Member.get_by_cellphone_number(request.form['phone']).first()

        if member is not None and member.check_password(request.form['password']):
            return redirect(url_for('panel_member', name = member.name))
        else:
            return render_template('login.html' , message = "اطلاعات شما با هم مطابقت ندارد." )
    else:
        return render_template('login.html', message = "")


@app.route('/panel')
def panel_member():
    return render_template('panel_member.html' , name = request.args.get('name'))


# mobile app 
@app.route('/m/register', methods=['POST'])
def m_register():

    data = request.get_json()

    member_by_cellphone = Member.get_by_cellphone_number(data['phone']).first()
    member_by_name= Member.get_by_name(data['name']).first()

    if member_by_cellphone is None and  member_by_name is None:

        member = Member(name=request.form['name'] , cellphone_number=request.form['phone'] ,email= request.form['email'],password = request.form['password'])
        flag = member.save()
            
        if flag:
            return jsonify({"data":{"user_name": member.name, "api_token":"api"} , "status":"success"})
        else:
            return jsonify({"data":'ثبت نام شما با خطا مواجه شد.' , "status":"error"})
    else:
             return jsonify({"data":'کاربری با این مشخصات وجود دارد.' , "status":"error"})



@app.route('/m/login' , methods=['POST'])
def m_login():
    data = request.get_json()
    member = Member.get_by_cellphone_number(data['phone']).first()

    if member is not None and member.check_password(data['password']):
        return jsonify({"data":{"user_id": member.id, "api_token":"api"} , "status":"success"})
    else:
        return jsonify({"data":"اطلاعات شما با هم مطابقت ندارد." , "status":"error"})

