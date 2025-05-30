from fastapi import APIRouter, HTTPException, status
from models import *
from tasks_dao import TasksDAO

roteador_tasks = APIRouter()

tasks_dao = TasksDAO()

@roteador_tasks.get('/tasks')
def listar_tasks(opcao: str = None, valor: int = None):
    if opcao:
        return tasks_dao.filtrar(opcao, valor)
    tarefas = tasks_dao.todas_tarefas()
    return tarefas

@roteador_tasks.get('/tasks/{task_id}')
def task_por_id(task_id: int):
    tarefa = tasks_dao.obter_por_id(task_id)
    return tarefa

@roteador_tasks.post('/tasks', status_code=status.HTTP_201_CREATED)
def criar_task(novo:createTarefa):
    tarefa = tasks_dao.criartarefa(novo)
    return tarefa

@roteador_tasks.put('/tasks/{task_id}')
def atualizar_task(task_id: int, tarefa:atualizarTarefa):
    tarefa = tasks_dao.atualizartarefa(task_id, tarefa)
    return tarefa

@roteador_tasks.delete('/tasks/{task_id}',status_code=status.HTTP_204_NO_CONTENT)
def deletar_task(task_id):
    if task_por_id(task_id):
        tasks_dao.removertarefa(task_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe uma tarefa com id = {task_id}')