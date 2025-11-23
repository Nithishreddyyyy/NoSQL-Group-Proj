from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes.faculty_route import router as faculty_router
from app.routes.appraisalCat_route import router as criteria_router
from app.routes.crit_score_route import router as score_router
app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def index(request : Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(faculty_router, prefix="/faculty")
app.include_router(criteria_router, prefix="/criteria")
app.include_router(score_router, prefix = "/scores")