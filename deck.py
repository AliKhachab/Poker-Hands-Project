from card import Card
import random

class Deck:
    """
    A class used to represent full deck of playing cards used to deal hands for games like poker, rummy. etc. 
    
    ...

    Attributes
    ----------
    deck_of_cards : list 
        List of Card objects that store the playing cards in the deck.
    

    Methods
    -------
    __init__():
        Constructs a Deck as a list of 52 Card objects in a standard deck of playing cards.  The cards ARE shuffled!  
    __str__():
        Returns a description of all cards in the deck.
    get_next_card(other):
        Returns the next card to be dealt to a player.  The card is deleted from the deck. 
    """


    def __init__(self):
        """
        Parameters: None
        """
        self.deck_of_cards = []
        for suit in range(4):
            for rank in range(2,15):
                card = Card(rank, suit)
                self.deck_of_cards.append(card)
        random.shuffle(self.deck_of_cards)



    def __str__(self):
        """
        Parameters
        ----------
        None

        Returns
        -------
        str: Description of the deck, which includes a description of every card currently in the deck in the (shuffled) order it appears. 
        """
        s = str(len(self.deck_of_cards)) + " cards in deck: \n"
        for c in self.deck_of_cards:
            s = s + str(c) + "\n"
        return s
    


    def get_next_card(self):
        """
        Parameters
        ----------
        None

        Returns
        -------
        Card: Returns the next Card object in the deck and deletes it from the deck.  Remember: This is a Card object; it is NOT a string!
        """
        return self.deck_of_cards.pop()
