from bs4 import BeautifulSoup
import lxml

with open("website.html", "r", encoding="utf-8") as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, "lxml")
# print(soup.title)
# print(soup.title.string)
print(soup.prettify())
