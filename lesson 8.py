import requests

'''coin_list = []

response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem in response_parse:
    if parse_elem.startswith("$"):
        for parse_elem_2 in parse_elem.split("</span>"):
            if parse_elem_2.startswith("$"):
                coin_list.append((parse_elem_2.split("$")[1]))

print(float(coin_list[0].replace(",", "")))'''

from bs4 import BeautifulSoup

response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", {"href":"/currencies/bitcoin/#markets"})
    res = soup_list[0].find("span")
    print(res.text.split("$")[1].replace(",", ""))