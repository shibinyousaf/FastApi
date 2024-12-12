from fastapi import FastAPI
from prediction import predict_price,get_city_map
from pydantic_data import Users,AccountCreate
from router import api_router
from product_management.manage_product import product_router


app = FastAPI()

app.include_router(api_router)
app.include_router(product_router)
@app.get("/api/predict")
def predict(size,total_sqft,bath,balcony,location):
     price =list(predict_price(size,total_sqft,bath,balcony,location))[0]
     return {"message":"Success","Data":{"predicted_price":price},"ErrorCode":0}


@app.get("/api/citylist")
def get_cit_map_api():
    """get city list of preidctions"""
    city_map = get_city_map()
    return {"message":"Success","Data":city_map,"ErrorCode":0}


@app.post("/api/UserLogin")
def user_login(user_info:Users):
     last_name =  user_info.last_name if user_info.last_name else ""
     account = AccountCreate(account_id=user_info.user_id,account_name=user_info.first_name + last_name )
     return account.model_dump()

@app.get("/api/name/{name}")
def display_user_name(name:str,donation:int):
     return {"message":"success","Data":f"{name} donated {donation}","errorcode":0}
