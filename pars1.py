import requests 
from bs4 import BeautifulSoup as bs
import csv

def write_to_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['image']])

def get_html(url):
    response = requests.get(url)
    return response.text
# # ls = []
# def get_total_pages(html):
#     soup = bs(html, 'lxml')
#     pages_list = soup.find('div', class_ = 'vm-pagination vm-pagination-bottom').find_all('li')[-3]
#     list_ = pages_list.find('a').get('href')
    
    # last_pages = pages_list.find_all('a')

   



def get_data(html):
    soup = bs(html, 'lxml')
    notebooks_list = soup.find_all('div', class_='product vm-col vm-col-1')

    for notebook in notebooks_list:
        try:
            title = notebook.find('span', class_='prouct_name').find('a').text
        except:
            title = ''
        
        try:
            price = notebook.find('span', class_='price').text
        except: 
            price = ''
        
        try:
            image = 'https://enter.kg' + notebook.find('img').get('src')
        except:
            image = ''    

        dict_notebook = {'title': title, 'price': price, 'image': image}
        write_to_csv(dict_notebook)

def main():
    url = 'https://enter.kg/computers/noutbuki_bishkek'
    html = get_html(url)
    get_data(html)
    # get_total_pages(html)


    list_ = []
    for i in list_:
        url_ = 'https://enter.kg' + i
        html = get_html(url_)
        get_data(html)



    

   

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'price', 'image'])

main()
