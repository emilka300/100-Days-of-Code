from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
print(response.text)

soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())

article_url = soup.find(name="span", class_="titleline").a.get("href")
article_text = soup.find(name="span", class_="titleline").a.string
article_upvote = soup.find(name="span", class_="score", id="score_41721668").string
print(article_url)
print(article_text)
print(article_upvote)

links = []
texts = []

articles = soup.find_all(name="span", class_="titleline")
for art in articles:
    link = art.a.get("href")
    links.append(link)
    text = art.a.string
    texts.append(text)

upvotes = [int(score.string.split()[0]) for score in soup.find_all(name="span", class_="score")]

print(links)
print(texts)
print(upvotes)

highest_value = max(upvotes)
index_h_value = upvotes.index(highest_value)
print(index_h_value)

print(links[index_h_value])
print(texts[index_h_value])
print(upvotes[index_h_value])



