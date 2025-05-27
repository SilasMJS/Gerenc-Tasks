import sqlite3

from models import Usuario, Task, createTask

class TasksDAO():
  
  def __init__(self):
    pass

  def criar_task(self, Task: createTask):
    with sqlite3.connect('Tarefa.bd') as c:
      cursor = c.cursor()

      sql = '''INSERT INTO Tarefa(titulo, descricao, usuario_id)
            VALUES ( ?, ?, ?)'''
      
      cursor.execute(sql, (Task.titulo, 
                          Task.descricao, 
                          Task.usuario_id))
      
      id = cursor.lastrowid
      concluida = 0
      return Task(id=id, concluida = concluida, **Task.dict())