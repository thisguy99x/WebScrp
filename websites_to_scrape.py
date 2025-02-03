import webbrowser
from scrape_and_select import scrape_product_info
import csv
import pandas as pd
import os

# Define a list of websites to scrape
urls = [
    'https://www.popflexactive.com/products/pirouette-skort-tutu-pink',
    'https://www.popflexactive.com/products/pirouette-skort-buttercream',
    'https://www.popflexactive.com/products/corset-pirouette-dress-ivory',
    'https://www.popflexactive.com/products/corset-pirouette-dress-black',
    'https://thehalara.com/products/adjustable-strap-button-multiple-pockets-plicated-waffle-casual-overalls?pmui=10.1.collection.list.1.jumpsuit&pmuih=jumpsuit&variant=44668209266854',
    'https://anua.us/products/heartleaf-quercetinol-pore-deep-cleansing-foam',
    'https://anua.us/products/heartleaf-70-daily-lotion-copy-1',
]

product_data = scrape_product_info(urls)

# Creates a .csv file with the scraped data and inserts it into the temp folder
with open("temp/product_data.csv", "w" , newline="") as file:
    writer = csv.writer(file)
    
    # Create and write headers
    header = ["Product", "Price"]
    writer.writerow(header)

    # Write the data rows
    for row in product_data[0:]:
        writer.writerows(product_data)

# Checks for duplicates and opens the file with the most recent data
old = pd.read_csv("temp/product_data.csv")
new = old.drop_duplicates()
new.to_csv("new_product_data.csv",index=False, )

os.remove("temp/product_data.csv")

