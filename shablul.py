import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

months_map = {
    "ינואר": "January", "פברואר": "February", "מרץ": "March", "אפריל": "April",
    "מאי": "May", "יוני": "June", "יולי": "July", "אוגוסט": "August",
    "ספטמבר": "September", "אוקטובר": "October", "נובמבר": "November", "דצמבר": "December"
}

url = "https://shablul.smarticket.co.il/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

events = []

for show_num, event in enumerate(soup.find_all('div', class_='show_cube col-lg-4 col-sm-6 col-xs-12'), 0):
    title = event.find('div', id=f'show_name_{show_num}').get_text(strip=True)
    if title == 'הירשמו לעדכונים':
        continue
    date = event.find('div', class_='show_date').get_text(strip=True)
    hour = event.find('div', class_='show_time').get_text(strip=True)
    date = date + ' ' + hour
    date = date.replace(' בשעה', '')
    _, date = date.split(', ', 1)
    for hebrew, english in months_map.items():
        date = date.replace(hebrew, english)
    date = datetime.strptime(date, '%d %B %Y %H:%M')
    description = event.find('div', class_='brief')
    if description:
        description = description.get_text(strip=True)
    link = event.find('a').get('href')
    link = 'https://shablul.smarticket.co.il/' + link
    img = event.find('div', class_='pic img-rounded').find('img').get('data-src')
    img = 'https://shablul.smarticket.co.il/' + img
    events.append({'title':title, 'date':date, 'description':description, 'link':link, 'img':img})

events = pd.DataFrame(events)