from fastapi import FastAPI
from scripts.services.ut_service import Student_rout
import uvicorn


app=FastAPI()

app.include_router(Student_rout)

if __name__ == "__main__":
    uvicorn.run(app='main:app' , port=1800)


