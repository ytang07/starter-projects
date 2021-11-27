import random
# 11 = J, 12 = Q, 13 = K, 14 = A
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ["clubs", "diamonds", "hearts", "spades"]

face_cards = {
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
    11: "J",
    12: "Q",
    13: "K",
    14: "A"
}
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def generate_cards():
    cards = []
    for value in card_values:
        for suit in suits:
            if value in face_cards:
                _card = Card(face_cards[value], suit)
            else:
                _card = Card(value, suit)
            cards.append(_card)
    return cards

cards = generate_cards()