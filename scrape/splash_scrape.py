# import libraries

from bs4 import BeautifulSoup,Comment
import requests
import pickle



BASE ='https://www.basketball-reference.com'
START ='https://www.basketball-reference.com/players/'
YEAR = 2020

# import custom classes
from Game import *
from Season import *
from Player import *
from Metadata import *

def Save(lst):
    '''
    Parameters: a list of player objects
    Returns: none
    Purpose: saves the list of player objects to a pickle file
    '''

    output_file = open('splash.spl','wb')
    pickle.dump(lst,output_file)
    output_file.close()
    print("Saved!")
def validate(dict):
    for i in dict.keys():
        try:
            if len(dict[i]) == 0 or len(dict[i]) == " " or len(dict[i]) == "":
                dict[i] = 0
        except TypeError:
            pass
def getAlphabet(html_temp):
    '''
    Parameters: html template
    Returns: a list of links as strings
    Purpose: Find all links on the page, and put them into a list
    '''
    all_links = html_temp.find_all('a')
    alphabet_links = []
    #For each link in the list of all links, check if there is only one character in its text
    #This will make sure the <a> tag is apart of the alphabet selection menu
    #Then append those links to a list
    for link in all_links:
        if len(link.get_text()) == 1:
            alphabet_links.append(link['href'])
    return alphabet_links
def writeError(name,code):
    with open("errorPlayer.txt", "a") as myfile:
        myfile.write(name +"," + str(code) +"\n")
def fetchGameTable(id,soup,playoff):

    details = {"date":None,"wasHome":None,"opponent":None,"wasWin":0,"netScore":0,
    "MP":None,"3P":0, "3PA":0,"2P":0, "2PA":0,"FT":0,"FTA":0,"ORB":0,"DRB":0,"AST":0,"STL":0,
    "BLK":0,"TOV":0,"PF":0,"PTS":0,"opponentRoster":None,"wasPlayoff":playoff,"FG":0,"FGA":0}

    games = []

    if playoff == True:
        if soup.find("div", {"id": id}) == None:
            return None

        rows = soup.find("div", {"id": id}).findAll(text=lambda text:isinstance(text, Comment))
        rows = BeautifulSoup(rows[0], 'html.parser')
        rows = rows.find_all('tr')
    else:
        rows = soup.find("div", {"id": id}).find_all('tr')

    for row in rows:

        try:
            column_data = row.find_all('td')

            if(len(column_data) == 0):
                continue

            details["date"] = column_data[1].get_text()
            print("Fetching Game Dated:",details["date"])
            details["wasHome"] = column_data[4].get_text()
            if "@" in details["wasHome"]:
                details["wasHome"] = False
            else:
                details["wasHome"] = True
            details["opponent"] = column_data[5].get_text()
            details["wasWin"] = column_data[6].get_text()
            if "W" in details["wasWin"]:
                        details["wasWin"] = True
            else:
                details["wasWin"] = False
            details["netScore"] = column_data[6].get_text().split("(")[1].strip(")")
            details["MP"] = column_data[8].get_text()
            details["3P"] = column_data[12].get_text()
            details["3PA"] = column_data[13].get_text()
            details["FG"] = column_data[9].get_text()
            details["FGA"] = column_data[10].get_text()
            details["FT"] = column_data[15].get_text()
            details["FTA"] = column_data[16].get_text()
            details["ORB"] = column_data[18].get_text()
            details["DRB"] = column_data[19].get_text()
            details["AST"] = column_data[20].get_text()
            details["STL"] = column_data[21].get_text()
            details["BLK"] = column_data[22].get_text()
            details["TOV"] = column_data[23].get_text()
            details["PF"] = column_data[24].get_text()
            details["PTS"] = column_data[25].get_text()

            validate(details)

            details["2P"] =  int(details["FG"]) - int(details["3P"])
            details["2PA"] = int(details["FGA"]) - int(details["3P"])

            details["opponentRoster"] = None
            if(column_data[5].find('a')!=None):
                roster_link = BASE + column_data[5].find('a')['href']
                details["opponentRoster"] = fetchRoster(roster_link)

            games.append(Game(details))

        except:
            pass
        #create game object


    return games
