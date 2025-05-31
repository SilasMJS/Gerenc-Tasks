from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tasks_routes import roteador_tasks
from auth_routes import router

app = FastAPI()

origins = ["http://127.0.0.1:5500"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Rotas de Veículos
app.include_router(roteador_tasks)

# Rotas de Autenticaco
app.include_router(router)