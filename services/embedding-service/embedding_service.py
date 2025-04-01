from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"status": "embedding-service ready"}