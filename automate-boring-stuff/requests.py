import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()#raise exception if downloading fails

file = open('romeojuliet.txt','wb') # use 'wb' to keep unicode format
for chunk in res.iter_content(10000):
	file.write(chunk)
file.close()