from fastapi import APIRouter, HTTPException, status, Depends
from models import *
from tasks_dao import TasksDAO
from typing import Annotated
from auth_utils import get_current_user


roteador_tasks = APIRouter()

tasks_dao = TasksDAO()

@roteador_tasks.get('/tasks')
def listar_tasks(user: Annotated[Usuario, Depends(get_current_user)], opcao: str = None, valor: int = None):
    if opcao:
        return tasks_dao.filtrar(opcao, valor)
    tarefas = tasks_dao.todas_tarefas(user)
    return tarefas

@roteador_tasks.get('/tasks/{task_id}')
def task_por_id(task_id: int, user: Annotated[Usuario, Depends(get_current_user)]):
    tarefa = tasks_dao.obter_por_id(task_id)
    return tarefa

@roteador_tasks.post('/tasks', status_code=status.HTTP_201_CREATED)
def criar_task(novo:createTarefa, user: Annotated[Usuario, Depends(get_current_user)]):
    tarefa = tasks_dao.criartarefa(novo, user)
    return tarefa

@roteador_tasks.put('/tasks/{task_id}')
def atualizar_task(task_id: int, tarefa:atualizarTarefa, user: Annotated[Usuario, Depends(get_current_user)]):
    tarefa = tasks_dao.atualizartarefa(task_id, tarefa)
    return tarefa

@roteador_tasks.delete('/tasks/{task_id}',status_code=status.HTTP_204_NO_CONTENT)
def deletar_task(task_id: int, user: Annotated[Usuario, Depends(get_current_user)]):
    if task_por_id(task_id):
        tasks_dao.removertarefa(task_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe uma tarefa com id = {task_id}')