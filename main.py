from fastapi import FastAPI, Request, HTTPException, File, UploadFile,Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
# from supabase_db import insert_table
import os 
import json 
import time

PROJECTS = [
        {'name':'촉법소년', 'project':'촉법소년 처벌 현황', 'opinion':'촉법소년 처벌 강화가 필요한 이유', 'goal':'good', "id":1, "image":"cover1.jpeg"},
        {'name':'공인탐정', 'project':'공인 탐정의 문제', 'opinion':'공인 탐정의 문제', 'goal':'gdood', "id":2, "image":"cover2.jpeg"},
        {'name':'Project3', 'project':'a333', 'opinion':'helblo', 'goal':'go2od', "id":3, "image":"metamong.webp"},
        {'name':'Project4', 'project':'b444', 'opinion':'heldlo', 'goal':'gofod', "id":4}
    ]

FILES = [
        {'name':'촉법소년이란', 'source':'','text1':'https://terms.naver.com/entry.naver?docId=1965556&cid=43667&categoryId=43667', 'text2':'#네이버 #사전', 'importance':90, "id":1},
        {'name':'대낮 칼부림', 'source':'', 'text1':'https://www.hankyung.com/article/202405147432i', 'text2':'#뉴스 #칼부림', 'importance':45, "id":2},
        {'name':'사회적인식',  'source':'youtube', 'text1':'https://youtu.be/sPD8bm4aLqs?si=fkVeqlWFBbpFjnh7', 'text2':'#youtube', 'importance':80, "id":3},
        {'name':'File4', 'source':'youtube', 'text1':'sample', 'text2':'sample2', 'importance':10, "id":4}
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




OUTLINE = """프레젠테이션 개요: "촉법소년 처벌 강화의 필요성"
1. 서론
현재 촉법소년에 대한 정의 및 법적 취급 소개
최근 촉법소년에 의한 범죄 사례 소개 및 사회적 문제 제기
2. 촉법소년에 대한 현재 법적 대응
촉법소년에 대한 형벌이 아닌 보호처분의 법적 근거
현재 적용되는 보호처분의 종류 및 절차
3. 촉법소년 처벌 강화의 필요성
촉법소년에 의한 범죄의 심각성 및 재발 우려
사례 분석: 경기 양주 초등학생 칼부림 사건
범죄 예방 및 재발 방지를 위한 처벌 강화의 중요성
사회적, 심리적 영향 고려: 촉법소년에 대한 일반인의 인식 및 불안감
4. 처벌 강화를 위한 구체적 방안
촉법소년 연령 하향 조정의 검토
처벌과 병행한 교육 및 상담 프로그램의 강화
재범 방지를 위한 사회적 지원 및 모니터링 체계 구축
5. 사례 및 연구 자료
다른 국가의 촉법소년 처벌 및 교육 정책 비교
전문가 의견 및 심리학적, 사회학적 연구 결과 소개
6. 반대 의견 및 논쟁점
처벌 강화에 대한 반대 의견 소개 및 반박
처벌과 교육의 균형에 대한 논의
7. 결론 및 제언
촉법소년 처벌 강화의 필요성 재확인
법적, 사회적 차원에서의 종합적 대책 제안
보충 자료
촉법소년 범죄 통계 및 추세 분석
심리학적, 사회학적 관점에서의 촉법소년 범죄 원인 분석
촉법소년을 위한 성공적인 교정 프로그램 사례
대중매체 및 SNS에서의 촉법소년 관련 인식 조사 결과"""


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