import requests
from bs4 import BeautifulSoup as soup
import os


def download(url1, filename):
    if os.path.exists(filename):
        print('file existed!')
        return
    try:
        headers = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url1, headers=headers, timeout=(3.05, 27))
        print(f"Pokemondb's Response: {r.status_code}")
        with open(filename, 'wb') as f:
            f.write(r.content)
    except Exception:
        print("There may have problem!!!")


def download2(url2):
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url2, headers=headers, timeout=(3.05, 27)).content
    temp = []
    picList = soup(response, "html.parser")
    for idx, val in enumerate(picList.find_all('img')):
        print(f"Now adding {idx+1}_th item to the list\n")
        temp.append(val['src'])
    temp.append(picList.find_all('a', {"rel": "lightbox"})[-1]['href'])
    for j in range(len(temp)):
        filename = os.path.join('PokePic', f"{url2.split('/')[-1]}_{j+1}.png")
        print(f"Now downloading {url2.split('/')[-1]}_{j+1}\n")
        download(temp[j], filename)


if os.path.isdir('PokePic') is False:
    os.mkdir('PokePic')


if __name__ == '__main__':
    url = 'https://pokemondb.net/pokedex/national'
    headers = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers).content
    soup_page = soup(r, "html.parser")
    pokelist = soup_page.find_all("a", {"class": "ent-name"})
    print(f"Total number of Pokemon is {len(pokelist)}\n")
    for i in range(len(pokelist)):
        print(f"Now download {pokelist[i].text}\n")
        target_url = "https://pokemondb.net/artwork/"+pokelist[i]['href'].split('/')[-1]
        download2(target_url)
