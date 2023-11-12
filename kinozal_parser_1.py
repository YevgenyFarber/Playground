import requests
from bs4 import BeautifulSoup
movies = []


url = 'https://kinozal.tv/browse.php?s=%C4%E6%EE%ED+%D3%E8%EA+4&g=0&c=0&v=0&d=0&w=0&t=0&f=0'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
items = []

# Assuming each item is in a div with a specific class (replace with actual tag and class)
for item_html in soup.find_all('div', class_='bx2_0')[3]:
    # Extracting title (replace with actual tag or structure)
    title = item_html.find('tag_for_title').text.strip()

    # Extracting other attributes similarly
    # size = item_html.find('tag_for_size').text.strip()
    # ...

    # Create a dictionary for each item
    item_data = {
        'title': title,
        # 'size': size,
        # ...
    }

    # Add the item's data to the list
    items.append(item_data)
# Extracting specific details
