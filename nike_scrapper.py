import requests
from bs4 import BeautifulSoup

# Replace the URL with the website that you want to scrape
url = 'https://www.consumeraffairs.com/sporting_goods/nike.html?#sort=recent&filter=5'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the review containers
reviews = soup.find_all('div', class_='review-container')

# Iterate through the reviews and extract the review text and rating
for review in reviews:
    text = review.find('p', class_='review-text').get_text()
    rating = review.find('div', class_='rating').get('aria-label')
    
    # Print the review text and rating
    print('Review text:', text)
    print('Rating:', rating)
