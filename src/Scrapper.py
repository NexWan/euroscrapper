import subprocess as sp
import os
from bs4 import BeautifulSoup

class Scrapper:
    FILE_PATH = 'tmp/file.html'
    
    def __init__(self, url):
        self.url = url
        
    def getPlatforms(self, soup):
                # Find the <span> element with the text "Platforms"
        platform_span = soup.find('span', string="Platforms")
        
        # Find the next sibling <ul> of the <span> element
        if platform_span:
            platform_ul = platform_span.find_next_sibling('ul')
            if platform_ul:
                print("Found <ul> next to 'Platforms' <span>. Contents:")
                for li in platform_ul.find_all('li'):
                    print(li.text.strip())
            else:
                print("No <ul> found next to the 'Platforms' <span>")
        else:
            print("No <span> with the name 'Platforms' found")
        
    def scrapSite(self):
        print("Scraping the site")
        with open(self.FILE_PATH) as file:
            soup = BeautifulSoup(file, 'html.parser')
            self.getPlatforms(soup)
        
        
    def curlSite(self):
        print(f"Fetching {self.url}")
        if os.path.exists(self.FILE_PATH):
            print("Not done yet")
        if not os.path.exists("tmp"):
            sp.run(["mkdir","tmp"])
        with open(self.FILE_PATH, "w") as file:
            sp.run(["curl", self.url], stdout=file)
        if os.path.exists(self.FILE_PATH):
            print(f"File created at {self.FILE_PATH}")
        else:
            print("Failed to create file")
        self.scrapSite()