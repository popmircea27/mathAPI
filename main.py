from fastapi import FastAPI
from controller import math_controller

app = FastAPI(title="Tema Python")
app.include_router(math_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
