from bs4 import BeautifulSoup
import requests

# Define the headers to avoid being blocked by the website
headers = {'user-agent': 'my-app/0.0.1'}

# Send a GET request to the website
html = requests.get("https://flatiron.com/", headers=headers)

# Parse the HTML content using BeautifulSoup
doc = BeautifulSoup(html.text, 'html.parser')

# Print the HTML content to inspect the structure
print(doc.prettify())  # This will print the whole HTML structure

# Try to select the header with the class 'heading-financier'
heading = doc.select('.heading-financier')

# Check if any elements were found
if heading:
    # Extract the text content from the element and remove extra whitespace
    text = heading[0].contents[0].strip()
    print(text)
else:
    print("No elements with class 'heading-financier' found.")
    
# Optional: If you want to check for different heading tags (h1, h2, h3), you can try this:
headings = doc.find_all('[h1', 'h2', 'h3]')
print(headings)  # This will print all headings found on the page
