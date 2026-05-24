from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"hello", "world"}

# uvicorn main:app --reload