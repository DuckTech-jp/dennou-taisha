from fastapi import FastAPI

app = FastAPI()

@app.get("/oracle")
def oracle():
    return {"message": "ガッ!今日の運勢はnull也!"}