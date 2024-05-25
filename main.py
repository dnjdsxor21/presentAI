from fastapi import FastAPI, Request, HTTPException, File, UploadFile,Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
import supabase_api
from gpt_api import gpt35
import uuid
import re
import os 
import json 
import time

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static") 
app.mount("/db", StaticFiles(directory="db"), name="db") 


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/projects")
async def projects_list(request: Request):
    projects = supabase_api.fetch_projects()
    return templates.TemplateResponse("projects.html", {"request": request, "projects":projects})

@app.post("/projects/new")
async def new_project(request: Request, name:str="", topic:str="", opinion:str="opinion", goal:str="goal"):
    if (name.strip()!="") and (topic.strip()!=""):
        # data insert
        options = {
            "name":name,
            "topic":topic,
            "opinion":opinion,
            "goal":goal
        }
        print(options)
        supabase_api.insert_projects(
            options
        )
    return 

@app.get("/projects/{project_id}")
async def projects(request: Request, project_id:int):
    
    project = supabase_api.fetch_projects(project_id=project_id)
    files = supabase_api.fetch_files(project_id=project_id)
    # print(project)
    # print(files)
    sorted_files = sorted(files, key=lambda x: x['importance'], reverse=True)

    return templates.TemplateResponse("data-list.html", {"request": request, 'files':sorted_files, "project":project})

@app.post("/projects/{project_id}/new")
async def new_file(request: Request, project_id:int, name=Form(None), text=Form(None)):
    project = supabase_api.fetch_projects(project_id=project_id)

    if "yout" in text:
        source = "youtube"
        text = extract_youtube(text)
        if 'error' in text:
            supabase_api.insert_files({'name':name, 'source':source, 'text':"Link Error", 'summary':"Link Error", "tags": "", 'importance':1, "project_id":project_id})
            return
    else:
        source="text"
    
    prompt = f"제목:{name}\n내용:{text}\n나의 의견:{project['topic']} {project['opinion']}\요약:"
    summary = gpt35(system=f"나의 의견을 참고해서 자료를 요약해줘. 그리고 다음 예시처럼 3개의 hashtags를 작성해줘(#사전 #네이버 #범죄)",
                       user=prompt)
    # print(summary)
    try:
        tags = " ".join(re.findall(r"#\s*\w+", summary))
    except:
        tags = " "

    try:
        score = gpt35(system=f"자료와 나의 의견을 비교해서 자료의 중요도를 1부터 100까지의 점수로 평가해줘.",
                    user=f"제목:{name}\n내용:{text}\n나의 의견:{project['topic']} {project['opinion']}\n점수:")
        score = max([int(s) for s in re.findall(r"\d+", score)])
    except:
        score = 10
    
    supabase_api.insert_files({'name':name, 'source':source, 'text':text, 'summary':summary, "tags": tags, 'importance':score, "project_id":project_id})
    return 
    


@app.get("/projects/{project_id}/outline")
async def project_ai_outline(request: Request, project_id:int):
    project = supabase_api.fetch_projects(project_id=project_id)
    files = supabase_api.fetch_files(project_id=project_id)

    sorted_files = sorted(files, key=lambda x: x['importance'], reverse=True)
    return templates.TemplateResponse("data-ai-outline.html", {"request": request, 'files':sorted_files, "project":project})

@app.post("/projects/{project_id}/outline")
async def generate_outline(request: Request, project_id:int):
    try:
        project = supabase_api.fetch_projects(project_id=project_id)
        files = supabase_api.fetch_files(project_id=project_id)

        sorted_files = sorted(files, key=lambda x: x['importance'], reverse=True)


        prompt = '\n'.join([ f"자료{idx}\n제목:{file['name']} 내용:{file['summary']}" for idx, file in enumerate(sorted_files[:6]) ])
        completion = gpt35(
            system= '다음 자료를 참고해서 발표 개요를 작성해줘.',
            user= f"발표주제: {project['topic']} {project['opinion']}\n{prompt}"
        )
        return JSONResponse(completion.split('\n'))
    except Exception as e:
        print(e)
        return JSONResponse(["Outline Error"])

@app.get("/projects/{project_id}/questions")
async def project_ai_question(request: Request, project_id:int):
    project = supabase_api.fetch_projects(project_id=project_id)
    files = supabase_api.fetch_files(project_id=project_id)

    sorted_files = sorted(files, key=lambda x: x['importance'], reverse=True)

    return templates.TemplateResponse("data-ai-question.html", {"request": request, 'files':sorted_files, "project":project})

@app.post("/projects/generate-questions")
async def generate_questions(request: Request, file: UploadFile=File(...)):
    text = await read_file(file)
    
    
    ## text -> questions
    # questions = [
    #     "This is question A",
    #     "This is question B",
    #     "This is question C"
    # ]
    # time.sleep(5)
    try:
        completion = gpt35(
                system= '발표 대본을 보고 예상가능한 질문 3개를 파이썬 리스트 포맷으로 작성해줘. example:["This is question A","This is question B","This is question C"]',
                user= text
            )
        print(completion)
        questions = re.findall(r'\"(.+)\"',completion) if re.findall(r'\"(.+)\"',completion) else completion
        
        print("")
        print(type(questions))
        print(questions)
    except Exception as e:
        print(e)
        questions = ["This is question A","This is question B","This is question C"]
    return questions

@app.get("/projects/{project_id}/settings")
async def project_settings(request: Request, project_id:int):
    project = supabase_api.fetch_projects(project_id=project_id)

    return templates.TemplateResponse("data-settings.html", {"request": request, "project":project})

@app.post("/projects/{project_id}/edit")
async def project_edit(request: Request, project_id:int, col1=Form(None), col2=Form(None), col3=Form(None), col4=Form(None)):
    print(col1, col2, col3, col4)
    return

@app.post("/projects/{project_id}/delete")
async def project_delete(request: Request, project_id:int):
    print(project_id)
    return

@app.get("/signup")
async def signup(request:Request):
    return templates.TemplateResponse("signup.html", {"request": request})

# @app.post("/signup")
# async def signup_email(email=Form(...), password=Form(...)):
#     response = supabase_api.signup_email(email, password)
#     print(response)
#     if response.get("error"):
#         raise HTTPException(status_code=400, detail=response["error"]["message"])
#     return JSONResponse(content=response)


# @app.post("/login")
# async def login_email(email=Form(...), password=Form(...)):
#     data = supabase_api.login_email(email, password)
#     return data 

# @app.post("/google")
# async def login_google():
#     data = supabase_api.login_google()
#     print(data.url)
#     return RedirectResponse(data.url)



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


def extract_youtube(video_link:str):
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api.formatters import TextFormatter
    

    # # YouTube 영상 ID
    if 'shorts' in video_link:
        video_id = video_link.split('/')[-1]
    elif 'watch' in video_link:
        video_id = re.findall(r"v=([\w\-\_]+)", video_link)
    else:
        video_id = re.findall(r'[\w\-\_]+', video_link.split('/')[-1])[0]

    try:
        # 스크립트 가져오기
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko','en'])
        
        # 스크립트를 일반 텍스트로 변환
        formatter = TextFormatter()
        text_transcript = formatter.format_transcript(transcript_list)
        
        # print(text_transcript)
    except Exception as e:
        # print(f"스크립트를 가져오는 데 실패했습니다: {e}")
        return "Link Error"
    return text_transcript