from fastapi import APIRouter
api_router = APIRouter(prefix="/api/v2/userlogin")

@api_router.get("/signin")
def welcome():
    return {"message":"success","data":{},"errorcode":1}
@api_router.get("/signup")
def signup():
    return {"message":"success","data":{},"errorcode":1}


@api_router.post("/otpRequest")
def otpHandle():
    return {}
