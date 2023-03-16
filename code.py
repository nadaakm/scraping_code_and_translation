from bs4 import BeautifulSoup
from bs4.formatter import HTMLFormatter
from googletrans import Translator
import requests
import random
import webbrowser
import io
import re
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]




# URL of the website to be scraped
url = 'https://www.classcentral.com/'

# Send a request to the website and get its HTML content
response = requests.get(url,headers={'User-Agent': random.choice(user_agents_list)})

html_content = response.text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')
##text = soup.get_text()
##print (text)

# translate content
translator = Translator()
texte=soup.get_text()
for element in texte:
     texte=soup.find_all(string=True)
     text = soup.get_text(strip=True)
     if not text:
        continue
text = re.sub(r'[\n\r]+', ' ', text)
text = re.sub(r'\s{2,}', ' ', text)
translated = translator.translate(text, dest='hi').text

soup.body.string = translated
##print(translated)
with open('translated.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))


##print(soup)

### relace the contennt with the translated one 
##texts = text.replace(html_content,translated)
##print(texts)

# Find all the links on the page
links = soup.find_all('a')

# Loop through each link and extract its URL
for link in links:
    href = link.get('href')
  

    # Check if the URL is valid
    if href.startswith('http'):

        # Send a request to the linked website and get its HTML content
        sub_response = requests.get(href)
        sub_html_content = sub_response.text

        # Create a BeautifulSoup object to parse the linked website's HTML content
        sub_soup = BeautifulSoup(sub_html_content, 'html.parser')
        
        #texte1=sub_soup.get_text()
        #for element in texte1:
         ## texte1=sub_soup.find_all(string=True)
          ##text = soup.get_text(strip=True)
          ##if not text:
          ## continue
          
translated1 = translator.translate(text, dest="hi").text

##textss = text.replace(sub_html_content,translated1)

        # Extract any information you need from the sub_soup object
        

    
##with open("fichier_traduit.html", "w") as file:
    ##f.write(soup.prettify().replace(soup.get_text(), b))
    

webbrowser.open('translated.html')
     
