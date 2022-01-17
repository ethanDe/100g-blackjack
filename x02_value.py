#!python3

def value(hand):
  '''
  input:
  list hand: hand is a list of strings that contains the cards in the hand
  eg: ['AH','3D','4S']
  
  return:
  int the total value of the hand
  may return a list if the hand contains an Ace
  eg: [8,18]
  '''
  value = []
  face = ['J','K','Q','10']
  no = ['1','2','3','4','5','6','7','8','9']
  ex = ['A']
  for i in hand:
    if value[:1] in face:
      return int(10)
    elif value[:1] in no:
      return int(value[:1])
    elif value[:1] in ex:
      return int(1) and int(11)



exit()
def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

if __name__ == "__main__":
  main()
