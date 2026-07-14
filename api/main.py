from fastapi import FastAPI
from api.routes.moradores import router as moradores_router

app = FastAPI(
    title="FaceHomeAI API",
    version="1.0.0",
    description="API oficial da plataforma FaceHomeAI."
)

@app.get("/")
def inicio():

    return {
        "empresa": "LGA Automation",
        "produto": "FaceHomeAI",
        "versao": "1.0.0",
        "status": "Online"
    }
app.include_router(moradores_router)