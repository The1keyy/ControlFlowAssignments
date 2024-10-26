import stdrandom
import stdio

# define the suits and ranks of a deck of cards
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# randomly select a suit and a rank
random_suit = stdrandom.uniformInt(0,4)
random_rank = stdrandom.uniformInt(0,13)

# print the selcted card
selected_card = ranks[random_rank] + " of " + suits[random_suit]
stdio.writeln(selected_card)



...
