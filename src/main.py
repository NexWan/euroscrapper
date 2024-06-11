import platform as plat
from Scrapper import *
from colors import *

def printWelcome():
    logo = """                              
                                          #@@@@#*++%@#"
                                     #@-................:%%
                                   +.........................-
                                 ................................
                               *...................................
             +      ................................................
           +.:.. -....................................................
          =.:.#+.......................................................
   ..:=+*@:.:%........#..................................................
-.       -:-+.........%:..................................................
        +:::@.........@.....=..............................................
        -.:.#%%@@@@%=.@...-%@@@@@@@*.........................................
        ++@..=@@@@@=..@.....@@@@@@.............................................#
        @....#@@@@@+..:.....@@@@@@...............................................@
      =#......:+*#.................................................................@%
      @...............................................................................%@
      @...................................................................................%#
       @...........................................................................................:
         *=................................................:=#%#=.+-.:+*#*%@@%@@##+:
              +%*=-:::::.....:=-:::::----=+#%@@@#%##%%+ """
    print(f"{colors.pink_color}{logo}{colors.reset_color}" + f"\n\n\n\n{colors.green_color}{('Welcome to euroScrapper!').center(100)}{colors.reset_color}")
    
    
def printMenu():
    print(f"""
    1. Scrape a site
    2. Exit
    """)
    choice = input("Enter your choice: ")
    return choice
  
def checkSite(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        print("Invalid url, please enter a valid url")
        return False
    if "eurogamer.net/games" not in url:
        print("Invalid url, please enter a valid eurogamer url" + 
              " (e.g. https://www.eurogamer.net/games/something....)")
        return False
    return True

def manageExit():
    Scrapper("").deleteFile()
    print("Exiting...")
    exit(0)
    
    
if __name__ == '__main__':
    if(plat.system() == 'Windows'):
        print(f"You should run this using linux or macos, you can use WSL as {plat.system()} is not yet supported")
        exit(1)
    printWelcome()
    while True:
        choice = printMenu()
        if choice == '1':
            url = input("Enter the url to scrape: ")
            if not checkSite(url):
                continue
            scrapper = Scrapper(url)
            scrapper.curlSite()
        elif choice == '2':
            manageExit()
            break
        else:
            print("Invalid choice")