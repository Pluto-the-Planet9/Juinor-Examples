import requests
from bs4 import BeautifulSoup

url = "https://www.wunderground.com/weather/us/oh/youngstown"
info = requests.get(url)
soup = BeautifulSoup(info.text, "html.parser")
print(soup.prettfy())

html_element = soup.find_all("a")

for item in html_element

