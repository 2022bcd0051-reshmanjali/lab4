from fastapi import FastAPI

app = FastAPI()

@app.get("/predict")
def predict():
    return {
        "name": "Reshmanjali Maddula",
        "roll_no": "2022BCD051",
        "wine_quality": 5
    }