from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/"
                        "best-movies-2/")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

titles_list = []
titles = soup.find_all(name="h3", class_="title")
for title in titles:
    title = title.string
    title = title.replace("â\x80\x93", "-")
    title = title.replace("Ã©", "é")
    titles_list.append(title)

# titles_list = [title.string for title in titles]
movies = titles_list[::-1]
# print(movies)

f = open("movies.txt", "w")
for movie in movies:
    f.write(f"{movie}\n")
f.close()
print("File saved")


