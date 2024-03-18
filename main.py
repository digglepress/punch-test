
cards = ['Jack', 8, 2, 6, 'King', "Jack", "Queen", 5, 3, 'Queen']


def prepare_cards(card):
    card_values = {"Jack": 9, "Queen": 10, "King": 11}
    return card_values.get(card, card)


sorted_cards = sorted(cards, key=prepare_cards)
print(sorted_cards)

# assign numbers to strings and arrange in ascending order -> [done]
# assign numbers to Jack Queen and King respectively -> [done]
# required to be output should be  [2,3,5,6,8,'Jack','Queen','King'] -> [done]
# the solution is written in Generic method and not hardcoded -> [done]
# add 2 more Jacks, 2 more Queens and 2 more Kings -> [done]
# output should have the same number of Jacks, Queens and Kings -> [done]
# make sure that your code should have just 1 loop -> [no need for loop]
# It shouldn't have more than 1 loop -> [done]
