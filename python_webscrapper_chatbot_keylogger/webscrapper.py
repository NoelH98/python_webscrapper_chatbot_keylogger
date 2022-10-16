import requests
from bs4 import BeautifulSoup
import random

r = requests.get('https://wisdomquoyes.com/zen-quotes/')
soup = BeautifulSoup(r.text, 'html.parser')

texts = []

for quote in soup.find_all('blockquote'):
    texts.append(quote.p.text)

print(random.choice(texts))