from fastapi import FastAPI
from prediction import predict_price

app = FastAPI()

@app.get("/api/predict")
def predict(size,total_sqft,bath,balcony,location):
    price = list(predict_price(size,total_sqft,bath,balcony,location))[0]
    return {"message":"Success","Data":{"predicted_price":price},"ErrorCode":0}
   