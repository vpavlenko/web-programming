from bs4 import BeautifulSoup

html = open('index.html').read()

soup = BeautifulSoup(html)

for tag in soup.find_all(class_='post_title'):
    print(tag.get_text())
