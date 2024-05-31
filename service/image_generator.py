import requests

response = requests.post(
  f"https://api.stability.ai/v2beta/stable-image/edit/inpaint",
  headers={
    "authorization": f"Bearer ",
    "accept": "image/*"
  },
  files={
    "image": open("../resources/dwayne_johnson.png", "rb")
  },
  data={
    "prompt": "Create a ponytail hairstyle with french beard",
    "search_prompt": "celebrity",
    "output_format": "webp",
  },
)

if response.status_code == 200:
  with open("../output/updated-style.webp", 'wb') as file:
    file.write(response.content)
else:
  raise Exception(str(response.json()))