from fastapi import FastAPI
from app.model import init_db
from app.controller.tarefa_controller import router

app = FastAPI(title="Micro-API de Tarefas")
app.include_router(router)

init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
