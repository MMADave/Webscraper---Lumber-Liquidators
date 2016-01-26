import sys
from bs4 import BeautifulSoup

with open(sys.argv[1]) as f:
    page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    product = soup.find_all(styleclass='strong')
    compare = soup.select('span[class="compareAT"]')
    sale = soup.select('span[class="sale"]')
    skus = soup.select('span[class="detail-sku"]')
    for i in range(0, len(sale)):
        print skus[i].getText().strip()[5:],
        print sale[i].getText()[10:-4],
        print compare[i].getText()[11:-4],
        print product[i].getText()