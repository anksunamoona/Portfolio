import random

def create_deck():
    """Create a deck of cards."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def card_value(card):
    """Return the value of a card."""
    if card['rank'] in ['Jack', 'Queen', 'King']:
        return 10
    elif card['rank'] == 'Ace':
        return 11
    else:
        return int(card['rank'])

def calculate_score(hand):
    """Calculate the score of a hand."""
    score = sum(card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card['rank'] == 'Ace')
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
    return score

def display_hand(hand):
    """Display the cards in a hand."""
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")

def blackjack():
    """Play a game of Blackjack."""
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Welcome to Blackjack!")
    print("Your hand:")
    display_hand(player_hand)
    print("Player's Score:", calculate_score(player_hand))
    print("Dealer's hand:")
    print(f"Face up card: {dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
    
    while True:
        player_score = calculate_score(player_hand)
        if player_score == 21:
            print("Blackjack! You win!")
            break
        elif player_score > 21:
            print("Bust! You lose.")
            break
        
        action = input("Do you want to (h)it or (s)tand? ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            print("Your hand:")
            display_hand(player_hand)
            print("Player's Score:", calculate_score(player_hand))
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    if player_score <= 21:
        print("Dealer's hand:")
        display_hand(dealer_hand)
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
        dealer_score = calculate_score(dealer_hand)
        print(f"Dealer's score: {dealer_score}")
        if dealer_score > 21 or dealer_score < player_score:
            print("You win!")
        elif dealer_score > player_score:
            print("Dealer wins.")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    blackjack()
