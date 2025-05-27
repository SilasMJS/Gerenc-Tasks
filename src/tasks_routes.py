from fastapi import APIRouter, HTTPException, status
from models import Usuario
from tasks_dao import TasksDAO

roteador_tasks = APIRouter()

tasks_dao = TasksDAO()

@roteador_tasks.get('/tasks')
def lista_tasks():
    pass

@roteador_tasks.get('/tasks/{task_id}')
def task_por_id(task_id):
    pass

@roteador_tasks.post('/tasks')
def criar_task():
    pass

@roteador_tasks.put('/tasks/task_id')
def atualizar_task(task_id):
    pass

@roteador_tasks.delete('/tasks/{task_id}')
def deletar_task(task_id):
    pass