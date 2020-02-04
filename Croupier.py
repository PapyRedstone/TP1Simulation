import random

class Croupier:
    def __init__(self):
        self.reset()

    def reset(self):
        #pack of cards that we can draw card from
        self.cards = []
        for t in ["Coeur", "Pique", "Trefle", "Carreau"]:
            for v in range(1,14):
                self.cards += [{"type":t, "value":v}]

        #pack of drawn cards
        self.drawCards = []
        random.shuffle(self.cards)

    def drawCard(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        self.drawCards += [card]
        return card

    #For Debug Purpose
    def showCards(self):
        print("Cards:")
        print(self.cards)

        print("Draw cards:")
        print(self.drawCards)

    def putBackCards(self):
        self.cards += self.drawCards
        self.drawCards = []
        random.shuffle(self.cards)

def testCroupier():
    c = Croupier()

    n = int(input("Entrez le nombre de tirages avec remises : "))
    
    distribution = dict()
    for _ in range(n):
        card = c.drawCard()
        try:
            distribution[str(card["value"]) + " " + card["type"]] += 1
        except KeyError:
            distribution[str(card["value"]) + " " + card["type"]] = 1
        c.putBackCards()

    for (k,v) in distribution.items():
        print("Carte {}   \t tirée   {} fois (erreur {:.3f}%)".format(k, v, abs(v - (n/52))/n*5200))
