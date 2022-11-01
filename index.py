from xml.etree.ElementInclude import include
from fastapi import FastAPI

from routes.index import user

app=FastAPI()

app.include_router(user)
