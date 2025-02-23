import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base URL of the website
BASE_URL = "http://books.toscrape.com/"

# Send a GET request to fetch the raw HTML content
response = requests.get(BASE_URL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all book containers
    books = soup.find_all('article', class_='product_pod')

    # List to store book details
    book_list = []

    # Loop through each book and extract details
    for book in books:
        try:
            # Get the book title
            title = book.find('h3').find('a')['title']

            # Get the book price
            price = book.find('p', class_='price_color').text.strip()

            # Get the book's relative link and convert it to an absolute URL
            relative_link = book.find('h3').find('a')['href']
            full_link = urljoin(BASE_URL, relative_link)

            # Store book details in a dictionary
            book_data = {
                "Title": title,
                "Price": price,
                "Link": full_link
            }

            book_list.append(book_data)

        except Exception as e:
            print(f"Error processing book: {e}")

    # Display the extracted book details
    for book in book_list:
        print(f"Title: {book['Title']}")
        print(f"Price: {book['Price']}")
        print(f"Link: {book['Link']}")
        print("-" * 50)

else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")
