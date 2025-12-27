from fastapi import FastAPI
import asyncio
from role.tradr.actions.buy import Buy
from role.tradr.events.moomo import MooMoo
from schema.user import User
from fastapi import Request

app = FastAPI()

async def func_tradr(data: dict,req) -> User:

    return await MooMoo().request_response(req)

@app.get("/health")
async def healthcheck(req: Request,app: str) -> dict[str,str]:
    if app == "tradr":
        return await func_tradr({"message": "Hello World"},req)
    else:
        return {}

@app.get("/get_data")
async def get_data(app: str, conf: dict[str,str]|str) -> dict[str, str | int]:
    if app == "tradr":
        return await func_tradr({"data": conf, "value": 42})
    else:
        return {}

@app.post("/post_data")
async def post_data(app: str, conf: dict[str,str]|str) -> dict[str, str | int]:
    if app == "tradr":
        return await func_tradr({"data": conf, "value": 100})
    else:
        return {}

