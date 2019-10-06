from sqlalchemy import Column , Integer , String , LargeBinary , Text
from . import Base , session
from werkzeug.security import check_password_hash , generate_password_hash
from hashlib import md5
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


class Admin(Base):
    __tablename__ = 'tbl_admin'

    id = Column(Integer , primary_key=True)
    name = Column(String(255))
    image = Column(LargeBinary)
    cellphone_number = Column(String(11))
    email = Column(String(255))
    password_hash = Column(String(255))

    def __init__(self , name , cellphone_number , image , email , password):
        self.name = name
        self.cellphone_number = cellphone_number
        self.image = image
        self.email = email
        self.set_password(password)

    def set_password(self , password):
        self.password_hash = generate_password_hash(password)

    def save(self):
        flag = True
        try:
            session.add(self)
            session.commit()
        except:
            session.rollback()
            flag = False

        return flag
    
    def check_password(self , password):
        return check_password_hash(self.password_hash , password)



class Class(Base):
    __tablename__ = 'tbl_class'

    id = Column(Integer , primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    admin_id = Column(Integer, ForeignKey('tbl_admin.id'))

    def __init__(self , title , description, admin_id):
        self.title = title 
        self.description = description
        self.admin_id = admin_id

    def save(self):
        flag = True
        try:
            session.add(self)
            session.commit()
        except:
            session.rollback()
            flag = False
        return flag

class Member(Base):
    __tablename__ = 'tbl_member'

    id = Column(Integer , primary_key=True)
    name = Column(String(255))
    cellphone_number = Column(String(11))
    image = Column(LargeBinary)
    email = Column(String(255))
    password_hash = Column(String(255))

    def __init__(self , name , cellphone_number , image , email , password):
        self.name = name
        self.cellphone_number = cellphone_number
        self.image = image
        self.email = email
        self.set_password(password)

    def set_password(self , password):
        self.password_hash = generate_password_hash(password)

    def save(self):
        flag = True
        try:
            session.add(self)
            session.commit()
        except:
            session.rollback()
            flag = False
        return flag

    @staticmethod
    def get_by_cellphone_number(phone)
        pass
    
    def check_password(self , password):
        return check_password_hash(self.password_hash , password)



class Items(Base):
    __tablename__ = 'tbl_items'

    id = Column(Integer , primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    class_id =  Column(Integer, ForeignKey('tbl_class.id'))

    def __init__(self , title , description , class_id):
        self.title = title 
        self.description = description
        self.class_id = class_id

    def save(self):
        flag = True
        try:
            session.add(self)
            session.commit()
        except:
            session.rollback()
            flag = False
        return flag


class Class_Member(Base):
    __tablename__ = 'tbl_class_member'

    id = Column(Integer , primary_key=True)
    member_id = Column(Integer, ForeignKey('tbl_member.id'))
    class_id = Column(Integer, ForeignKey('tbl_class.id'))

    def __init__(self , member_id , class_id):
        self.member_id = member_id
        self.class_id = class_id

    def save(self):
        flag = True
        try:
            session.add(self)
            session.commit()
        except:
            session.rollback()
            flag = False
        return flag


class Member_Item(Base):
    __tablename__ = 'tbl_member_item'

    id = Column(Integer , primary_key=True)
    description_admin = Column(Text)
    description_member = Column(Text)
    member_id = Column(Integer, ForeignKey('tbl_member.id'))
    item_id = Column(Integer, ForeignKey('tbl_items.id'))
    date = Column(String(255))

    
    def __init__(self , description_admin , date , member_id , item_id):
        self.description_admin = description_admin
        self.member_id = member_id 
        self.item_id = item_id
        self.date = date
        self.description_member = ' '

    def save(self):
        flag = True
        try:
            session.add(self)
            session.commit()
        except:
            session.rollback()
            flag = False
        return flag
