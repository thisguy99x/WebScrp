import webbrowser
from scrpr import scrape_product_info

urls = [
    'https://www.popflexactive.com/products/pirouette-skort-tutu-pink',
    'https://www.popflexactive.com/products/pirouette-skort-buttercream',
    'https://thehalara.com/products/adjustable-strap-button-multiple-pockets-plicated-waffle-casual-overalls?pmui=10.1.collection.list.1.jumpsuit&pmuih=jumpsuit&variant=44668209266854',
    'https://anua.us/products/heartleaf-quercetinol-pore-deep-cleansing-foam',
    'https://anua.us/products/heartleaf-70-daily-lotion-copy-1',
    'https://ariembroiderystudio.com/products/the-lakes-cardigan?currency=USD'
]

product_data = scrape_product_info(urls)

# Write results to an HTML file
with open("product_prices.html", "w") as f:
  f.write("<table>\n")
  for row in product_data:
    f.write("  <tr>\n")
    f.write(f"    <td>{row[0]}</td>\n")
    f.write(f"    <td>{row[1]}</td>\n")
    f.write("  </tr>\n")
  f.write("</table>\n")

# Open your separate HTML file (replace 'your_separate_file.html' with the actual filename)
webbrowser.open_new_tab('front_End.html') 

print("Product information written to product_prices.html")