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

        self.cards = []
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
                    self.cards.append(Card(key, suit, value))
                    if key == '6':
                        break

    def show(self):                         # Вывод колоды
        for card in self.cards:
            card.show()

    def shuffle(self):                      # Перемешивание колоды
        random.shuffle(self.cards)

    def pick_top_card(self):                # Берем верхнюю карту колоды
        top_card = self.cards.pop()
        return top_card

    def count_score(self):                  # Считаем очки
        score = 0
        if self.cards:
            for card in self.cards:
                score += card.score
        return score


class Player:
    def __init__(self):
        self.hand = Deck()
        self.passed = False

    def makemove(self):
        if self.hand.count_score() >= 17:  # Ставим некоторое условие, при котором должны пасовать:
            self.passed = True


def player_play():
    hand = Deck()                           # Создаем пустую руку
    deck = Deck(36)                        # Создаем колоду в 36 карт
    deck.shuffle()                         # Перемешиваем
    hand.cards.append(deck.pick_top_card())     # Берем первую карту из колоды
    hand.cards.append(deck.pick_top_card())     # Берем вторую карту из колоды
    while True:
        hand.show()  # Вывод карт в руке
        score = int(hand.count_score())     # Считаем очки
        print('Очков у вас в руке {}'.format(score))
        if score > 21:                      # Если больше 21, то проигрыш
            print('Перебор(')
            break
        vvod = input('Хочешь еще 1 карту?(y/n): ')  # Берем или не берем еще одну карту
        if vvod == 'y':
            hand.cards.append(deck.pick_top_card())
        if vvod == 'n':
            print('Набратно очков: {}. Ждем результат соперника'.format(score))     # Вывод резултатов
            break
    return score


def game_template():
    player1 = Player()  # Сейчас сражаются клоны, потом каждый подставит свой класс такого шаблона
    player2 = Player()
    for p in player1, player2:  # Выполняем следующий код для обоих игроков
        deck = Deck(36)
        deck.shuffle()
        p.hand.cards.append(deck.pick_top_card())
        p.hand.cards.append(deck.pick_top_card())
        p.makemove()  # Этот метод некоторым образом решает, пасовать или нет; если нет, то тянем карту
        while True:
            p.makemove()  # Этот метод некоторым образом решает, пасовать или нет; если нет, то тянем карту
            # Игрок тянет карты или пока не спасует сам, или пока не наберет больше 21
            if p.hand.count_score() > 21 or p.passed is True:
                break
            p.hand.cards.append(deck.pick_top_card())  # Если не спасовали, то тянем карту
        if p.hand.count_score() > 21:  # Если набрали больше 21, то буквально сбрасываем руку:
            p.hand = Deck()
            p.passed = True  # И на всякий случай принудительно становимся спасовавшим

    score1 = player1.hand.count_score()
    score2 = player2.hand.count_score()
    if score1 > score2:
        # print('Со счетом ' + str(score1) + ' : ' + str(score2) + ' победил первый игрок!')
        return 'Первый игрок победил'
    elif score1 < score2:
        # print('Со счетом ' + str(score1) + ' : ' + str(score2) + ' победил второй игрок!')
        return 'Второй игрок победил'
    else:
        # print('Со счетом ' + str(score1) + ' : ' + str(score2) + ' матч окончился вничью!')
        return 'Ничья'


if __name__ == "__main__":      # Чтобы при импорте файла main не начинала выполняться программа
    results = {'Первый игрок победил': 0, 'Второй игрок победил': 0, 'Ничья': 0}
    for i in range(20000):
        results[game_template()] += 1
    print(*results.items())
    #result = player_play()
    #print(result)


