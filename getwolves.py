# Imports 
import requests
from bs4 import BeautifulSoup as bs

import os

#URL that images are scraped from

url = ('https://pixabay.com/en/photos/?q=wolf&hp=&image_type=all&order=&cat=&min_width=&min_height=')

#Gets the URL and parses the code into html
page = requests.get(url)
soup = bs(page.text, 'html.parser')

#Looks for the 'img' tag in the html code 
image_tags = soup.findAll('img')

# Looks for a folder in the directory named 'wolves'
# If there isn't one, it creates it
if not os.path.exists('wolves'):
    os.makedirs('wolves')

# Moves to the folder 
os.chdir('wolves')

x = 0

#For every image in the code, it will save the images into the folder

x = 0

for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('wolf-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
