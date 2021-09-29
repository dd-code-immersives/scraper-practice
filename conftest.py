import pytest 
from quote_scraper import * 

@pytest.fixture
def page_request():
	req = requests.get(URL)
	return req

@pytest.fixture
def page_html(page_request):
	bs = BeautifulSoup(page_request.content, 'html.parser')
	return bs