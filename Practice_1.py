import requests
from bs4 import BeautifulSoup

month_dict = {"January": 1, "February" : 2, "March" : 3,
              "April" : 4, "May" : 5, "June" : 6, "July" : 7,
              "August" : 8, "September" : 9, "October" : 10,
              "November" : 11, "December" : 12}
price_dict_CSGO = {}
price_dict_Dota2 = {}

def main():

    get_game("https://en.game-tournaments.com/dota-2/tournaments", "Dota 2")
    get_game("https://en.game-tournaments.com/csgo/tournaments", "CSGO")

    print("Please enter a command: ")
    user_input = ""
    while user_input != "Exit":
        user_input = input()

        if user_input == "Print Dota 2":

            print_total("Dota 2")

        elif user_input == "Print CSGO":

            print_total("CSGO")

        print("Please enter a command: ")

def print_total(game):

    print("Please enter a month: ")
    
    month = input()

    print("Please enter a year: ")
    
    year = int(input())
    
    summ = 0
    if game == "Dota 2":
        for tourn in price_dict_Dota2[month_dict[month]*100 + (year - 2000)]:
            summ += int(tourn[2])
    elif game == "CSGO":
        for tourn in price_dict_CSGO[month_dict[month]*100 + (year - 2000)]:
            summ += int(tourn[2]) 

    print("The total prize monet for the month of " + month + ", " + str(year) + " is: $" + str(summ))
    print()
    


def get_game(url, game):
    

    r = requests.get(url)
    #print(r.status_code)
    
    soup = BeautifulSoup(r.text, "html.parser")


    tournaments = soup.find("tbody").find_all("tr")

    for tournament in tournaments:

        name = tournament.find("a", "teamname1").text.strip()
        date = tournament.find("time", "sct").text.strip()

        month = date.split()[0]
        year = int(date.split()[2])

        
        
        price = tournament.find("span", "badge-money").text.strip().replace(",", "")


        
        hsh = month_dict[month]*100 + (year - 2000)

        if game == "Dota 2":
            if hsh not in price_dict_Dota2:
                price_dict_Dota2[hsh] = [(name, date, price)]
            else:
                price_dict_Dota2[hsh].append((name, date, price))
        elif game == "CSGO":
            if hsh not in price_dict_CSGO:
                price_dict_CSGO[hsh] = [(name, date, price)]
            else:
                price_dict_CSGO[hsh].append((name, date, price))

 

main()

