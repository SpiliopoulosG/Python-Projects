from bs4 import BeautifulSoup
import requests

# with open(file="index.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)


# print(soup.a)
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
#
# my_photo = soup.find(name="img", id="myimage")
# print(my_photo)
#
# my_photo = soup.find(name="img", class_="myimage")
#
# company_url = soup.select_one(selector="p a")
#
# headings = soup.select(".heading")
# print(headings)
#
# response = requests.get("https://news.ycombinator.com/news")
# yc_webpage = response.text
#
# soup = BeautifulSoup(yc_webpage, "html.parser")
# articles = soup.find_all(name="a", class_="titlelink")
# article_texts = []
# article_links = []
# for article in articles:
#     article_texts.append(article.getText())
#     article_links.append(article.get("href"))
#
# article_score_elemnts = soup.find_all(name="span", class_="score")
# article_scores = [int(score.getText().split()[0]) for score in article_score_elemnts]
#
#
#
# print(article_texts)
# print(article_links)
# print(article_scores)
# index = (article_scores.index(max(article_scores)))
# print(article_texts[index], article_links[index])