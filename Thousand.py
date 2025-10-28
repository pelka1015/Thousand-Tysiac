import random
# import os

# Generating cards
class Card:
    def __init__(self, value, suit, game_value):
        self.value = value
        self.suit = suit
        self.game_value = game_value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

suits = ["diamonds", "hearts", "clubs", "spades"]
values = ['9', '10', 'Jack', 'Queen', 'King', 'Ace']
game_values = {'9': 0, '10': 10, 'Jack': 2, 'Queen': 3, 'King': 4, 'Ace': 11}

cards = [Card(value, suit, game_values[value]) for suit in suits for value in values]
random.shuffle(cards)

# Pile of cards (for the talon)
class PileOfCards:
    def __init__(self):
        self.hand = []
        
    def add_card_to_hand(self, num):
        for _ in range(num):
            if cards:
                self.hand.append(cards.pop(0))
                
    def show_hand(self):
        return self.hand

# Player (as subclass)
class Player(PileOfCards):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.points = 0
        self.bid = 0
        self.fold = False
        self.declared_points = 0

    def __repr__(self):
        return f"Player({self.name}, Hand: {self.hand}, Points: {self.points}, Bid: {self.bid}, Fold: {self.fold})"
        

######################################### FUNCTIONS ########################################    

# Meld function
def meld(self):
    melds = {"spades": 40, "clubs": 60, "diamonds": 80, "hearts": 100}
    for suit, meld_value in melds.items():
        if any(card.value == "King" and card.suit == suit for card in self.hand) and \
           any(card.value == "Queen" and card.suit == suit for card in self.hand):
            print(f"{self.name} melds {meld_value} ({suit})")
            self.points += meld_value
            return suit
    return None

# Dealing cards
def deal_cards(player_list, cards_per_player, include_talon, talon_cards_count):
    for player in player_list:
        player.add_card_to_hand(cards_per_player)
    if include_talon:
        talon = PileOfCards()
        talon.add_card_to_hand(talon_cards_count)
        return talon
    return None

# Bidding for 3-player game
def bidding(player_list):
    bid_value = 100
    for player in player_list:
        player.bid = bid_value
    player_list[0].bid += 1
    print(player_list[0].name, "starts the bidding at", bid_value)

    while True:
        for player in player_list:
            if player.fold:
                continue

            print(player.name, "Your cards:", player.show_hand())
            
            decision = input("Do you raise? (yes/no) ").lower()
            if decision == "yes":
                raise_amount = int(input("By how much do you raise? "))
                player.bid += raise_amount
                bid_value += raise_amount
                print(player.bid)
            elif decision == "no":
                player.fold = True
                print(f"{player.name} folds.")
            
            print("Current bid value:", bid_value)
            
            active_players = [p for p in player_list if not p.fold]
            
            if len(active_players) == 0:
                if player_list[0].bid > player_list[1].bid and player_list[0].bid > player_list[2].bid:
                    winner = player_list[0]
                elif player_list[1].bid > player_list[0].bid and player_list[1].bid > player_list[2].bid:
                    winner = player_list[1]
                else: 
                    winner = player_list[2]     
                    
                print(winner.name, "wins the bidding.")
                return winner

# Instead of clearing console
def next_player():
    print(" " * 50)

####################################### GAME LOGIC ###############################################   

def show_playable_cards(hand):
    print("Cards to play:")
    for idx, card in enumerate(hand):
        print(f"{idx}: {card}")

def show_discardable_cards(hand):
    print("Cards to discard:")
    for idx, card in enumerate(hand):
        print(f"{idx}: {card}")

def handle_talon(player, talon, num_players, player_list):
    print("Talon:", talon.show_hand())
    if num_players == 2:
        choice = int(input("Choose pile 1 or 2: ")) - 1
        chosen_cards = talon.hand[choice*2: (choice+1)*2]
        player.hand.extend(chosen_cards)
        discarded_cards = talon.hand[(1-choice)*2: (2-choice)*2]
        print("Discarded cards:", discarded_cards)
    else:
        player.hand.extend(talon.hand)
        print("Player takes the talon.")
    while len(player.hand) > 7:
        show_discardable_cards(player.hand)
        discard_index = int(input(f"You have {len(player.hand)} cards, choose one to discard (0-{len(player.hand)-1}): "))
        player.hand.pop(discard_index)

