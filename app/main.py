# https://medium.com/thelorry-product-tech-data/aws-lambda-fastapi-ci-cd-pipeline-with-github-actions-c414866b2d48

from fastapi import FastAPI
from mangum import Mangum
from api.v1.api import router as api_router

app = FastAPI(title='Serverless Lambda FastAPI')

app.include_router(api_router, prefix="/api/v1")

@app.get("/",  tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome Kevin to your ROOT CI/CD Pipeline with GitHub Actions!"}
	
@app.get("/kevin",  tags=["Endpoint Test-2"])
def main_endpoint_test2():
    return {"message": "Welcome Kevin Cusack to your /kevin endpoint CI/CD Pipeline with GitHub Actions!"}

# to make it work with Amazon Lambda, we create a handler object
handler = Mangum(app=app)