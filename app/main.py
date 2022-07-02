# https://www.deadbear.io/simple-serverless-fastapi-with-aws-lambda/
# https://medium.com/thelorry-product-tech-data/aws-lambda-fastapi-ci-cd-pipeline-with-github-actions-c414866b2d48

# https://lsh8cin25k.execute-api.us-east-2.amazonaws.com/Dev
# https://lsh8cin25k.execute-api.us-east-2.amazonaws.com/Dev/kevin
# https://lsh8cin25k.execute-api.us-east-2.amazonaws.com/Dev/api/v1/test/
# https://lsh8cin25k.execute-api.us-east-2.amazonaws.com/Dev/api/v1/users/
# https://lsh8cin25k.execute-api.us-east-2.amazonaws.com/Dev/api/v1/posts/
# http://127.0.0.1:8000/api/v1/test/
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/kevin
# http://127.0.0.1:8000/redoc
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/api/v1/test/      I need the final forward slash here
# http://127.0.0.1:8000/api/v1/users/
# http://127.0.0.1:8000/api/v1/posts/

# uvicorn main:app --reload                 cd into app - cd app

from fastapi import FastAPI
from mangum import Mangum
from api.api_v1.api import router as api_router

app = FastAPI(title='Serverless Lambda FastAPI')
app.include_router(api_router, prefix="/api/v1")

@app.get("/",  tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome Kevin to your ROOT CI/CD Pipeline with GitHub Actions!"}
	
@app.get("/kevin/{item_id}",  tags=["Endpoint Test-2"])
def main_endpoint_test2(item_id: int):
    return {"Welcome Kevin Cusack to your /kevin endpoint CI/CD Pipeline with GitHub Actions! Id sent=": item_id}

handler = Mangum(app=app) # to make it work with Amazon Lambda, we create a handler object using Mangum