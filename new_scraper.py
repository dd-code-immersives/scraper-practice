"""
run interactively with python3 -i new_scraper.py to 
play around with the code
"""
from bs4 import BeautifulSoup
import requests

URL = 'https://stackoverflow.com/questions/'

res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')