from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services.faculty_crit_score_service import (
    get_faculty_score,
    calculate_total_score,
    update_faculty_score,
    initialize_faculty_scores
)
from app.services.faculty_service import get_all_faculty
from app.services.appraisalCat_service import get_all_criteria

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def scores_page(request: Request):
    await initialize_faculty_scores()
    faculty_list = await get_all_faculty()
    criteria_list = await get_all_criteria()
    
    faculty_with_scores = []
    for faculty in faculty_list:
        score_data = await get_faculty_score(faculty["id"])
        total_score = await calculate_total_score(faculty["id"])
        faculty_with_scores.append({
            **faculty,
            "selected_criteria": score_data.get("criterion_name", []) if score_data else [],
            "total_score": total_score
        })
    
    return templates.TemplateResponse("scores.html", {
        "request": request,
        "scores": faculty_with_scores,
        "all_criteria": criteria_list
    })

@router.post("/update/{faculty_id}")
async def update_score(
    faculty_id: str,
    criteria: list = Form(default=[])
):
    await update_faculty_score(faculty_id, criteria)
    return RedirectResponse("/scores/", status_code=303)