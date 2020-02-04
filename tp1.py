#!/usr/bin/python3

from Croupier import *

# n is the number of game the simulation must play
def game1(n):
    playerScore = 0
    
    for _ in range(n):
        c = Croupier()
        playerScore -= 1
        if c.drawCard()["value"] == 1:
            playerScore += 10

    #print(playerScore)
    print("Le joueur aura {} {}$ au cours des {} parties".format(
        "gagné" if playerScore >= 0 else "perdu",
        abs(playerScore),
        n))
    
def game2(n):
    playerScore = 0

    for _ in range(n):
        c = Croupier()
        playerScore -= 1
        
        c1 = c.drawCard()
        c.putBackCards()
        c2 = c.drawCard()

        if c1 == c2:
            playerScore += 50

    print("Le joueur aura {} {}$ au cours des {} parties".format(
        "gagné" if playerScore >= 0 else "perdu",
        abs(playerScore),
        n))

    
def game3(n):
    playerScore = 0

    for _ in range(n):
        c = Croupier()
        playerScore -= 1
        
        c1 = c.drawCard()["value"]
        c2 = c.drawCard()["value"]

        if c2 > c1:
            playerScore += 2

    print("Le joueur aura {} {}$ au cours des {} parties".format(
        "gagné" if playerScore >= 0 else "perdu",
        abs(playerScore),
        n))
    
def game4(n):
    playerScore = 0

    for _ in range(n):
        c = Croupier()
        playerScore -= 1
        cards = []

        for _ in range(3):
            cards += [c.drawCard()["type"]]

        playerScore += cards.count("Coeur")

    print("Le joueur aura {} {}$ au cours des {} parties".format(
        "gagné" if playerScore >= 0 else "perdu",
        abs(playerScore),
        n))

def game5(n):
    playerScore = 0
    for _ in range(n):
        playerScore -= 1
        c = Croupier()
        cards = []
        for __ in range(5):
            cards += [c.drawCard()]

        cards.sort(key=lambda c: c["value"])
        for i in range(3):
            c1 = cards[i]["value"]
            c2 = cards[i+1]["value"]
            c3 = cards[i+2]["value"]
            if c1+1 == c2 and c1+2 == c3:
                playerScore += 5
                break
    print("Le joueur aura {} {}$ au cours des {} parties".format(
        "gagné" if playerScore >= 0 else "perdu",
        abs(playerScore),
        n))
            
def main():
    games = {
        "1":game1,
        "2":game2,
        "3":game3,
        "4":game4,
        "5":game5
    }
    functions = {
        "c":testCroupier,
        "q":exit
    }

    while True:
        print("\nQue voulez-vous faire ?")
        print("\tJeu 1 (1)")
        print("\tJeu 2 (2)")
        print("\tJeu 3 (3)")
        print("\tJeu 4 (4)")
        print("\tJeu 5 (5)")
        print("\tTester le croupier (c)")
        print("\tQuitter (q)")
        
        choice = input()

        try:
            if choice in functions.keys():
                functions[choice]()
            elif choice in games.keys():
                n = int(input("Combien de parties voulez jouez ? "))
                functions[choice](n)
            else:
                raise KeyError
        except ValueError:
            print("Veuillez entrer un nombre")
        except KeyError:
            print("Veuillez choisir une entree correcte")

            
if __name__ == "__main__":
    main()
