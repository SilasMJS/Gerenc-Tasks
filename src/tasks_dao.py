import sqlite3

from models import Tarefa, createTarefa

class TasksDAO():
  
  def __init__(self):
    pass
  
  def todas_tarefas(self):
    with sqlite3.connect('GerencTasks.db') as c:
      cursor = c.cursor()
      
      sql = '''SELECT * from tarefas'''
      
      cursor.execute(sql)
      tarefas_list = cursor.fetchall()
      
      tarefas: list[Tarefa] = []
      
      for t in tarefas_list:
        tarefa = Tarefa(id = t[0],
        titulo = t[1],
        descricao = t[2],
        concluida = t[3],
        usuario_id = t[4])
      
        tarefas.append(tarefa)
      return tarefas
  
  def filtrar(self, opcao, valor):
    with sqlite3.connect('GerencTasks.db') as c:
      cursor = c.cursor()
      
      sql = f"select * from tarefas where {opcao} = ?"
      
      cursor.execute(sql, (valor,))
      tarefas_list = cursor.fetchall()
      
      tarefas: list[Tarefa] = []
      
      if not tarefas_list:
        return None
      
      for t in tarefas_list:
        tarefa = Tarefa(id = t[0],
        titulo = t[1],
        descricao = t[2],
        concluida = t[3],
        usuario_id = t[4])
      
        tarefas.append(tarefa)
      return tarefas

  def obter_por_id(self, id: int):
    with sqlite3.connect('GerencTasks.db') as c:
      cursor = c.cursor()
      
      sql = 'select * from tarefas where id = ?'
      cursor.execute(sql, (id,))
      result = cursor.fetchone()
      
      if not result:
        return None
      
      tarefa = Tarefa(
        id = result[0],
        titulo = result[1],
        descricao = result[2],
        concluida = result[3],
        usuario_id = result[4]
      )
      
      return tarefa
  
  def criartarefa(self,tarefa:createTarefa):
    with sqlite3.connect('GerencTasks.db') as c:
      cursor = c.cursor()

      sql = '''INSERT INTO tarefas(titulo, descricao)
            VALUES ( ?, ?)'''
      
      cursor.execute(sql, (tarefa.titulo, 
                          tarefa.descricao))
      
      id = cursor.lastrowid
      concluida = 0
      usuario_id = 1
      return Tarefa(id=id, concluida = concluida, usuario_id = usuario_id, **tarefa.dict())
  
  
  def atualizartarefa(self, id: int, Task:Tarefa):
    with sqlite3.connect('GerencTasks.db') as c:
      cursor = c.cursor()

      sql = '''UPDATE tarefas SET titulo = ?,
      concluida = ?
      WHERE id = ?'''

      cursor.execute(sql, (Task.titulo, Task.concluida, id))
      c.commit()
      if cursor.rowcount > 0:
        return self.obter_por_id(id)
      return None
  
  def removertarefa(self, id: int):
    with sqlite3.connect('GerencTasks.db') as c:
      cursor = c.cursor()
      
      sql = '''delete from tarefas where id=?'''
      
      cursor.execute(sql,(id,))
      result = cursor.fetchone()
      
      if not result:
        return 