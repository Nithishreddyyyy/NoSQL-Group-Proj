from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from routes.faculty_route import router as faculty_router
from routes.appraisalCat_route import router as criteria_router
from routes.crit_score_route import router as score_router
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request : Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(faculty_router, prefix="/faculty")
app.include_router(criteria_router, prefix="/criteria")
app.include_router(score_router, prefix = "/scores")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)