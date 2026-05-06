from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from services import crud
from data.database import SessionLocal

router = APIRouter()
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "tasks": tasks
    })


@router.post("/add")
def add(
    title: str = Form(...),
    status: str = Form(""),
    priority: str = Form(""),
    deadline: str = Form(""),
    db: Session = Depends(get_db)
):
    crud.create_task(db, title, status, priority, deadline)
    return RedirectResponse("/", status_code=302)

@router.get("/edit/{task_id}")
def edit_page(task_id: int, request: Request, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id)

    return templates.TemplateResponse("edit.html", {
        "request": request,
        "task": task
    })

@router.post("/edit/{task_id}")
def edit_task(
    task_id: int,
    title: str = Form(...),
    status: str = Form(""),
    priority: str = Form(""),
    deadline: str = Form(""),
    db: Session = Depends(get_db)
):
    crud.update_task(db, task_id, title, status, priority, deadline)
    return RedirectResponse("/", status_code=302)


@router.get("/delete/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    crud.delete_task(db, task_id)
    return RedirectResponse("/", status_code=302)