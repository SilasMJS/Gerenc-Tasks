from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from models import *
from auth_dao import AuthDAO
from auth_utils import *

router = APIRouter()

auth_dao = AuthDAO()

@router.post('/auth/signin')
def login(data: SignInUser):
    usuario_existente = auth_dao.buscar_usuario_por_email(data.email)
    
    if not usuario_existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Email e/ou senha incorreto(s)!")
    
    if not verify_hash_password(data.password_hash, usuario_existente.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Email e/ou senha incorreto(s)!')
    
    access_token = create_jwt_token(usuario_existente.email)
    
    return{
        'username':usuario_existente.username,
        'access_token':access_token
    }

@router.post('/auth/signup')
def signup(data:SignupUser):
    usuario_existente = auth_dao.buscar_usuario_por_email(data.email)
    
    if not is_valid_password(data.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'A senha não atende aos critérios.')
        
    if usuario_existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Já existe um usuário com email {data.email}')
    data.password_hash = hash_password(data.password_hash)
    usuario = auth_dao.salvar(data)
    return usuario

@router.post('/auth/forget-password')
def forget_password():
    pass


@router.get('/auth/me')
def me(user: Annotated[Usuario, Depends(get_current_user)]):
    return {
        'username':user.username,
        'email':user.email
    }