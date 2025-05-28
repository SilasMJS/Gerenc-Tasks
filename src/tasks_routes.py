from fastapi import APIRouter, HTTPException, status
from models import createUsuario, createTarefa
from tasks_dao import TasksDAO

roteador_tasks = APIRouter()

tasks_dao = TasksDAO()

@roteador_tasks.get('/tasks')
def listar_tasks():
    tarefas = tasks_dao.todas_tarefas()
    return tarefas

@roteador_tasks.get('/tasks/{task_id}')
def task_por_id(task_id: int):
    tarefa = tasks_dao.obter_por_id(task_id)
    return tarefa

@roteador_tasks.post('/tasks')
def criar_task(novo:createTarefa):
    tarefa = tasks_dao.criartarefa(novo)
    return tarefa

@roteador_tasks.put('/tasks/{task_id}')
def atualizar_task(task_id):
    pass

@roteador_tasks.delete('/tasks/{task_id}')
def deletar_task(task_id):
    pass