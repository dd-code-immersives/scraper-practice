import pytest 
from quote_scraper import * 
from pathlib import Path


def test_html_source_exists(page_html):

	assert page_html != None 

def test_div_class_quotes_exists(page_html):
	quote_divs = page_html.find_all('div', {'class': 'quote'})
	assert len(quote_divs) > 0

def test_url_request(page_request):
	assert page_request.status_code == 200

def test_file_path_valid():
	path_to_file = "quote_list.csv"
	path = Path(path_to_file)
	assert path.is_file()

def test_make_request():

	assert True 


def test_pagination(page_html):
	# find the link to the next page
	next_page = page_html.find('li', {'class': 'next'})
	assert next_page != None 