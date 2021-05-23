
# https://www.datamuse.com/api/
import requests

url = 'https://api.datamuse.com/words?rel_jjb=ocean&topics=temperature'


resp = requests.get(url=url) #, params=params)
data = resp.json()
print(data)
