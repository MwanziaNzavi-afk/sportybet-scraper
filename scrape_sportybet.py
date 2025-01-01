import requests
from bs4 import BeautifulSoup
import os

# Step 1: Send a GET request to the website
url = 'https://www.sportybet.co.ke'  # Corrected the URL
headers = {  # Fixed headers variable name to match
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

# Create a folder to store data
output_folder = 'Scraped_data'
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Check if request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Find all the links on the page
    links = soup.find_all('a')

    # Step 3: Write the links to a text file
    output_file = os.path.join(output_folder, 'scraped_links.txt')
    with open(output_file, 'w', encoding='utf-8') as file:
        for link in links:
            href = link.get('href')  # Corrected the access method for href
            if href:
                file.write(f'Link: {href}\n')

    print(f"Scraped links have been saved to {output_file}")
else:
    print('Failed to retrieve the webpage')  # Moved this outside the loop
