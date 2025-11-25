import requests
from bs4 import BeautifulSoup

year = input(int(input("Enter a year: ")))
URL = "https://www.billboard.com/charts/hot-100/" + year
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}


response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
music_titles_spans = soup.select("li lu li h3")

music_titles = [music.getText() for music in music_titles_spans]
