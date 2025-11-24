from bs4 import BeautifulSoup

# import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)

print(soup.find_all(name="a", href=True))


# with open("website.html", "r", encoding="utf-8") as file:
#     html_content = file.read()


# soup = BeautifulSoup(html_content, "lxml")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# # for tag in all_anchor_tags:
# # print(tag.getText())
# # print(tag.get("href"))


# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))


# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)
