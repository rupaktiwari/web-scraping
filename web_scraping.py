from bs4 import BeautifulSoup

# Define a function to parse the saved HTML file
def parseHTMLFile(filePath):
    with open(filePath, "r") as f:
        html_content = f.read()

    # Create a Beautiful Soup object to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")  # You can use "lxml" or "html5lib" as well

    # Now you can use Beautiful Soup to extract data from the HTML
    # For example, let's find all the links on the page
    links = soup.find_all("a")
    for link in links:
        print("Link Text:", link.text)
        print("Link URL:", link.get("href"))

# Call the parseHTMLFile function to parse the saved HTML file
parseHTMLFile("data/movies.html")
