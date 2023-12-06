import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt

URL = 'https://steampay.com'
HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
# start
@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

#get data
@csrf_exempt
def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='catalog-item')
    games = []

    for item in items:
        games.append({
            "title_name": item.find("div", class_='catalog-item__name').get_text(),
        })

    return games



# endparser
@csrf_exempt
def parser_games():
    html = get_html(URL)
    if html.status_code == 200:
        games2 = []
        for page in range(0, 1):
            html = get_html(f'https://steampay.com/action', params=page)
            games2.extend(get_data(html.text))
        #return games2
        print(games2)

    else:
        raise Exception('Error in Parse')


parser_games()