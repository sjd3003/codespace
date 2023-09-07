from bs4 import BeautifulSoup

# Specify the path to your local HTML file
file_path = 'C:\\Users\\sh\\Documents\\VeriFone\\SRNTemp\\radBA089.tmp_PLU.html'
# OR
file_path = r'C:\Users\sh\Documents\VeriFone\SRNTemp\radBA089.tmp_PLU.html'


# Open and read the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Now, you can extract data from the parsed HTML using BeautifulSoup methods
# For example, to extract and print the title of the HTML page:
title = soup.title.string
print(f'Title: {title}')

# You can also extract other elements, attributes, or text as needed