def fetchRoster(url):
    '''
    Parameters: url as string"
    Returns: list
    Purpose: To "fetch" each season roster of players
    '''
    #time.sleep(1)
    page = requests.get(url)
    #print("request sucess")
    roster = []
    soup = BeautifulSoup(page.text, 'html.parser')
    div_tag = soup.find("div", {"id": "all_roster"})
    table = div_tag.find("tbody").find_all('tr')
    for row in table:
        roster.append(row.find('td').get_text())

    return roster
def fetchSalaries(soup):
    salaries = []
    result = []
    x = soup.find("div", {"id": "all_all_salaries"})
    if x != None:
        for numbers in x.findAll(text=lambda text:isinstance(text, Comment)):
            data = BeautifulSoup(numbers, 'html.parser')
            for number in data.find_all("tr"):
                salaries.append(number.text.split('$'))

    for entry in salaries:
        try:
            result.append([entry[0][:7],entry[1]])
        except IndexError:
            pass

    return result
def fetchBasics(soup):

    basics = {"name":None,"active":None,"position":None,"height":None,"weight":None,
    "nicknames":None,"birthdate":None,"birthplace":None,"age":None, "college":None,
    "link":None,"hand":None,"draftTeam":None,"image":None,"pick":None}

    #load columns
    data1 = soup.find_all('th')
    data2 = soup.find_all('td')

    #fill in data respectively, Round 1
    basics["name"] = data1[0].get_text().strip("*")
    basics["link"] = BASE + data1[0].find('a')['href']
    basics["active"] = data2[0].get_text() + "-" + data2[1].get_text()
    basics["position"] = data2[2].get_text()
    basics["height"] = data2[3].get_text()
    basics["weight"] = data2[4].get_text()
    basics["birthdate"] = data2[5].get_text()
    basics["age"] = YEAR - int(basics["birthdate"].split(",")[1])
    basics["college"] = data2[6].get_text()

    #get the player's in-depth page to finish basics collection
    #time.sleep(1)
    page = requests.get(basics["link"])
    #print("request sucess")
    soup = BeautifulSoup(page.text, 'html.parser')

    #Round 2
    tags = soup.find_all('p')
    for i in range(len(tags)):
        text = tags[i].get_text()
        if "(" in text and basics["nicknames"] == None:
            basics["nicknames"] = text.strip("\n").strip("(").strip(")")
        if "Shoot:" in text:
            text = text.split("Shoots:")[1].strip()
            basics["hand"] = text
        if "Born:" in text:
            basics["birthplace"] = text.strip("\n").strip(" ").split("in")[1].strip("xa").strip("neg").replace("\xa0","").strip("\n").strip('us').strip("\n").strip()
        if "Draft:" in text:
            text = text.split("Draft:")[1].split(",")
            basics["pick"] = text[1] + ", " + text[2].strip("\n").strip()
            basics["draftTeam"] = text[0].strip("\n").strip()

    if soup.find("div", {"class": "media-item"}):
        basics["image"] = soup.find("div", {"class": "media-item"}).find("img")['src']

    return [basics,soup]
