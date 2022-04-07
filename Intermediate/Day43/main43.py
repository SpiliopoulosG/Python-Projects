import requests
from bs4 import BeautifulSoup

date_to_find = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

URL = f"https://www.billboard.com/charts/hot-100/{date_to_find}/"

response = requests.get(url=URL)
response.raise_for_status()
website = response.text



soup = BeautifulSoup(website, "html.parser")
first_song =soup.find(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet" )
song_titles = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only", id="title-of-a-story")

titles = [title.getText().strip() for title in song_titles]
titles.insert(0, first_song.getText().strip())

print(titles)
# c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021  lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis  u-max-width-230@tablet-only
