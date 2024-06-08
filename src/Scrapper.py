import subprocess as sp
import os

class Scrapper:
    FILE_PATH = 'tmp/file.html'
    
    def __init__(self, url):
        self.url = url
        
    def curlSite(self):
        global FILE_PATH
        if os.path.exists(FILE_PATH):
            
        sp.run(["mkdir","tmp"])
        sp.run(["curl", f"{self.url}", ">", "tmp/page.txt"])
        