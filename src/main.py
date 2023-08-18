from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="AI consulting site"
    )

templates = Jinja2Templates(directory="../inside_net/templates")
app.mount("/templates", StaticFiles(directory="../inside_net/templates"), name="templates")



@app.get("/")
def get_index_html(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})