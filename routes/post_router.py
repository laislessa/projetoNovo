from fastapi import APIRouter

router = APIRouter()

@router.get('/posts')
def posts():
    return{"message" : "Listar Post" }