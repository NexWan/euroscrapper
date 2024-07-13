import subprocess as sp
import os
from bs4 import BeautifulSoup
import json

class Scrapper:
    FILE_PATH = 'tmp/file.html'
    
    def __init__(self, url, multi=False):
        self.url = url
        self.multi = multi
        
    def deleteFile(self):
        if os.path.exists(self.FILE_PATH):
            os.remove(self.FILE_PATH)
            print(f"Deleted {self.FILE_PATH}")
            
    def getTitle(self, soup):
        # Find the h1 title
        title = soup.find('h1', class_="page_title")
        if title:
            return title.text.strip()
            
    def getFranchise(self, span):
        # Find the <span> element with the text "Franchise"
        franchise_span = span.find('span', string="Franchise")
        # Find the next sibling <a> of the <span> element
        if franchise_span:
            franchise_a = franchise_span.find_next_sibling('a')
            if franchise_a:
                print("Found <a> next to 'Franchise' <span>. Contents:")
                return franchise_a.text.strip()
            else:
                print("No <a> found next to the 'Franchise' <span>")
        else:
            print("No <span> with the name 'Franchise' found")
            
    def getPublishers(self, soup):
        list = []
        # Find the <span> element with the text "Publishers"
        publisher_span = soup.find('span', string="Publishers")
        # Find the next sibling <ul> of the <span> element
        if publisher_span:
            publisher_ul = publisher_span.find_next_sibling('ul')
            if publisher_ul:
                print("Found <ul> next to 'Publishers' <span>. Contents:")
                for li in publisher_ul.find_all('li'):
                    list.append(li.text.strip())
                return list
            else:
                print("No <ul> found next to the 'Publishers' <span>")
        else:
            print("No <span> with the name 'Publishers' found")
            
    def getGenres(self,soup):
        list = []
        # Find the <span> element with the text "Genres"
        genre_span = soup.find('span', string="Genres")
        # Find the next sibling <ul> of the <span> element
        if genre_span:
            genre_ul = genre_span.find_next_sibling('ul')
            if genre_ul:
                print("Found <ul> next to 'Genres' <span>. Contents:")
                for li in genre_ul.find_all('li'):
                    list.append(li.text.strip())
                return list
            else:
                print("No <ul> found next to the 'Genres' <span>")
        else:
            print("No <span> with the name 'Genres' found")
            
    def getRelease(self, soup):
        # Find the <span> element with the text "Release Date"
        release_span = soup.find('span', string="Initial release")
        # Find the next sibling <time> of the <span> element
        if release_span:
            release_time = release_span.find_next_sibling()
            if release_time:
                print("Found time value next to 'Release Date' <span>. Contents:")
                return release_time.text.strip()
            else:
                print("No <time> found next to the 'Release Date' <span>")
        else:
            print("No <span> with the name 'Release Date' found")
        
    def getPlatforms(self, soup):
        list = []
        # Find the <span> element with the text "Platforms"
        platform_span = soup.find('span', string="Platforms")
        # Find the next sibling <ul> of the <span> element
        if platform_span:
            platform_ul = platform_span.find_next_sibling('ul')
            if platform_ul:
                print("Found <ul> next to 'Platforms' <span>. Contents:")
                for li in platform_ul.find_all('li'):
                    list.append(li.text.strip())
                return list
            else:
                print("No <ul> found next to the 'Platforms' <span>")
        else:
            print("No <span> with the name 'Platforms' found")
        
    def scrapSite(self):
        print("Scraping the site")
        with open(self.FILE_PATH) as file:
            soup = BeautifulSoup(file, 'html.parser')
            title = self.getTitle(soup)
            platforms = self.getPlatforms(soup)
            release = self.getRelease(soup)
            genres = self.getGenres(soup)
            publishers = self.getPublishers(soup)
            franchise = self.getFranchise(soup)
            self.writeToJson(title, platforms, release, genres, publishers, franchise)
        
    
    def writeToJson(self, title, platforms, release, genres, publishers, franchise):
        file_path = "tmp/data.json"
        game_data = {'title': title, 'content': {"platforms": platforms, "release": release, "genres": genres, "publishers": publishers, "franchise": franchise}}
        
        # Check if the file exists and is not empty
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r+', encoding='utf-8') as file:
                data = json.load(file)
                # Append the new game data to the 'games' array
                data['games'].append(game_data)
                # Move the file pointer to the beginning of the file
                file.seek(0)
                # Write the updated JSON data
                json.dump(data, file, indent=4)
                # Truncate the file to the new size
                file.truncate()
        else:
            # If the file doesn't exist or is empty, create a new structure
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump({'games': [game_data]}, file, indent=4)
    
        print(f"Data of game {title} saved to {file_path}")

    def deleteJson(self):
        if os.path.exists("tmp/data.json"):
            os.remove("tmp/data.json")
            print("Deleted tmp/data.json")

    def initialCheck(self):
        if(os.path.exists("tmp/data.json")):
            print("Data file already exists, do you want to overwrite it? (y/n)")
            choice = input()
            if choice == "y":
                self.deleteJson()
                json.dump({'games': []}, open("tmp/data.json", "w"), indent=4)
            else:
                print("Exiting...")
                exit(0)
        
    def curlSite(self):
        print(f"Fetching {self.url}")
        if os.path.exists(self.FILE_PATH):
            print("Not done yet")
        if not os.path.exists("tmp"):
            os.makedirs("tmp")
        with open(self.FILE_PATH, "w") as file:
            sp.run(["curl", self.url], stdout=file)
        if os.path.exists(self.FILE_PATH):
            print(f"File created at {self.FILE_PATH}")
        else:
            print("Failed to create file")
        self.scrapSite()