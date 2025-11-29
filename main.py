from fastapi import FastAPI
app = FastAPI()
data = [{"id":1, "name":"rasoa", "email":"rasa@gmail.com"}]
@app.get("/")
def getusers():
    return {"status":"success", "msg": "displayed successfully", "data": data}
