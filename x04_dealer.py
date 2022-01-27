#!python3

'''
In Blackjack, the dealer always must follow the same rules.

1. They will stand pat (not take new cards) if their score is over 16
2. They will automatically take a new card if their score is less than 17
'''
score = 0

def value(hand):

  value = []
  total = 0
  face = ['J','K','Q','T']
  no = ['2','3','4','5','6','7','8','9']
  ex = ['A']

  for value in hand:
    if value[:1] in face:
      total = total + 10
    elif value[:1] in no:
      total = total + int(value[:1])
    elif value[:1] in ex:
        if total + 11 > 21:
          total = total + 1
        elif total + 11 <= 21:
          total = total + 11
  return total

def dealer(deck):
  dealer = []
  for i in range(len(deck)):
    dealer.append(deck[i])
    score = value(dealer)
    if score > 16:
      break
  for i in dealer:
    deck.remove(i)
  return [dealer,score]

def main():
  deck = ['3C', '3S', '8S', '3D', 'AC', '9H', 'QC', 'TD', 'TH', '8H', '8D', '7C', 'TS', '7D', 'AD', 'QD', 'KC', '6H', 'JH', 'KH', 'QS', '6C', '4H', '7H', '5S', '2S', 'AS', 'AH', '5C', '2D', '2H', '6D', 'TC', '4C', 'JS', 'JC', 'KD', '2C', '4S', '3H', '5H', '7S', 'KS', '5D', 'QH', '6S', '8C', '9D', 'JD', '9S', '9C', '4D']
  run1 = dealer(deck)
  assert dealer(deck) == [['3C', '3S', '8S', '3D'], 17, run1[2] ]
  run2 = dealer( run1[2] )
  assert dealer(run1[2]) == [['AC', '9H'], 20, run2[2] ]

if __name__ == "__main__":
  main()
