from curl_cffi import requests
from bs4 import BeautifulSoup
import re

url = "https://static.prts.wiki/voice/char_003_kalts/CN_067.wav"
response = requests.get(url)

#soup = BeautifulSoup(response.text, 'html.parser')
#print (soup.find_all("PRTS"))
print(response.status_code)