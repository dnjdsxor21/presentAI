from fastapi import FastAPI, Request, HTTPException, File, UploadFile,Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
# from supabase_db import insert_table
import os 
import json 
import time

PROJECTS = [
        {'name':'Project1', 'project':'p111', 'opinion':'hello', 'goal':'good', "id":1},
        {'name':'Project2', 'project':'1222', 'opinion':'hdello', 'goal':'gdood', "id":2},
        {'name':'Project3', 'project':'a333', 'opinion':'helblo', 'goal':'go2od', "id":3},
        {'name':'Project4', 'project':'b444', 'opinion':'heldlo', 'goal':'gofod', "id":4}
    ]

FILES = [
        {'name':'File1', 'source':'', 'text1':'aoaoaoaoaoaoaoaoaoaogjgjg안녕하세요', 'text2':'hello2', 'importance':90, "id":1},
        {'name':'File2', 'source':'jajaja.pdf', 'text1':'hello1안녕하세요안녕하세요', 'text2':'hello2', 'importance':0, "id":2},
        {'name':'File3', 'source':'aaa.docx', 'text1':'aoinoweignoweign;e안녕하세요oigna', 'text2':'hello2', 'importance':36, "id":3},
        {'name':'File4', 'source':'youtube', 'text1':'hell안녕하세요o1', 'text2':'aoinowe안녕하세요ignoweign', 'importance':85, "id":4}
    ]

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static") 

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

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
    return templates.TemplateResponse("data-list.html", {"request": request, 'files':sorted_files, "project":project})

@app.get("/projects/{project_id}/outline")
async def project_ai_outline(request: Request, project_id:int):
    global PROJECTS, FILES
    sorted_files = sorted(FILES, key=lambda x: x['importance'], reverse=True)
    project = PROJECTS[project_id-1]
    return templates.TemplateResponse("data-ai-outline.html", {"request": request, 'files':sorted_files, "project":project})

@app.post("/projects/{project_id}/outline")
async def generate_outline(request: Request, project_id:int):
    global PROJECTS, OUTLINE
    project = PROJECTS[project_id-1]
    ## outline extract
    time.sleep(5)
    return JSONResponse(OUTLINE.split('\n'))


@app.get("/projects/{project_id}/questions")
async def project_ai_question(request: Request, project_id:int):
    global PROJECTS, FILES
    sorted_files = sorted(FILES, key=lambda x: x['importance'], reverse=True)
    project = PROJECTS[project_id-1]
    return templates.TemplateResponse("data-ai-question.html", {"request": request, 'files':sorted_files, "project":project})

@app.post("/projects/generate-questions")
async def generate_questions(request: Request, file: UploadFile=File(...)):
    text = await read_file(file)
    
    ## text -> questions
    questions = [
        "This is question A",
        "This is question B",
        "This is question C"
    ]
    time.sleep(5)
    return questions

@app.get("/projects/{project_id}/settings")
async def project_settings(request: Request, project_id:int):
    global PROJECTS
    project = PROJECTS[project_id-1]
    return templates.TemplateResponse("data-settings.html", {"request": request, "project":project})

@app.post("/projects/{project_id}/edit")
async def project_edit(request: Request, project_id:int, col1=Form(None), col2=Form(None), col3=Form(None), col4=Form(None)):
    print(col1, col2, col3, col4)
    return

@app.post("/projects/{project_id}/delete")
async def project_delete(request: Request, project_id:int):
    print(project_id)
    return




OUTLINE = """자료 정리 및 계획
1. 통합 자료 관리

다양한 형태의 자료(문서, 이미지, 영상 등)를 한 곳에 모아 체계적으로 관리할 수 있습니다.
자료의 중요도, 용도 등을 태그하여 손쉽게 검색하고 활용할 수 있습니다.
예를 들어 Asana와 같은 프로젝트 관리 도구를 활용하여 자료를 체계적으로 정리할 수 있습니다. 2
2. 발표 연습 및 피드백

발표 영상을 녹화하고 저장할 수 있습니다.
녹화된 영상에 대해 AI가 피드백을 제공하여 발표 스킬 향상을 돕습니다.
주변인들의 피드백을 수집하고 관리할 수 있습니다.
이를 통해 발표 전 충분한 연습과 피드백 수집이 가능합니다.
3. 팀 협업

팀원들과 자료를 공유하고 함께 관리할 수 있습니다.
팀 단위 발표 연습 및 피드백을 진행할 수 있습니다.
팀워크와 협업 능력을 향상시킬 수 있습니다.
4. 발표 통합 솔루션

자료 관리, 발표 연습, 피드백 수집 등의 기능을 하나의 솔루션에서 제공합니다.
학교 및 기관에서 발표 준비 및 관리를 위해 활용할 수 있습니다.
이와 같은 체계적인 자료 관리와 발표 준비 과정을 통해 데이터 리터러시와 비판적 사고력을 향상시킬 수 있습니다. 또한 발표 능력 향상과 팀워크 강화의 효과도 기대할 수 있습니다."""


async def read_file(file):
    text = ""
    if file.filename.endswith(".txt"):
        contents = await file.read()
        text = contents.decode("utf-8")  # 인코딩을 지정하여 한국어 처리
    elif file.filename.endswith(".pdf"):
        import fitz  # PyMuPDF
        contents = await file.read()
        
        # 임시 파일로 저장
        with open("temp.pdf", "wb") as f:
            f.write(contents)
            
        # PDF 파일 열기
        doc = fitz.open("temp.pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
    elif file.filename.endswith('.docx'):
        from docx import Document
        import io
        contents = await file.read()
        
        # 바이트 스트림으로 DOCX 파일을 읽음
        document = Document(io.BytesIO(contents))
        text = ""
        for para in document.paragraphs:
            text += para.text
    else:
        text = "none"
    return text