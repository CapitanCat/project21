import random
class Card():
    def __init__(self, name, suit, score):
        self.name = name
        self.suit = suit
        self.score = score

    def show(self):
        print(self.name, self.suit)


class Deck():
    def __init__(self,key):
        self.deck = []
        suits = ['Червей','Бубей','Пик','Треф']
        names = {'Туз':11,
                 'Король':4,
                'Дама':3,
                'Валет':2,
                '10':10,
                '9':9,
                '8':8,
                '7':7,
                '6':6,
                '5':5,
                '4':4,
                '3':3,
                '2':2,
                'Джокер':0,
        }
        if key == 36:
            for suit in suits:
                for key, value in names.items():
                    self.deck.append(Card(key,suit,value))
                    if key == '6':
                        break


    def show(self):
        for card in self.deck:
            card.show()


    def shuffle(self):
        random.shuffle(self.deck)

    def pick_top_card(self):
        top_card = self.deck.pop()
        return top_card


d1=Deck(36)
d1.show()
d1.pick_top_card()
