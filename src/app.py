import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import Dict
import logging
from config.settings import logging_config, settings
from data_validation_utils.field_validation import get_field_type
from data_validation_utils.fill_db import example_form


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logging_config("INFO")
        async_client = AsyncIOMotorClient(settings.URL_DATABASE)
        async_db = async_client[settings.DB_NAME]
        async_form_collection = async_db[settings.DB_COLLECTION]
        app.state.async_form_collection = async_form_collection

        for form in example_form:
            await app.state.async_form_collection.update_one({"name": form["name"]}, {"$set": form}, upsert=True)
        yield
    except Exception as e:
        sys.exit(1)


app = FastAPI(lifespan=lifespan)
log = logging.getLogger(__name__)


class FormTemplate(BaseModel):
    name: str
    fields: Dict[str, str]


@app.post("/get_form")
async def get_form(request: Request):
    try:
        data = dict(request.query_params)
        print(data)
        if not data or len(data) == 0:
            log.error("No data in request")
            return {"error": "No data in request"}
        forms = await app.state.async_form_collection.find().to_list(None)
        print(f'forms: {forms}')
        for form in forms:
            form_fields = form.get('fields', {})
            if all(field in data for field in form_fields):
                log.info(f"Form found: {form.get('name')}")
                return {"form_name": form.get('name')}

        typed_fields = {}
        for field, value in data.items():
            typed_fields[field] = get_field_type(value)
        log.info(f"Typed fields: {typed_fields}")
        return typed_fields
    except Exception as e:
        log.error(f"Error: {str(e)}")
        return {"error": "Error processing request"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
