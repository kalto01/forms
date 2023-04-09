from fastapi import FastAPI
from tinydb import TinyDB, Query

from src.templates import GetFormTemplate


db = TinyDB('database.json')
table = db.table('forms')
app = FastAPI()


@app.post("/get_form")
def get_form(data: GetFormTemplate):
    template = db.search(Query().fragment(data.fields))
    if not template:
        return dict(data=data.fields)
    return dict(data=dict(template_name=template[0]['name']))
