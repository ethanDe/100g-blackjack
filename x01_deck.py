#!python3

"""
Create a list of cards
the cards should be denoted with a number or A, J, Q, K, T (for ace, jack, queen, king or ten)
as well as a suit
"""
import random as r
def createDeck():
  ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
  suits = ['C','D','H','S']
  deck = []
  
  return deck
  
  '''
  use the two lists to create a new list "deck" 
  return the deck list to your calling function
  '''

def main():
  deck = createDeck()
  assert "JH" in deck == True
  assert "AC" in deck == True
  assert "TD" in deck == True
  assert len(deck) == 52
  
if __name__ == "__main__":
  main()
