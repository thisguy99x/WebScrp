from bs4 import BeautifulSoup
import requests
import time

st = time.time()
# URLs to scrape and convert data to text 
pink_skort = requests.get('https://www.popflexactive.com/products/pirouette-skort-tutu-pink').text,
buttercream_skort = requests.get('https://www.popflexactive.com/products/pirouette-skort-buttercream').text,
overalls = requests.get('https://thehalara.com/products/adjustable-strap-button-multiple-pockets-plicated-waffle-casual-overalls?pmui=10.1.collection.list.1.jumpsuit&pmuih=jumpsuit&variant=44668209266854').text,
anua_cleanse = requests.get('https://anua.us/products/heartleaf-quercetinol-pore-deep-cleansing-foam').text,
anua_lotion = requests.get('https://anua.us/products/heartleaf-70-daily-lotion-copy-1').text,
lakes_cardigan = requests.get('https://ariembroiderystudio.com/products/the-lakes-cardigan?currency=USD').text

# Each new URL needs a block like these

pink_skort_soup = BeautifulSoup(str(pink_skort), 'lxml')
pink_skort_product = pink_skort_soup.find('h1', class_='product-title', ).text.replace('/n','')
pink_skort_proice = pink_skort_soup.find('span', class_='price__current').text.replace('/n','')

buttercream_skort_soup = BeautifulSoup(str(buttercream_skort), 'lxml')
buttercream_skort_product = buttercream_skort_soup.find('h1', class_='product-title', ).text.replace('/n','')
buttercream_skort_proice = buttercream_skort_soup.find('span', class_='price__current').text.replace('/n','')

overalls_soup = BeautifulSoup(str(overalls), 'lxml')
overalls_product = overalls_soup.find('h1', class_='index_N1_desc__pPriJ index_N1_descIsOp3__J5CG6').text.replace('/n','')
overalls_proice = overalls_soup.find('span', class_='index_N1_price__1aeXy undefined').text.replace('/n','')

anua_cleanse_soup = BeautifulSoup(str(anua_cleanse), 'lxml')
anua_cleanse_product = anua_cleanse_soup.find('h1', class_='product-title h2').text.replace('/n','')
anua_cleanse_proice = anua_cleanse_soup.find('sale-price',
                                             form="product-form-8257208975638-template--22447971434774__main").text.replace('/n','')

anua_lotion_soup = BeautifulSoup(str(anua_lotion), 'lxml')
anua_lotion_product = anua_lotion_soup.find('h1', class_='product-title h2').text.replace('/n','')
anua_lotion_proice = anua_lotion_soup.find('sale-price',
                                           form="product-form-9780587561238-template--22297173295382__main").text.replace('/n','')

lakes_cardigan_soup = BeautifulSoup(str(lakes_cardigan), 'lxml')
lakes_cardigan_product = lakes_cardigan_soup.find('h1').text.replace('/n','')
lakes_cardigan_proice = lakes_cardigan_soup.find('span',
                                                 class_="price-item price-item--sale price-item--last").text.replace('/n','')

# Stores the outputs to variables
pink_skort_result = (f"The price of {pink_skort_product} is: {pink_skort_proice}\n")
buttercream_skort_result = (f"The price of {buttercream_skort_product} is: {buttercream_skort_proice}\n")
overalls_result = (f"The price of {overalls_product} is: {overalls_proice}\n")
anua_cleanse_result = (f"The price of {anua_cleanse_product} is: {anua_cleanse_proice}\n")
anua_lotion_result = (f"The price of {anua_lotion_product} is: {anua_lotion_proice}\n")
lakes_cardigan_result = (f"The price of {lakes_cardigan_product} is:  {lakes_cardigan_proice}\n")

# Writing to an existing file (content will be overwritten)
with open("product_prices.txt", "w") as f:
    f.write(pink_skort_result)
    f.write(buttercream_skort_result)
    f.write(overalls_result)
    f.write(anua_cleanse_result)
    f.write(anua_lotion_result)
    f.write(lakes_cardigan_result)

et = time.time()
time_result = et - st
print(f"Wrote file successfully! Took {time_result} seconds")