import requests #http library
from bs4 import BeautifulSoup as bs #parsing html
from pandas import DataFrame #make a table organized in dataframe for excel.

base_url = 'https://www.youthforum.org/'
url = 'https://www.youthforum.org/members'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

res = requests.get(url, headers=headers) #request from the url.
print(res)

soup = bs(res.text, 'html.parser')

members_wrapper = soup.find(class_ = "w-full px-3 md:w-2/3 js-filter-results")

title_all = members_wrapper.find_all('a', class_="transition-colors duration-200 link--extended hover:text-primary hover:underline")
site_ref = members_wrapper.find_all('href', class_="transition-colors duration-200 link--extended hover:text-primary hover:underline")
titles_list = []
type_all = members_wrapper.find_all('div', class_="mb-4 text-sm text-primary")
types_list = []

for title in title_all:
    titles_list.append(title.get_text())
    #print(title.get_text())

for type in type_all:
    types_list.append(type.get_text())

print('Start')
print(site_ref)
print('End')


df = DataFrame({'Title': titles_list, 'Type': types_list})
df.to_excel('test.xlsx', sheet_name='sheet1', index=False)