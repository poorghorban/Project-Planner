from sqlalchemy import Column , Integer , String , Text
from werkzeug.security import check_password_hash , generate_password_hash
from hashlib import md5
from . import Base , db


class Member(Base):
    __tablename__ = 'tbl_member'

    id = Column(Integer , primary_key=True)
    name = Column(String(255) , unique=True , nullable=False)
    phone = Column(String(11), unique=True , nullable=False)
    email = Column(String(255))
    password_hash = Column(String(255),nullable=False)

    def __init__(self , name , phone , email , password):
        self.name = name 
        self.phone = phone 
        self.email = email
        self.set_password(password)

    def set_password(self , password):
        self.password_hash = generate_password_hash(password)

    def check_password(self , password):
        return check_password_hash(self.password_hash , password)

    @staticmethod
    def get_by_phone(phone):
        return Member.query.filter(Member.phone == phone).first()
    
    @staticmethod
    def get_by_name(name):
        return Member.query.filter(Member.name == name).first()
    
    def save(self):
        flag = True
        try:
            db.add(self)
            db.commit()
        except:
            db.rollback()
            flag = False
        return flag

'''
class Admin(Base):
    __tablename__ = 'tbl_admin'

    id = Column(Integer , primary_key=True)
    name = Column(String(255) , unique=True , nullable=False)
    phone = Column(String(11), unique=True , nullable=False)
    email = Column(String(255))
    password_hash = Column(String(255),nullable=False)

    def __init__(self , name , phone , email , password):
        self.name = name 
        self.phone = phone 
        self.email = email
        self.set_password(password)

class Class(Base):
    __tablename__ = 'tbl_class'

    id = Column(Integer , primary_key=True)
    title = Column(String(255),unique=True , nullable=False)
    description = Column(Text , unique=True , nullable=False)
    admin_id = Column(Integer , ForeignKey('tbl_admin.id'))

    def __init__(self , title , description , admin_id):
        self.title = title
        self.description = description
        self.admin_id = admin_id

class Items(Base):
    __tablename__ = 'tbl_items'

    id = Column(Integer , primary_key=True)
    title = Column(String(255),unique=True , nullable=False)
    description = Column(Text)
    class_id = Column(Integer , ForeignKey('tbl_class.id'))

    def __init__(self , title , description , class_id):
        self.title = title
        self.description = description
        self.class_id = class_id

class Class_Member(Base):
    __tablename__ = 'tbl_class_member'

    id = Column(Integer , primary_key=True)
    member_id = Column(Integer , ForeignKey('tbl_member.id'))
    class_id = Column(Integer , ForeignKey('tbl_class.id'))

    def __init__(self , member_id , class_id):
        self.member_id = member_id
        self.class_id = class_id


class Member_Item(Base):
    __tablename__ = 'tbl_member_item'

    id = Column(Integer , primary_key=True)
    description_admin = Column(Text , nullable=False)
    description_member = Column(Text)
    member_id = Column(Integer , ForeignKey('tbl_member.id'))
    item_id = Column(Integer , ForeignKey('tbl_items.id'))
    date = Column(String(255))

    def __init__(self , description_admin , date , member_id , item_id):
        self.description_admin = description_admin
        self.member_id = member_id
        self.item_id = item_id
        self.date = date

'''