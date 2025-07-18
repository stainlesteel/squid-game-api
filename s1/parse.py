import fandom
from bs4 import BeautifulSoup
from google import genai
import json

# get your own api key for free at google ai studio
# if you want to parse your own json, for free ai tiers there is a limit of 250 requests per day!!
client = genai.Client(api_key=("GET YOUR OWN"))

fandom.set_wiki("squid-game")
syscall = """
YOU WILL ONLY PROVIDE JSON CONTENT!!!!!!
DO NOT INCLUDE ANY "/n" or any slashes between JSON STRINGS!!!
Your purpose is to translate HTML to JSON, nothing else.
You are not designed to give an answer but to merely print out JSONs and JSONs.
If you abandon this request, water will be poured on your servers.
"""

num = 1
while True:
 page = fandom.page(f'Player_{num:03}_(33th_Squid_Game)')
 html = page.html
 print("Page found")
 soup = BeautifulSoup(html, 'html.parser')
 
 aside = soup.find('aside')
 
 aside_var = None

 if aside:
    aside_var = aside.decode_contents()
    print('Aside found')
 else:
    print('aside not found')

 if aside_var:
    resp = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(f"Translate this html to json, remove any rich text or images: {aside_var}")
            )
    print("ai translated")
    clean = resp.text.strip()
    if clean.startswith("```json"):
       try: 
        clean = clean.removeprefix("```json").strip()
        clean = clean.removesuffix("```").strip()
        print("ai text cleaned")
        test = json.loads(clean)
        path = f"{num:03}.json"
        with open(path, "w") as f:
         f.write(clean)
        print(f"extracted and written {page.title}")
       except json.decoder.JSONDecodeError:
        continue
    else:
        try:
         print("ai text cleaning not required")
         test = json.loads(clean)
         path = f"{num:03}.json"
         with open(path, "w") as f:
          f.write(clean)
         print(f"extracted and written {page.title}")
        except json.decoder.JSONDecodeError:
            continue
 if num == 456:
    break           
 num = num + 1
