"""

Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида
<a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами
поддоменов. То есть, это последовательность символов, которая следует
сразу после символов протокола, если он есть, до символов порта или пути,
если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

"""

import requests
import re


def get_lins(url):
    text_url = requests.get(url).text
    links = re.findall(r'<a.*href=[\'\"](.+)[\'\"\:\"]', text_url)
    answer = []
    for link in links:
        if link[0] in ['.']:
            continue
        pos = link.find('//')
        if pos != -1:
            link = link[pos+2:]

        link = re.split(':|/|\"|\'', link)[0]
        if link not in answer:
            answer.append(link)
    answer.sort()
    return(answer)


a = input()
links = get_lins(a)
for link in links:
    print(link)


