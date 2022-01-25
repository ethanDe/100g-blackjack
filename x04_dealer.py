#!python3

'''
In Blackjack, the dealer always must follow the same rules.

1. They will stand pat (not take new cards) if their score is over 16
2. They will automatically take a new card if their score is less than 17
'''
import x02_value as z
#split list into integer
#if value not integer: try with 11, add if not greater than 21, add 11 else add 1
def myValue(inList):
  if type(inList) == list:
    if score + 11 > 21:
      return 1
    elif score + 11 <= 21:
      return 11
#^ in progress

def dealer(deck):
  dealer = []
  score = 0
  
  for i in range(len(deck)):
    dealer.append(deck[i])
    score = z.value(dealer)
    if score > 16:
      break
  for i in dealer:
    deck.remove(i)
  return [dealer,score]

deck = ['3C', '3S', '8S', '3D', 'AC', '9H', 'QC', 'TD', 'TH', '8H', '8D', '7C', 'TS', '7D', 'AD', 'QD', 'KC', '6H', 'JH', 'KH', 'QS', '6C', '4H', '7H', '5S', '2S', 'AS', 'AH', '5C', '2D', '2H', '6D', 'TC', '4C', 'JS', 'JC', 'KD', '2C', '4S', '3H', '5H', '7S', 'KS', '5D', 'QH', '6S', '8C', '9D', 'JD', '9S', '9C', '4D']
run1 = dealer(deck)
print(run1)
run2 = dealer(deck)
print(run2)
exit()
''' 
inputs:
list deck: contains a shuffled list of cards
return:
list of lists:
list[0] : the dealer's hand
list[1] : the dealer's count
list[2] : the remaining deck

function will keep drawing a card from the deck until they have a score > 16
You may need to use the function in problem 2 to count the score
it will then return a list
'''

#return [ dealer , score , deck ]
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
  deck = ['3C', '3S', '8S', '3D', 'AC', '9H', 'QC', 'TD', 'TH', '8H', '8D', '7C', 'TS', '7D', 'AD', 'QD', 'KC', '6H', 'JH', 'KH', 'QS', '6C', '4H', '7H', '5S', '2S', 'AS', 'AH', '5C', '2D', '2H', '6D', 'TC', '4C', 'JS', 'JC', 'KD', '2C', '4S', '3H', '5H', '7S', 'KS', '5D', 'QH', '6S', '8C', '9D', 'JD', '9S', '9C', '4D']
  run1 = dealer(deck)
  assert dealer(deck) == [['3C', '3S', '8S', '3D'], 17, run1[2] ]
  run2 = dealer( run1[2] )
  assert dealer(run1[2]) == [['AC', '9H'], 20, run2[2] ]

if __name__ == "__main__":
  main()
