from fastapi import APIRouter, HTTPException, status
from models import Usuario
from tasks_dao import TasksDAO
roteador_tasks = APIRouter()

tasks_dao = TasksDAO()