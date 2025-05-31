import sqlite3
from models import *

class AuthDAO():
    def __init__(self):
        pass
    
    
    def salvar(self, usuario: SignInUser):
        with sqlite3.connect('GerencTasks.db') as c:
            cursor = c.cursor()
            
            sql = '''insert into usuarios(username, email, password_hash)
            values(?,?,?)'''
            
            cursor.execute(sql, (usuario.username, usuario.email, usuario.password_hash))
            
            id = cursor.lastrowid
            return Usuario(id=id, **usuario.dict())
    
    def buscar_usuario_por_email(self, email: str):
        with sqlite3.connect('GerencTasks.db') as c:
            cursor = c.cursor()
            
            sql = '''select * from usuarios where email = ?'''
            cursor.execute(sql,(email,))
            result = cursor.fetchone()
            if not result:
                return None
            
            usuario = Usuario(
                id = result[0], username=result[1],email=result[2],password_hash = result[3]
            )
            return usuario