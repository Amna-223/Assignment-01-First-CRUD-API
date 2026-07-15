from fastapi import FastAPI, HTTPException
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