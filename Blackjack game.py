#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}
playing = True


# In[8]:


class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


# In[9]:


suits[0]


# In[10]:


class Deck:
    
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp +='\n'+card.__str__()
        return 'The deck has:' + deck_comp
            
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.deck)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        single_card = self.deck.pop()        
        return single_card


# In[11]:


test_deck = Deck()
test_deck.shuffle()
print(test_deck)


# In[ ]:





# In[ ]:





# In[12]:


for card in test_player.cards:
    print(card)


# In[13]:


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank == 'Ace':
            self.aces+=1
            
    def adjust_for_ace(self):
        while self.value >21 and self.aces:
            self.value-=10
            self.aces-=1
            
        


# In[14]:


test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
#Dealing a card from the deck
pulled_card = test_deck.deal_one()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)


# In[15]:


test_player.add_card(test_deck.deal_one())
test_player.value


# In[16]:


class Chips:
    
    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
        
    
    def lose_bet(self):
        self.total-=self.bet
        


# In[17]:


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Select the amount you want to bet: "))
        except ValueError:
            print("Sorry please provide an integer: ")
        else:
            if chips.bet>chips.total:
                print("Sorry you don't have enough chips! You have {}".format(chips.total))
            else:
                break
    
 


# In[18]:


def hit(deck,hand):
    
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()
    
    


# In[19]:


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Hit or stand? Enter H or S ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player stands, dealers turn!")
            playing = False
        else:
            print("Sorry I didn't understand, please enter H or S! ")
            continue
        break
            
            


# In[20]:


def show_some(player,dealer):
    #Show only one of the dealer's cards
    print("\n Dealer's hand: ")
    print(" <card hidden!>")
    print(dealer.cards[1])
    
    #Show all (2)cards in the player's hands
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
        
   
    
def show_all(player,dealer):
    #Show all dealer's cards
    print("\n Dealer's hand: ")
    for card in dealer.cards:
        print(card)
        
    #Calculate and display value
    print(f'Value of dealers hand is {dealer.value}')
    #Show all player's cards
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
    print(f'Value of Players hand is {player.value}')
    
    
 


# In[21]:


def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


# In[22]:


while True:
    # Print an opening statement
    print("Welcome to blackjack!")

    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())
    

    
        
    # Set up the Player's chips
    player_chips = Chips()
    
    
    # Prompt the Player for their bet
    take_bet(player_chips)

    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            
        

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value<=21:
        while dealer_hand.value<17:
            hit(deck,dealer_hand)
                
    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
            
        
    
    # Inform Player of their chips total 
    print("\n Player chips are at: {}".format(player_chips.total))
    # Ask to play again
    new_game = input("Would you like to play again?: y/n")
    if new_game[0].lower()=='y':
        playing = True
    else:
        print('Thank you for playing!')
    

        break


# In[ ]:





# In[ ]:




