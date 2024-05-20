
import os
from dotenv import dotenv_values
from supabase import create_client, Client
import json 

# config = dotenv_values('.env')
# url = config['SUPABASE_URL']
# key = config['SUPABASE_KEY']
# supabase: Client = create_client(url, key)


# def insert_table(email:str, option:str):
#     data, count = supabase.table(TABLE_NAME).insert({
#         ROW1: email, ROW2:option
#         }).execute()
#     return data

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

def get_projects():
    with open('db/json/projects.json', 'r',encoding='utf-8') as f:
        data = json.load(f)
    return data

def get_files():
    with open('db/json/files2.json', 'r',encoding='utf-8') as f:
        data = json.load(f)
    return data

def add_file(data):
    with open('db/json/files2.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__=='__main__':
    pass