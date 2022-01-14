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
  
  for i in suits:
    for e in ranks:
      deck.append(e+i)
  return deck
  
  '''
  use the two lists to create a new list "deck" 
  return the deck list to your calling function

  def dealing():
    list1 = []
    suit = ["Hearts", "Clubs", "Spades", "Diamonds"]
    value = ["Ace","One", "Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
    for i in suit:
        for e in value:
            list1.append(e + " of " + i)
    while True:
        playeracards = random.sample(list1,5)
        for i in playeracards:
            list1.remove(i)
        playerbcards = random.sample(list1,5)
        for i in playerbcards:
            list1.remove(i)
        print(f"PlayerA dealt: {playeracards}")
        print(f"PlayerB dealt: {playerbcards}\n")
        input("Enter to draw again: ")
        if len(list1) < 10:
            print("Out of cards")
            exit()
  '''



def main():
  deck = createDeck()
  assert ("JH" in deck) == True
  assert ("AC" in deck) == True
  assert ("TD" in deck) == True
  assert len(deck) == 52
  
if __name__ == "__main__":
  main()