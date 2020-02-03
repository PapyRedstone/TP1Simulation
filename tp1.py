#!/usr/bin/python3

from Croupier import *

# n is the number of game the simulation must play
def game1(n):
    playerScore = 0
    for _ in range(n):
        playerScore -= 1
        c = Croupier()
        if c.drawCard()["value"] == 1:
            playerScore += 10

    #print(playerScore)
    print("Le joueur aura {} {}$ au cours des {} parties".format(
        "gagné" if playerScore >= 0 else "perdu",
        abs(playerScore),
        n))
    
def game2(n):
    return

    
def game3(n):
    return
    
def game4(n):
    return

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
    functions = {
        "c":testCroupier,
        "1":game1,
        "2":game2,
        "3":game3,
        "4":game4,
        "5":game5,
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
        #choice = "5" #for testing

        try:
            if choice == 'q' or choice == 'c':
                functions[choice]()
            else:
                n = int(input("Combien de parties voulez jouez ? "))
                #n = 1 # for testing
                functions[choice](n)
            #return #for testing
        except ValueError:
            print("Veuillez entrer un nombre")
        except KeyError:
            print("Veuillez choisir une entree correcte")

            
if __name__ == "__main__":
    main()
