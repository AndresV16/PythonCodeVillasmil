# Andres Villasmil Ocando
# aev1@williams.edu
# Assignment 6: Perfect Shuffle

# need to ask user how many times to shuffle
import Epic

# components of the deck
rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

# for every rank in every suit make a card and place it in the deck
def build_deck(rank, suit):
    deck = []
    for r in rank:
        for s in suit:
            deck.append("%s of %s" % (r, s))
    return deck

# perfect shuffle function
def shuffle(deck):
    half1 = []
    half2 = []
    half1 = deck[0:len(deck)/2]
    half2 = deck[len(deck)/2:]
    
    shuffled_deck = []
    for i in range(0, len(deck)):
        if i % 2 == 0: # use remainder function to quantify list and split
            shuffled_deck.append(half1[0])
            del half1[0]
        else:
            shuffled_deck.append(half2)
            del half2[0]
            
    return shuffled_deck
    
# deal 5 cards
def deal(deck):
    return deck[0:5]


def main():
    d = build_deck(rank, suit)
    
    times = Epic.userInt("How many times would you like the deck to be shuffled?:")
    
    for i in range(0,times):
        d = shuffle(d)
    print deal(d)
    
main()