#!python3
import x01_deck

def value(hand):
  
  value = []
  total = 0
  total2 = 0
  # card value
  face = ['J','K','Q','T']
  no = ['2','3','4','5','6','7','8','9']
  ex = ['A']
  extr = [1,11]
  for value in hand:
    if value[:1] in face:
      total = total + 10# add 10 to the total int(10)
      #return int(10)
    elif value[:1] in no:
      total = total + int(value[:1])#return int(value[:1])
    elif value[:1] in ex:
      total = total + 1
      total2 = total + 11


      #[int(1), int(11)]
  
  if total != :
    return [total, total2]
  else:
    return total

'''
  input:
  list hand: hand is a list of strings that contains the cards in the hand
  eg: ['AH','3D','4S']
  
  return:
  int the total value of the hand
  may return a list if the hand contains an Ace
  eg: [8,18]
  '''

print(value(['AD','QH']))

exit()



def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

if __name__ == "__main__":
  main()
