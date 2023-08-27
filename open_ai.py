import os
import random

import openai
from config import apikey

openai.api_key = apikey

def ai(text):
  result = f"OpenAI response for Prompt: {text} \n *******************\n"
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": text
      },
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  #todo: Write this inside a try-catch
  try:
    result += response["choices"][0]["message"]["content"]
    if not os.path.exists("../../MyProjects/AI Assistant/OpenAI"):
      os.mkdir("../../MyProjects/AI Assistant/OpenAI")

    with open(f"OpenAI/prompt - {text[:10]}.txt", "w") as f:
      f.write(result)
  except Exception as e:
    return "Some error occurred!"
  return result

