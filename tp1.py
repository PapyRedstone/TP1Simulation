#!/usr/bin/python3

from Croupier import *

def game1():
    return

def game2():
    return

def game3():
    return

def game4():
    return

def game5():
    return
    
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
        
        try:
            functions[choice]()
        except KeyError:
            print("Veuillez choisir entre 1,2,3,4,5,c et q")
            
if __name__ == "__main__":
    main()
