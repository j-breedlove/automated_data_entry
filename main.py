import requests
from bs4 import BeautifulSoup

from form_filler import FormFiller

# Constants
ZILLOW_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C...'
ZILLOW_PREPEND = 'https://www.zillow.com'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9"
}


def scrape_zillow():
    """
    Scrapes rental listings from Zillow and returns their addresses, prices, and links.

    Returns:
    - tuple: Three lists containing the addresses, prices, and links of the listings, respectively.
    """
    try:
        response = requests.get(ZILLOW_URL, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract addresses
        address_tags = soup.find_all('address')
        addresses = [listing.text for listing in address_tags]

        # Extract links
        link_tags = soup.find_all('a', class_='property-card-link')
        links = [ZILLOW_PREPEND + listing.get('href') for listing in link_tags]

        # Extract prices
        price_tags = soup.select('[data-test="property-card-price"]')
        prices = [price.text.split("+")[0].replace('/mo', '') for price in price_tags]

        return addresses, prices, links
    except requests.RequestException as e:
        print(f"Error during scraping: {e}")
        return [], [], []


def main():
    """Main function to initiate the scraping process and fill the form with the scraped data."""
    addresses, prices, links = scrape_zillow()
    form_filler = FormFiller()
    for address, price, link in zip(addresses, prices, links):
        form_filler.fill_form(address, price, link)


if __name__ == "__main__":
    main()
