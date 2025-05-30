from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    id: int
    username: str
    email: str
    password_hash: str

class Usuario(UsuarioBase):
    id: int | None = None

class TarefaBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None

    
class Tarefa(TarefaBase):
    id: int | None = None
    concluida: int | bool = 0
    usuario_id : int = 1

class atualizarTarefa(BaseModel):
    titulo: str
    concluida: int = 0

class createUsuario(UsuarioBase):
    pass

class createTarefa(TarefaBase):
    pass
