import os 
import tiktoken
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

def limit_token(text:str, limit=1000):
    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
    return enc.decode(enc.encode(text)[:limit])

def gpt35(system, user):
    client = OpenAI(
        api_key=os.environ['OPENAI_API_KEY']
    )
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": limit_token(user)}
            ],
            max_tokens=4000
        )
        output = completion.choices[0].message.content
    except:
        output = 'error'
    return output

