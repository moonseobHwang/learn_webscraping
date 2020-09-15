from bs4 import BeautifulSoup

source_html = '<html><head></head><body>Sacr&eacute; bleu!</body></html>'
soup = BeautifulSoup(markup=source_html)			# ignore waring
print(type(soup), soup)