import os
import openai
import keys
openai.api_key = keys.apptoken
response = openai.Image.create(
  prompt="",
  n=2,
  size="1024x1024"
)

print(response["data"][0]["url"])