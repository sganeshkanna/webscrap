from bs4 import BeautifulSoup
import requests
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
def parse_courses(url_):
    req = requests.get(url_,headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    # divs = soup.find("div", class_="cardBlkInn pull-left")
    courses_list = []
    head_links = soup.find_all('h2')
    for n in head_links:
       for a in n.find_all('a', href=True):
           courses_list.append(a.contents[0].strip())

    return courses_list
