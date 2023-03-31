from fastapi import APIRouter

router = APIRouter()

@router.get('/usuarios')
def usuarios():
    return{"message" : "Lista de Usuarios" }