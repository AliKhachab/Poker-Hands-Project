class Card:
    """
    A class used to represent a single playing Card
    
    ...

    Attributes
    ----------
    rank : int
        the rank on the card, e.g. 14 is for Ace, 13 is for King, ....2 is for Two
    suit : int
        the suit of the card, i.e. 3 is for Spades, 2 is for Hearts, 1 is for Diamonds, 0 is for Clubs


    Methods
    -------
    __init__(rank, suit):
        Constructs a playing card
    __str__():
        Returns a description of the playing card, e.g. "Ace of Spades"
    __gt__(other):
        Checks if one Card is ranked higher than another Card
    get_suit_name():
        Returns the suit name of the Card, i.e. "Hearts" or "Spades" or "Clubs" or "Diamonds"
    get_rank_name():
        Returns the rank name of the Card, i.e. "Ace" or "King" or "Queen" or ,,, or "Two"
    """


    #class attributes
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, None, 'Two', 'Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack', 'Queen','King','Ace']



    def __init__(self, rank, suit):
        """
        Parameters
        ----------
        rank : str or int
            If rank is a string, it should be a value like "Ace" or "King" or "Queen" or ... or "Three" o "Two"
            If rank is an int, it should be between 2 and 14 and the mapping used is 14-->Ace, 13-->King, ...2-->Two
        suit : str or int
            If suit is a string, it should be either "Clubs" or "Diamonds" or "Hearts" or "Spades"
            If rank is an int, it should be between 0 and 3 and the mapping used is 3-->Spades, 2-->Hearts, 1-->Diamonds, 0-->Clubs
        """
        
        #the rank of the playing card is ALWAYS stored as an int
        #but this allows it to be created with either an int or a str like "Ace" or "Two" or "Three"
        if isinstance(rank, int) and 1 < rank < 15:
            self.rank = rank 
        elif isinstance(rank, str) and rank in Card.rank_names[2:]:
            self.rank = Card.rank_names.index(rank)
        else: 
            raise Exception('The rank of a card should be a str ("Ace", "Two", etc.) or an int (2 through 14)')

        if isinstance(suit, int) and -1 <  suit < 4:
            self.suit = suit
        elif isinstance(suit, str) and suit in Card.suit_names:
            self.suit = Card.suit_names.index(suit)
        else:
            raise Exception('The suit of a card should be a str ("Hearts", "Clubs", etc.) or an int (0 through 3)')



    def __str__(self):
        """
        Parameters
        ----------
        None

        Returns
        -------
        str: Description of the card like "Ace of Diamonds" or "Two of Clubs"
        """
        return self.get_rank_name() + " of " + self.get_suit_name()



    def __gt__(self, other):
        """
        Parameters
        ----------
        other: Card

        Returns
        -------
        bool: Returns True if the card that called the method is higher ranked than the other card.  Compares rank first and then suit if the ranks are tied. 
        """
        if self.rank == other.rank:
            return self.suit > other.suit
        else:
            return self.rank > other.rank
    
    def __eq__(self, other):
        """
        Parameters
        ----------
        other: Card

        Returns
        -------
        bool: Returns True if the card that called the method is the same rank and suit as the other card  
        """
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        """
        Parameters
        ----------
        other: Card

        Returns
        -------
        bool: Returns True if the card that called the method is lower ranked than the other card. 
        """
        return (not self==other) and (not self > other)


    def get_suit_name(self):
        """
        Parameters
        ----------
        None

        Returns
        -------
        str: Returns the suit name of the card, such as  "Clubs" or "Diamonds" or "Hearts" or "Spades" 
        """
        return Card.suit_names[self.suit]



    def get_rank_name(self):
        """
        Parameters
        ----------
        None

        Returns
        -------
        str: Returns the rank name of the card, such as  "Two" or "Three" or ... or "Queen" or "King" or Ace 
        """
        return Card.rank_names[self.rank]

#This is a class that will create card objects. This is the foundation of the entire project. Without these objects, the project would not work as smoothly.