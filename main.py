from fastapi import FastAPI
app = FastAPI()
@app.get("/")
data = {"id":1, "name":"rasoa", "email":"rasa@gmail.com"}
def getusers():
    return {"status":"success", "msg": "displayed successfully", "data": data}
