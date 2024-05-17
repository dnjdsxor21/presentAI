from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
# from supabase_db import insert_table
import os 
import json 

PROJECTS = [
        {'name':'Project1', 'project':'p111', 'opinion':'hello', 'goal':'good', "id":1},
        {'name':'Project2', 'project':'1222', 'opinion':'hdello', 'goal':'gdood', "id":2},
        {'name':'Project3', 'project':'a333', 'opinion':'helblo', 'goal':'go2od', "id":3},
        {'name':'Project4', 'project':'b444', 'opinion':'heldlo', 'goal':'gofod', "id":4}
    ]

FILES = [
        {'name':'File1', 'source':'', 'text1':'aoaoaoaoaoaoaoaoaoaogjgjg안녕하세요', 'text2':'hello2', 'importance':90},
        {'name':'File2', 'source':'jajaja.pdf', 'text1':'hello1안녕하세요안녕하세요', 'text2':'hello2', 'importance':0},
        {'name':'File3', 'source':'aaa.docx', 'text1':'aoinoweignoweign;e안녕하세요oigna', 'text2':'hello2', 'importance':36},
        {'name':'File4', 'source':'youtube', 'text1':'hell안녕하세요o1', 'text2':'aoinowe안녕하세요ignoweign', 'importance':85}
    ]

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static") 

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/projects")
async def projects_list(request: Request):
    global PROJECTS
    projects = PROJECTS
    return templates.TemplateResponse("projects.html", {"request": request, "projects":projects})

@app.post("/projects/new")
async def new_project(request: Request, name="", project="", opinion="", goal=""):
    if (name.strip()!="") and (project.strip()!=""):
        # data insert
        pass
    return 

@app.get("/projects/{project_id}")
async def projects(request: Request, project_id:int):
    
    global PROJECTS, FILES
    sorted_files = sorted(FILES, key=lambda x: x['importance'], reverse=True)
    project = PROJECTS[project_id-1]
    return templates.TemplateResponse("data-list.html", {"request": request, "project_id":project_id, 'files':sorted_files, "project":project})

@app.get("/projects/{project_id}/outline")
async def project_ai_outline(request: Request, project_id:int):
    global PROJECTS, FILES
    sorted_files = sorted(FILES, key=lambda x: x['importance'], reverse=True)
    project = PROJECTS[project_id-1]
    return templates.TemplateResponse("data-ai-outline.html", {"request": request, "project_id":project_id, 'files':sorted_files, "project":project})

@app.get("/projects/{project_id}/questions")
async def project_ai_question(request: Request, project_id:int):
    global PROJECTS, FILES
    sorted_files = sorted(FILES, key=lambda x: x['importance'], reverse=True)
    project = PROJECTS[project_id-1]
    return templates.TemplateResponse("data-ai-question.html", {"request": request, "project_id":project_id, 'files':sorted_files, "project":project})

@app.get("/projects/{project_id}/settings")
async def project_settings(request: Request, project_id:int):
    global PROJECTS
    project = PROJECTS[project_id-1]
    return templates.TemplateResponse("data-settings.html", {"request": request, "project_id":project_id, "project":project})


# @app.get("")


