from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://m.newegg.com/subcategories/48/desktop-graphics-cards/?depa=1'

#Opening up connection, grabing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()



#html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product

containers = page_soup.findAll("div", {"class":"item-container"})

#create a csv that will store the scraped data neatly

filename = "products.csv"
f = open(filename, "w")
#headers =  "product_name, price, shipping\n"

headers =  "product_name, shipping\n"

f.write(headers)
#loop through each container
for container in containers:
    
    title_container = container.findAll("a", {"class":"item-title"})
    #grab name of the product
    product_name = title_container[0].text
    
    shipping_container = container.findAll("li", {"class":"price-ship"})
    
    shipping = shipping_container[0].text.strip()
    
    print("product_name"+ product_name)
    print("shipping"+ shipping)    
    #price_dol =  container.findAll("li" ,{"strong":"strong"})

    #cent_price  = container.find("li" , {"sup":"sup"})
    #price =str(price_dol) + str(cent_price)
    
    #f.write(product_name.replace(",", "|") + ","+ price  + shipping + "\n")

    f.write(product_name.replace(",", "|") + ","  + shipping + "\n")
