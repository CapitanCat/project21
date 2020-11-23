import random


class Card:                                 # класс карты
    def __init__(self, name, suit, score):
        self.name = name
        self.suit = suit
        self.score = score

    def show(self):                         # Вывод имени и масти карты
        print(self.name, self.suit)


class Deck:
    def __init__(self, key=''):             # По умолчанию колода пуста

        self.deck = []
        suits = ['Червей', 'Бубей', 'Пик', 'Треф']
        names = {'Туз': 11,
                 'Король': 4,
                 'Дама': 3,
                 'Валет': 2,
                 '10': 10,
                 '9': 9,
                 '8': 8,
                 '7': 7,
                 '6': 6,
                 '5': 5,
                 '4': 4,
                 '3': 3,
                 '2': 2,
                 'Джокер': 0,
        }
        if key == 36:
            for suit in suits:
                for key, value in names.items():
                    self.deck.append(Card(key,suit,value))
                    if key == '6':
                        break

    def show(self):                         # Вывод колоды
        for card in self.deck:
            card.show()

    def shuffle(self):                      # Перемешивание колоды
        random.shuffle(self.deck)

    def pick_top_card(self):                # Берем верхнюю карту колоды
        top_card = self.deck.pop()
        return top_card

    def count_score(self):                  # Считаем очки
        score = 0
        for card in self.deck:
            score += card.score

        return score


def player_play():
    hand = Deck()                           # Создаем пустую руку
    deck1 = Deck(36)                        # Создаем колоду в 36 карт
    deck1.shuffle()                         # Перемешиваем
    hand.deck.append(deck1.pick_top_card())     # Берем первую карту из колоды
    hand.deck.append(deck1.pick_top_card())     # Берем вторую карту из колоды
    hand.show()                             # Вывод карт в руке
    while True:
        score = int(hand.count_score())     # Считаем очки
        print('Очков у вас в руке {}'.format(score))
        if score > 21:                      # Если больше 21, то проигрышь
            print('Перебор(')
            break
        vvod = input('Хочешь еще 1 карту?(y/n): ')  # Берем или не берем еще одну карту
        if vvod == 'y':
            hand.deck.append(deck1.pick_top_card())
        if vvod == 'n':
            print('Набратно очков: {}. Ждем результат соперника'.format(score))     # Вывод резултатов
            break
    return score


if __name__ == "__main__":      # Чтобы при импорте файла main не начинала выполняться программа
    result = player_play()
    print(result)


