from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
      return {"status": "Social Media Manager is running"}
  
