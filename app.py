import requests
from bs4 import BeautifulSoup
import csv

def main():
    search = input("Search: ")
    page = input("Max Page: ")
    
    with open("results.csv", "w") as fp:
        writer = csv.writer(fp)
        # Menulis header
        writer.writerow(['Nama Produk', 'Harga Produk', 'Produk Terjual'])

        for x in range(int(page)):
            URL = "https://www.tokopedia.com/search?navsource=&page=" + str(x) + "&&q=" + search 

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0'
            }

            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser') 

            elements = soup.find_all(class_='css-5wh65g')
            
            for element in elements:
                product_name = element.find('span', class_='OWkG6oHwAppMn1hIBsC3pQ==')
                if product_name:
                    product_name = product_name.text
                    print(f"Nama Produk: {product_name}")

                product_price = element.find('div', class_='_8cR53N0JqdRc+mQCckhS0g==')
                if product_price:
                    product_price = product_price.text
                    print(f"Harga Produk: {product_price}")
                
                product_sold = element.find('span', class_='eLOomHl6J3IWAcdRU8M08A==')
                if product_sold:
                    product_sold = product_sold.text
                    print(f"Produk Terjual : {product_sold}")

                if (product_name and product_price and product_sold):
                    writer.writerow([product_name, product_price, product_sold])
    pass

if __name__ == "__main__":
    main()