from fastapi import FastAPI
app = FastAPI(title="reunite API")

@app.get("/")
def root():
    return {"message": "Hello World"}