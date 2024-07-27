
from openai import OpenAI
from pool.server import config

def init():
    conf = config()
    global client
    client = OpenAI(base_url=conf.url, api_key=conf.api_key)
    global history 
    history = [
        {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    ]
def send(msg:str):
    history.append({"role": "user", "content": msg})
    completion = client.chat.completions.create(
        model="cognitivecomputations/dolphin-2.9-llama3-8b-gguf",
        messages=history,
        temperature=0.7,
        stream=True,
    )
    new_message = {"role": "assistant", "content": ""}    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content
    history.append(new_message)

