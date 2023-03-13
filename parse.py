import requests
from bs4 import BeautifulSoup as Soup
import pandas as pd
import threading
from db import BotDB
from bot import bot

#bot = BotDB()

number_page = 86
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def parsers():
    #threading.Timer(3600.0, parsers).start()
    page = 1
    data_mas = []
    res = []
    while True:
        response_gippo = requests.get('https://codeforces.com/problemset/page/' + str(page) + '?order=BY_SOLVED_DESC',headers=headers)
        soup = Soup(response_gippo.content, 'html.parser')


        table = soup.find('table')
        table_rows = table.find_all('tr')

        
        if (page > number_page):
            break

        else:
            for tr in table_rows:
                td = tr.find_all('td')
                row = [tr.text.strip() for tr in td if tr.text.strip()]
                if row:
                    res.append(row)
                    
            page += 1

    df = pd.DataFrame(res)
    #print(df)
        #for row in df.iloc:
        #for i in range(len(df)):

    for i in range(0, len(df) - 1):
        tasks_data = []
        for k in df.loc[i]:
            str(k).split()
            tasks_data.append(k)
            data_mas.append(tasks_data)

    print(data_mas[1])
    for tasks in data_mas:
        if bot.tasks_exists(str(tasks[0])):
            print('Tasks yes')
            continue
        else:
            print('Tasks not')
            bot.add_data_tasks(tasks[0], tasks[2], tasks[1], tasks[3])


if __name__ == "__main__":
    parsers()