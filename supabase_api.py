
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import json 

config = load_dotenv()
url = os.environ['SUPABASE_URL']
key = os.environ['SUPABASE_KEY']
supabase: Client = create_client(url, key)

def fetch_projects(project_id:int=-1):
    try:
        if project_id >=0 :
            response = supabase.table("projects").select("*").eq("id", project_id).execute()
            data = response.data[0]
        else:
            response = supabase.table("projects").select("*").execute()
            data = response.data
            if len(data) < 4:
                for i in range(4 - len(data)): data.append({"name": "Project","topic": "Sample data","opinion": "","goal": "","id": 999})
    except Exception as e:
        print(e)
        data = {"name": "Project","topic": "Sample data","opinion": "","goal": "","id": 999}
    return data

def insert_projects(options:dict):
    response = supabase.table("projects").insert(
        options
    ).execute()
    return response.data

def fetch_files(project_id:int):
    response = supabase.table("files").select("*").eq("project_id", project_id).execute()
    files = response.data
    if not files:
        files = [{
        "name": "데이터를 추가해보세요",
        "source": "text",
        "text": "데이터 내용입니다.",
        "summary": "데이터 요약입니다.",
        "tags": "#데이터를 #추가 #해보세요",
        "importance": 80,
        "id": 999,
        "project_id": project_id
    }]
    return files

def insert_files(options:dict):
    response = supabase.table("files").insert(
        options
    ).execute()
    return response.data

# def upsert_table(id:list, email:list, option:list):
#     data, count = supabase.table(TABLE_NAME).upsert(
#         [ {'id':a, ROW1:b, ROW2:c} for (a,b,c,d) in zip(id, email, option)]
#         ).execute()
#     return data

# def signup_email(email, password):
#     credentials = {
#     "email": email,
#     "password": password
#   }
#     user = supabase.auth.sign_up(credentials)
#     return user

# def login_email(email, password):
#     data = supabase.auth.sign_in_with_password({"email": email, "password": password})
#     return data

# def login_google():
#     data = supabase.auth.sign_in_with_oauth({
#   "provider": 'google'
#     })
#     return data

if __name__=='__main__':
    pass