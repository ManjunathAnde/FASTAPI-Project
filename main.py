from fastapi import FastAPI
app = FastAPI() #creating an instance of FASTAPI

@app.get("/") 
def greet():
    return "Welcome to MJ APP"

@app.get("/skills")
def skills():
    return {"skills": ["Python", "FastAPI", "AWS"]}