def declare_points(player):
    while True:
        declaration = int(input(f"{player.name}, declare the number of points you intend to earn: "))
        if declaration >= player.bid and declaration % 10 == 0:
            player.declared_points = declaration
            print(f"{player.name} declared {declaration} points.")
            break
        else:
            print("The declaration must be a multiple of 10 and not less than your bid.")    

# Main game play
def play_round(winning_player):
    for round_num in range(10):
        print(f"--- Round {round_num + 1} ---")
        
        # Winning player plays a card
        played_card_index = int(input(f"{winning_player.name}, your cards: {winning_player.hand}, choose card to play (0-{len(winning_player.hand)-1}): "))
        card = winning_player.hand.pop(played_card_index)
        print(f"{winning_player.name} plays {card}")
        
        # Opponents play
        for opponent in players:
            if opponent != winning_player:
                print(f"{opponent.name}, your cards: {opponent.show_hand()}")
                opp_card_index = int(input(f"{opponent.name}, choose card to play (0-{len(opponent.hand)-1}): "))
                opp_card = opponent.hand.pop(opp_card_index)
                print(f"{opponent.name} plays {opp_card}")
                
                # Compare cards and assign points
                if card.suit == opp_card.suit:
                    if card.game_value > opp_card.game_value:
                        winning_player.points += card.game_value + opp_card.game_value
                        print(f"{winning_player.name} wins the round and gains {card.game_value + opp_card.game_value} points.")
                    else:
                        opponent.points += card.game_value + opp_card.game_value
                        print(f"{opponent.name} wins the round and gains {card.game_value + opp_card.game_value} points.")
                else:
                    if card.suit == "hearts" or opp_card.suit == "hearts":
                        if card.suit == "hearts":
                            winning_player.points += card.game_value + opp_card.game_value
                            print(f"{winning_player.name} wins the round and gains {card.game_value + opp_card.game_value} points.")
                        else:
                            opponent.points += card.game_value + opp_card.game_value
                            print(f"{opponent.name} wins the round and gains {card.game_value + opp_card.game_value} points.")
                    else:
                        print("The round ends in a draw.")

        # Show updated score
        print(f"Scores after round {round_num + 1}:")
        for player in players:
            print(f"{player.name}: {player.points} points")

    # End of game summary
    print("--- End of Game ---")
    for player in players:
        if player.points >= player.declared_points:
            print(f"{player.name} scored {player.points} points and met their declaration!")
        else:
            print(f"{player.name} scored {player.points} points but did not meet their declaration.")

    # Announce winner
    winner = max(players, key=lambda p: p.points)
    print(f"The winner is {winner.name} with {winner.points} points.")

  
# Main Menu
def main():
    while True:
        print("=== Main Menu ===")
        print("1. 2-player game")
        print("2. 3-player game")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '3':
            break
        elif choice == '1':
            two_player_game()
        elif choice == '2':
            three_player_game()
        else:
            print("Invalid option. Try again.")

        
def two_player_game():
    global players
    player_1 = Player(input("Enter the name of the first player: "))
    player_2 = Player(input("Enter the name of the second player: "))
    next_player()
    players = [player_1, player_2]
    random.shuffle(players)
    talon = deal_cards(players, 8, 1, 4)
    handle_talon(players[0], talon, 2, players)
    declare_points(players[0])
    play_round(players[0])

def three_player_game():
    global players
    player_1 = Player(input("Enter the name of the first player: "))
    player_2 = Player(input("Enter the name of the second player: "))
    player_3 = Player(input("Enter the name of the third player: "))
    next_player()
    players = [player_1, player_2, player_3]
    random.shuffle(players)
    talon = deal_cards(players, 7, 1, 3)
    winner = bidding(players)
    handle_talon(winner, talon, 3, players)
    declare_points(winner)
    play_round(winner)


main()
