from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def getusers():
    data = [{"name":"rasoa", "email":"rasoa@gmail.com"}]
    return {"status":"success", "msg": "displayed successfully", "data": data}

