from bs4 import BeautifulSoup
import requests

def scrape_product_info(urls):
  """
  Scrapes product name and price from given URLs.

  Args:
      urls: A list of URLs to scrape.

  Returns:
      A list of lists, where each inner list contains 
      [product_name, price] for each URL.
  """
  results = []
  for url in urls:
    try:
      response = requests.get(url)
      response.raise_for_status()  # Raise an exception for bad status codes
      soup = BeautifulSoup(response.text, 'html.parser')

      # Define website-specific selectors (example)
      if 'popflexactive.com' in url:
        product_name = soup.find('h1', class_='product-title').text.strip()
        price = soup.find('span', class_='price__current').text.strip()
      elif 'thehalara.com' in url:
        product_name = soup.find('h1', class_='index_N1_desc__pPriJ index_N1_descIsOp3__J5CG6').text.strip()
        price = soup.find('span', class_='index_N1_price__1aeXy undefined').text.strip()
      elif 'anua.us' in url:
        product_name = soup.find('h1', class_='product-title h2').text.strip()
        price_element = soup.find('sale-price') 
        price = price_element.text.strip() if price_element else "N/A" 
      elif 'ariembroiderystudio.com' in url:
        product_name = soup.find('h1').text.strip()
        price = soup.find('span', class_='price-item price-item--sale price-item--last').text.strip()
      else:
        product_name = "N/A"
        price = "N/A"

      results.append([product_name, price])
    except requests.exceptions.RequestException as e:
      print(f"Error fetching URL {url}: {e}")
      results.append([url, "Error"]) 
    except AttributeError:
      print(f"Error parsing data from URL {url}")
      results.append([url, "Parsing Error"])

  return results


