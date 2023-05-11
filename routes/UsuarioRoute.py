from fastapi import APIRouter, Body


router = APIRouter()


@router.post("/" , response_description="Rota para criar novo usuario.")
async def rota_criar_usuario(usuario = Body(...)):
    return {
        "message": "Usuario criado com sucesso."
    }
