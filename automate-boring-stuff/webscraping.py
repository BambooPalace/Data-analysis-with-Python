'''scraping amazon price'''

import bs4
import requests

res = requests.get('https://www.amazon.sg/Automate-Boring-Stuff-Python-2nd-dp-1593279922/dp/1593279922/')

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

#right click text to copy (CSS) selector
price_e = soup.select('#buyNewSection > div > div > span > span')
title_e = soup.select('#productTitle')

price = price_e[0].text.strip()
title = title_e[0].text.strip()

print('the price for the book <<'+title+'>> is ' + price)



'''Future inspirations: download web images, check link for previous and next buttons and get the url; and repeat the downloading.'''