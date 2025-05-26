from fastapi import FastAPI
from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    username: str
    email: str
    password: str

class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str
    concluida: False
    usuario_id : int