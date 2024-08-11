import requests #http library
from bs4 import BeautifulSoup as bs #parsing html
from pandas import DataFrame #make a table organized in dataframe for excel.

base_url = 'https://www.youthforum.org/'
url = 'https://www.youthforum.org/members'
url2 = ''

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

page = 1
titles_list = []
types_list = []
mail_list = []
description_list = []

while page <= 7:
    url = 'https://www.youthforum.org/members'
    if url == 1:
        url = url
    elif url != 1:
        url = url + '/p' + str(page)

    res = requests.get(url, headers=headers) #request from the url.
    
    soup = bs(res.text, 'html.parser')
    
    

    members_wrapper = soup.find(class_ = "w-full px-3 md:w-2/3 js-filter-results")
    a_tags = members_wrapper.find_all('a')
    for tag in a_tags:
        print(tag['href'])

    title_all = members_wrapper.find_all('a', class_="transition-colors duration-200 link--extended hover:text-primary hover:underline")

    type_all = members_wrapper.find_all('div', class_="mb-4 text-sm text-primary")
    

    for title in title_all:
        titles_list.append(title.get_text())

    for type in type_all:
        types_list.append(" ".join(type.get_text().split()))

    page += 1

df = DataFrame({'Title': titles_list, 'Type': types_list})
df.to_excel('test.xlsx', sheet_name='sheet1', index=False)

print('Done')