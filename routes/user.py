from distutils.log import debug
from tkinter.tix import COLUMN
from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

from fastapi.encoders import jsonable_encoder


user = APIRouter()


#-------------------------------Read-------------------------------------------------
@user.get('/read')
def read_info():

     return conn.execute(users.select()).fetchall()


@user.get('/read/{id}')
def read_info(id:int):
     return conn.execute(users.select().where(users.c.id==id)).fetchall()

 

@user.post('/readbyany')
def read_info(info:dict):
    def send_format(a):
        try:
            b = int(a)
            return a
        except:
            return "'"+a+"'" 
    t= conn.execute("select * from users where  %s=%s " %(list(info["set"].keys())[0], send_format(list(info["set"].values())[0]))) .fetchall()
    return t



#---------------------------------------Insert data------------------------------------------
@user.post('/Inserdata')
def write_data(info:dict):
    
    conn.execute(users.insert().values(info))

    return conn.execute(users.select()).fetchall()


#---------------------------------------Update--------------------------------------------------
@user.put('/update/{id}')
def Update(id:int,user:dict):
    conn.execute(users.update().values(user).where(users.c.id==id))
    
    return conn.execute(users.select()).fetchall()

@user.put('/update')
def Update(info:dict):
    def send_format(a):
        try:
            b = int(a)
            return a
        except:
            return "'"+a+"'"

    conn.execute("UPDATE users SET %s=%s WHERE %s==%s " %(list(info["set"].keys())[0], send_format(list(info["set"].values())[0]), list(info["cond"].keys())[0],send_format(list(info["cond"].values())[0])))
    return "Update successfully"  

#-------------------------------------------------Delete--------------------------------------
@user.delete('/delete')
def delete(info:dict):
    def send_format(a):
        try:
            b = int(a)
            return a
        except:
            return "'"+a+"'"
    conn.execute("delete from users where  %s=%s " %(list(info["set"].keys())[0], send_format(list(info["set"].values())[0])))
    return "--- Data Deleted--- "  


