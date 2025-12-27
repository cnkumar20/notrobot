from typing import Any
from schema.user import User
from fastapi import FastAPI,Request
class MooMoo:
    def __init__(self, conf: dict) -> None:
        self.id = self._meta_data(conf)["id"]

    def _meta_data(self, conf: Any) -> Request: 
        # Simulate creating a connection using the provided configuration
        return conf["meta_data"]
    
    async def place_order(self, conf:dict) -> User:
        # Simulate processing the request and retu`rning a response
        req = Request(conf)
        resp = await req.json() 
        return User(**resp)

    async def sell(self, conf:dict) -> User:
        # Simulate processing the request and returning a response
        req = Request(conf)
        resp = await req.json() 
        return User(**resp)
   
    async def get_equity_data(self, conf:dict) -> Any):
        pass    


