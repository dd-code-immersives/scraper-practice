import csv
from bs4 import BeautifulSoup
import requests
import traceback
import os
# URL to the website
URL = 'http://quotes.toscrape.com/tableful' 
#/page/digit

# Getting the html file and parsing with html.parser
html = requests.get(URL)
bs = BeautifulSoup(html.text, 'html.parser')
page_counter =  1

# Tries to open the file
try:
    csv_file = open('quote_list.csv', 'w')
    fieldnames = ['quote', 'author', 'tags']
    dictwriter = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Writes the headers
    dictwriter.writeheader()

    # While next button is found in the page the loop runs
    while True:
        print(f"scraping page {page_counter}")
        # Loops through quote in the page
        all_rows = bs.find('table').find_all('tr')

        for index in range(1,len(all_rows) - 1, 2):

            quote_info = all_rows[index: index + 2]
            quote, author = quote_info[0].get_text().split('Author:') # this is the quote 

            #author = text[1]
            #quote =  text[0]
            tags  = [tag.get_text() for tag in quote_info[1].find_all('a')]
            # # Extract the text part of quote, author and tags
            # text = quote.find('span', {'class': 'text'}).text
            # author = quote.find('small', {'class': 'author'}).text
            # tags = []
            # for tag in quote.findAll('a', {'class': 'tag'}):
            #     tags.append(tag.text)
            # # Writes the current quote,author and tags to a csv file
            # dictwriter.writerow(
            #     {'quote': text, 'author': author, 'tags': tags})
            print("Tags:", tags)
            print("Quote:", quote)
            print("Author:",author)

        # Finds the link to next page
        #next_page_anchor = all_rows[-1].find_all('a')[-1]
        #if not next_page_anchor:
        #    break


        page_counter += 1
        # Gets and parses the html file of next page
        page_req = os.path.join(URL ,'page/') + str(page_counter)

        html = requests.get(page_req)
        if html.status_code == 200:
            bs = BeautifulSoup(html.text, 'html.parser')
        else:
            break
except:
    traceback.print_exc()
finally:
    csv_file.close()
