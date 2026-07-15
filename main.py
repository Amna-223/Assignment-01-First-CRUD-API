from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

class Task(BaseModel):
    title:str

app = FastAPI()

chores = [
    {
        "id" : 1,
        "title" : "Laundery", 
        "done" : False  
    }, 
    {
        "id" : 2,
        "title" : "Cooking", 
        "done" : True  
    }, 
    {
        "id" : 3,
        "title" : "Study", 
        "done" : True  
    }
]
taskLength = len(chores)

@app.get("/")
async def root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/health")
async def health():
    return { "status": "ok" }

@app.get("/tasks")
async def get_all_tasks():
    return chores

@app.get("/tasks/{id}")
async def get_task_by_id(id: int):
    for chore in chores:
        if chore["id"] == id:
            return chore
        
    raise HTTPException(status_code=404, detail="Task not Found")

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def add_task(task: Task):
    if not task.title:
        raise HTTPException(status_code=400, detail="Bad Request")
    else:
        global taskLength
        taskLength = taskLength + 1
        newTask = {
                "id" : taskLength,
                "title" : task.title,
                "done" : False
            }
        chores.append(newTask)
        return newTask