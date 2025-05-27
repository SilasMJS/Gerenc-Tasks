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
  
  def atualizar_task(self, id: int, Task: Task):
    with sqlite3.connect('Tarefa.bd') as c:
      cursor = c.cursor()

      sql = '''UPDATE Veiculos SET titulo = ?,
      descricao = ?,
      concluida = ?
      WHERE id = ?'''

      cursor.execute(sql, (Task.titulo, Task.descricao, Task.concluida, id))
      c.commit()
      if cursor.rowcount > 0:
        return self.obter_por_id(id)
      return None
    
  def obter_por_id(self, id: int):
    pass