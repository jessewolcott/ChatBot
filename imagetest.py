# create.py

import os
import openai
import keys

PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"

openai.api_key = keys.apptoken
response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="1024x1024",
)


print(response["data"][0]["url"])