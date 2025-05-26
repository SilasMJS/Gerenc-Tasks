from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    username: str
    email: str
    password: str

class Task(BaseModel):
    id: int
    titulo: str
    descricao: str
    concluida: False
    usuario_id : int

class createUsuario(Usuario):
    pass

class createTask(Task):
    pass
