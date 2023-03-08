from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)
# First article
article_tag = soup.find(name="a")
print(article_tag)
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score ").getText()

print(article_text)
print(article_link)
print(article_upvote)


# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
#
# all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText)
#     print(tag.get("href"))
#
# # Use of select
# name = soup.select_one("#name")
# print (name)
#
# headings = soup.select(".heading")
# print(headings)

