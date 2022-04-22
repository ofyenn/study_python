"""

В этой задаче вам необходимо воспользоваться API сайта artsy.net
API проекта Artsy предоставляет информацию о некоторых деятелях
искусства, их работах, выставках.
В рамках данной задачи вам понадобятся сведения о деятелях искусства
(назовем их, условно, художники).
Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе
рождения.
Выведите имена художников в порядке неубывания года рождения. В случае
если у художников одинаковый год рождения, выведите их имена в
лексикографическом порядке.

"""

import requests
import json
import time

with open('actors_id.txt') as f:
    list_id = f.readlines()

token ='eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6ImFydHN5Iiwic3ViamVjdF9hcHBsaWNhdGlvbiI6IjVkNDA5OTZlNmU2MDQ5MDAwNzQ5MGZhMiIsImV4cCI6MTYzNjk5MzM5OSwiaWF0IjoxNjM2Mzg4NTk5LCJhdWQiOiI1ZDQwOTk2ZTZlNjA0OTAwMDc0OTBmYTIiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNjE4OTRlZjc1OTEzZmQwMDBiMzg2ZmFmIn0.aei_KO5_W0xqU8Ir3ai1BggaUxLzC6EqeammzLe3YGI'
headers = {"X-Xapp-Token" : token}
dict_artist = {}
for id_actor in list_id:
    time.sleep(1)
    url = "https://api.artsy.net/api/artists/" + id_actor.strip()
    r = requests.get(url, headers=headers)
    j = json.loads(r.text)
    dict_artist[j['sortable_name']] = int(j['birthday'])
    dict_artist = sorted(dict_artist.items(), key=lambda x: (x[1], x[0]))
    for actor in dict_artist:
        print(actor[0], actor[1])



