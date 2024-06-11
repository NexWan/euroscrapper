# EuroScrapper

This is a simple webscrapper that uses curl and python to scrap some info about videogames in EuroGame!.  
This proyect was made because when I was coursing prolog I had to create a proyect with info about something of my interest, I choose videogames
and I didn't found any scrapper so I decided to create mine xd.

## THIS PROJECT IS STILL IN PROGRESS:
### TODO:
- ~~Curl the website into a html file.~~
- ~~Scrape the website.~~
- - ~~Get platforms~~
- - ~~Get Title~~
- - ~~Get release~~
- - ~~Get Genres~~
- - ~~Get Publishers~~
- - ~~Get Franchise~~
- Generate a JSON file 
- Generate e CSV file.

### NOTE FOR WINDOWS
I'm not entirely sure if this works in windows, it worked in windows 11 but idk about the rest lol

## How to install  


In order to install you need to do 
```sh
git clone https://github.com/NexWan/euroscrapper
```
Go into the src folder and do 
```sh
python main.py
```

You are going to need to install the following dependencie with pip:
```sh
pip install beautifulsoup4
```

### NOTE FOR ARCH
If you are using Arch Linux is most likely that you are going to need to create your own venv with python in order to run the program.
```sh
python3 -m venv env
```
Then activate it in your terminal
```sh
source env/bin/activate
```
And you should be able to use the pip install command
