from card import Card 
from deck import Deck 


#WRITE YOUR HAND CLASS BELOW
class Hand:
  hand_types_list = ['High card', 'One pair', 'Two pairs', 'Three of a kind', 'Straight', 'Flush', 'Full house', 'Four of a kind', 'Straight flush']
  hand_types_to_strength = {
    hand_type: index 
    for index, hand_type 
    in enumerate(hand_types_list)
  }
  list_of_ranks = [None, None, 'Two', 'Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack', 'Queen','King','Ace']
  ranks_to_numbers = {
    rank_word: rank 
    for rank, rank_word
    in enumerate(list_of_ranks)
    if rank_word is not None
  }
  
  def __init__(self):
    self.hand = []
    self.dirty = True
    self.rank_dictionary = {}
    self.hand_type = None

  
  def add_card(self, card):
    self.hand.append(card)
    self.dirty = True
    
  def __str__(self):
    string = ""
    for i in self.hand:
      string+=str(i) + '\n'
    return string

  def hand_type_to_strength(self):
    return Hand.hand_types_to_strength[self.hand_type]
    
  def __evaluate_straight(self):
    self.high_card = self.hand[4]
    
  def __evaluate_n_of_a_kind(self, n):
    self.kickers = []
    self.ranks_of_a_kind = []
    for rank, count in self.rank_dictionary.items():
      if count == n:
        self.ranks_of_a_kind.append(Hand.ranks_to_numbers[rank])
      else:
        self.kickers.append(Hand.ranks_to_numbers[rank])
    self.ranks_of_a_kind.sort(reverse = True)
    self.kickers.sort(reverse = True)


  
  def __evaluate_full_house(self):
    for rank, count in self.rank_dictionary.items():
      if count == 3:
        self.triple = Hand.ranks_to_numbers[rank]
      else:
        self.pair = Hand.ranks_to_numbers[rank]
  

    
  def evaluate_hand(self):
    if not self.dirty:
      return
    self.hand.sort()
    self.rank_dictionary = self.get_rank_dictionary()
    self.hand_type = self.get_hand_type()
    
    if self.hand_type == "Straight flush" or self.hand_type == "Straight":
      self.__evaluate_straight()
      
    elif self.hand_type == "Four of a kind":
      self.__evaluate_n_of_a_kind(4)
          
    elif self.get_hand_type() == "Full house":
      self.__evaluate_full_house()
      
    elif self.get_hand_type() == "Three of a kind":
      self.__evaluate_n_of_a_kind(3)
          
    elif self.get_hand_type() == "Two pairs":
      self.__evaluate_n_of_a_kind(2)
          
    elif self.get_hand_type() == "One pair":
      self.__evaluate_n_of_a_kind(2)
  
    self.dirty = False
    
  

      

  def add_cards_from_deck(self, deck_name, number_of_cards):
    for i in range(number_of_cards):
      self.hand.append(deck_name.get_next_card())
    self.dirty = True
    
  def get_rank_dictionary(self):
    rank_dictionary = {}
    for i in self.hand:
      if i.get_rank_name() not in rank_dictionary:
        rank_dictionary[i.get_rank_name()] = 1
      else:
        rank_dictionary[i.get_rank_name()] += 1
    return rank_dictionary

  def check_one_pair(self):
    a = self.get_rank_dictionary()
    count = 0
    three_check = False
    for i in a:
      if a[i] == 2:
        count+=1
      elif a[i] == 3:
        three_check = True
    if count == 1 and not three_check:
      return True
    return False

  def check_two_pair(self):
    a = self.get_rank_dictionary()
    counter = 0
    for i in a:
      if a[i] == 2:
        counter+=1
        if counter == 2:
          return True
    return False
    
  def check_three_of_a_kind(self):
    a = self.get_rank_dictionary()
    counter = 0
    two_checker = False
    for i in a:
      if a[i] == 3:
        counter +=1
      elif a[i] == 2:
        two_checker = True
    if counter == 1 and not two_checker:
      return True
    return False
  
  def check_four_of_a_kind(self):
    a = self.get_rank_dictionary()
    for i in a:
      if a[i] == 4:
        return True
    return False

  def check_full_house(self):
    a = self.get_rank_dictionary()
    two_counter = 0
    three_counter = 0
    for i in a:
      if a[i] == 2:
        two_counter+=1
      elif a[i] == 3:
        three_counter+=1
    if two_counter == three_counter and two_counter == 1:
      return True
    return False

  def check_flush(self):
    for i in range(1, len(self.hand)):
      if self.hand[i].suit != self.hand[i-1].suit:
        return False
    return True

      
  def sort(self):
    self.hand.sort()
    
  def check_straight(self):
    list = []
    for i in self.hand:
      number = i.get_rank_name()
      list.append(Hand.list_of_ranks.index(number))
    list.sort()
    for i in range(1, len(list)):
      if list[i] != list[i-1] + 1:
        return False
    return True
    
  def check_straight_flush(self):
    if self.check_flush() and self.check_straight():
      return True
    return False

  def get_hand_type(self):
    if self.hand == []:
      return "Hand is empty"
    if self.check_straight_flush():
      return "Straight flush" 
    elif self.check_four_of_a_kind():
      return "Four of a kind"
    elif self.check_full_house():
      return "Full house"
    elif self.check_flush():
      return "Flush"
    elif self.check_straight():
      return "Straight"
    elif self.check_three_of_a_kind():
      return "Three of a kind"
    elif self.check_two_pair():
      return "Two pairs"
    elif self.check_one_pair():
      return "One pair"
    else:
      return "High card"

  def __n_of_a_kind_lt(self, other):
    for rank, other_rank in zip(self.ranks_of_a_kind, other.ranks_of_a_kind):
      if rank != other_rank:
        return rank < other_rank
    for rank, other_rank in zip(self.kickers, other.kickers):
      if rank != other_rank:
        return rank < other_rank
    return False

  def __full_house_lt(self, other):
    if self.triple != other.triple:
      return self.triple < other.triple
    return self.pair < other.pair

  def __straight_lt(self, other):
    return self.high_card < other.high_card

  def __high_card_lt(self, other):
    for card, other_card in zip(reversed(self.hand), reversed(other.hand)):
      if card.rank != other_card.rank:
        return card < other_card
    return False

  
  def __is_same_type_lt(self, other):
    if self.hand_type == "Straight flush" or self.hand_type == "Straight":
      return self.__straight_lt(other)
      
    elif self.hand_type == "Four of a kind" or self.hand_type == "Three of a kind" or self.hand_type == "Two pairs" or self.hand_type == "One pair":
      return self.__n_of_a_kind_lt(other)
      
    elif self.hand_type == "Full house":
      return self.__full_house_lt(other)

      
    elif self.hand_type == "Flush" or self.hand_type == "High card":
      return self.__high_card_lt(other)
  
  
    
  def __lt__(self, other):
    self.evaluate_hand()
    other.evaluate_hand()
    if self.hand_type != other.hand_type:
      return self.hand_type_to_strength() < other.hand_type_to_strength()
      
    else:
      return self.__is_same_type_lt(other)

  
  def __eq__(self, other):
    self.evaluate_hand()
    other.evaluate_hand()
    if self.hand_type != other.hand_type:
      return False
    else:
      selflist = []
      otherlist = []
      for i in range(len(self.hand)):
        selflist.append(self.hand[i].rank)
        otherlist.append(other.hand[i].rank)
      if sorted(selflist) == sorted(otherlist):
        return True
      return False
                  
  def __gt__(self, other):
    return not self.__lt__(other) and not self.__eq__(other)
      
