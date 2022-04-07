import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
website = response.text

titles = []

soup = BeautifulSoup(website, "html.parser")
html_titles = soup.find_all(name="h3", class_="title")
for title in html_titles:
    titles.append("\n")
    titles.append(title.getText())

# print(titles)

with open(file="movies.txt", mode="w") as file:
    file.writelines(titles[::-1])