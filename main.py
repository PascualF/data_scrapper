import requests #http library
from bs4 import BeautifulSoup as bs #parsing html
from pandas import DataFrame #make a table organized in dataframe for excel.

base_url = 'https://www.youthforum.org/'
url = 'https://www.youthforum.org/members'

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

    res = requests.get(url, headers=headers) #request from the url, main.
    print(res)
    soup = bs(res.text, 'html.parser')
    
    non_url = ['javascript:void(0);', 'https://www.youthforum.org/members/p2', 'https://www.youthforum.org/members/p3', 'https://www.youthforum.org/members/p7', 'https://www.youthforum.org/members/p4'
               ,'https://www.youthforum.org/members/p5', 'https://www.youthforum.org/members/p6', '#', 'https://www.youthforum.org/members']

    members_wrapper = soup.find(class_ = "flex flex-wrap -mx-3")
    
    a_tags = members_wrapper.find_all('a')
    
    for tag in a_tags:
        
        if tag['href'] not in non_url:
            url2 = tag['href']

            res2 = requests.get(url2, headers=headers) #request second url that changes for each entity.

            soup2 = bs(res2.content, 'html.parser') 

            #try:
            mail_div = soup2.find(class_ = "flex items-center mt-2")
            #except:
            #   mail_div = 'N/A'
            
            if mail_div is not None:
                mail_text = mail_div.find(class_ = "link")
            else:
                mail_text = 'N/A'
            print(mail_text)
            print('mail_text')
            if mail_text == 'N/A' :
                mail_to_text = 'N/A'
            else:
                mail_to_text = mail_text.get_text()

            description_text = soup2.find(class_ = "mt-12 redactor")
            
            

            mail_list.append(mail_to_text)

            description_list.append(description_text.text if description_text else "N/A")

    title_all = members_wrapper.find_all('a', class_="transition-colors duration-200 link--extended hover:text-primary hover:underline")

    type_all = members_wrapper.find_all('div', class_="mb-4 text-sm text-primary")
    

    for title in title_all:
        titles_list.append(title.get_text())

    for type in type_all:
        types_list.append(" ".join(type.get_text().split()))

    page += 1

df = DataFrame({'Title': titles_list, 'Type': types_list, 'E-mail': mail_list, 'Description': description_list})
df.to_excel('test.xlsx', sheet_name='sheet1', index=False)

print('Done')