def fetchSeasons(soup):

    details = {"year":None,"age":None,"team":None,"position":None,"GP":0,"MP":0,
    "3P":0, "3PA":0,"2P":0, "2PA":0,"FT":0,"FTA":0,
    "ORB":0,"DRB":0,"AST":0,"STL":0,"BLK":0,"TOV":0,"PF":0,"PTS":0,
    "link":None,"games":None,"salary":None, "roster":None,"wentPlayoffs":None,"wasChamp":None}

    #Salary Detection
    print("Fetching Salary")
    salaries = fetchSalaries(soup)
    print("Got Salary")

    season_rows = soup.find("div", {"id": "all_totals"}).findAll(text=lambda text:isinstance(text, Comment))
    season_rows = BeautifulSoup(season_rows[0], 'html.parser').find_all('tr')
    seasons = []

    for season in season_rows:

        header_data = season.find_all('th')
        column_data = season.find_all('td')

        #if the row doesn't pertain to a season, skip it
        if(header_data[0].find('a'))== None:
            continue
        if int(header_data[0].get_text().split("-")[0]) <1980:
            continue

        details["year"] = header_data[0].get_text()
        details["link"] = BASE + header_data[0].find('a')['href']
        details["age"] = column_data[0].get_text()
        details["team"] = column_data[1].get_text()
        details["position"] = column_data[3].get_text()
        details["GP"] = column_data[4].get_text()
        details["MP"] = column_data[6].get_text()
        details["3P"] = column_data[10].get_text()
        details["3PA"] = column_data[11].get_text()
        details["2P"] = column_data[13].get_text()
        details["2PA"] = column_data[14].get_text()
        details["FT"] = column_data[17].get_text()
        details["FTA"] = column_data[18].get_text()
        details["ORB"] = column_data[20].get_text()
        details["DRB"] = column_data[21].get_text()
        details["AST"] = column_data[23].get_text()
        details["STL"] = column_data[24].get_text()
        details["BLK"] = column_data[25].get_text()
        details["TOV"] = column_data[26].get_text()
        details["PF"] = column_data[27].get_text()
        details["PTS"] = column_data[28].get_text()

        details["roster"] = None
        details["salary"] = None

        if(column_data[1].find('a')!=None):
            roster_link = BASE + column_data[1].find('a')['href']
            details["roster"] = fetchRoster(roster_link)

        for salary in salaries:
            if salary[0] == details["year"]:
                details["salary"] = salary[1]
                break

        print("Fetching Season:",details["year"])
        result = fetchGames(details["link"])


        details["wentPlayoffs"] = result[0]
        details["wasChamp"] = result[1]
        details["games"] = result[2]

        seasons.append(Season(details))

    return seasons
def fetchGames(soup):

    #time.sleep(1)
    page = requests.get(soup)

    soup = BeautifulSoup(page.text, 'html.parser')

    wentPlayoffs = False
    wasChamp = False

    games = fetchGameTable("all_pgl_basic",soup,False)
    playoff_games = fetchGameTable("all_pgl_basic_playoffs",soup,True)

    if playoff_games != None:
        wentPlayoffs = True
        wasChamp = playoff_games[-1].isWin()
        games = games +playoff_games

    return [wentPlayoffs,wasChamp, games]
def loadLetter(letter):

    #construct new url with letter link and base, then parse it
    url = BASE +letter
    #time.sleep(1)
    page = requests.get(url)
    #print("request sucess")
    soup = BeautifulSoup(page.text, 'html.parser')

    #load the table of player general data from the html
    players = soup.find_all('tr') #load players from the table

    #sift through each player and begggin aggregating data
    for player in players:

        #DATA-MARK 1: Basic Player Data
        try:
            print("Player:",player.find_all('th')[0].get_text())

            print("Fetching Basics!")
            result = fetchBasics(player)

            if int(result[0]["active"].split("-")[1]) <1980:
                ename = player.find_all('th')[0].get_text()
                print("fetchBasics:: Nullified Player (<1980) - ",ename)
                continue

            #create metadata object
            metaObject = Metadata(result[0])
            print("Got Basics")
        except (IndexError,TypeError):
            ename = player.find_all('th')[0].get_text()
            print("fetchBasics:: Formatting Error for player - ",ename)
            writeError(ename,1)
            continue


        print("Fetching Career!")
        seasons = fetchSeasons(result[1])
        newPlayer = Player(metaObject,seasons)
        print("Got Career! Sucess!")


def main():

    #assign source code requested
    page = requests.get(START)

    #pass source code through beautiful soup and get alphabet links
    soup = BeautifulSoup(page.text, 'html.parser')
    links = getAlphabet(soup)

    #sift through the links and laod their pages
    for letter in links:
        loadLetter(letter)
main()
