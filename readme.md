# EuroScrapper

This is a simple webscrapper that uses curl and python to scrap some info about videogames in EuroGame!.  
This proyect was made because when I was coursing prolog I had to create a proyect with info about something of my interest, I choose videogames
and I didn't found any scrapper so I decided to create mine xd.

## How to use  
The program is pretty straight foward, you need to first make sure you have all installed (look a bit down on this readme to see how to install it properly), then you just do  

```sh
python src/main.py
```  
you'll be greeted by the welcome message, you'll have 3 options:
1. Scrape a single site
2. Scrape multiple sites
3. Exit.    

The first option you can just scrape one site and will overwrite each time, with the second option you'll have to provide mutliple links in each line, you can stop just writting ('done'), the third option will simply exit the program and delete the result of curling the websites.  
<b>Make sure you exit by the third option, since if you stop it by using ctrl c or closing your terminal the temp files will not get deleted!</b>

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
- ~~Generate a JSON file~~
- Generate e CSV file.
- ~~Add the option to do it with multiple links.~~

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


### DEMO   

<img src="https://i.imgur.com/E7gIkyf.gif">
