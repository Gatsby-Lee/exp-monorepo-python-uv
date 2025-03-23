from fastapi import FastAPI
from py_zcommonlib.datetime_lib import get_utc_timestamp

app = FastAPI()


@app.get("/")
async def utc_timestamp():
    return get_utc_timestamp()
