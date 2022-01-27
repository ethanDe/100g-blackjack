#!python3

def value(hand):
  
  value = []
  total = 0
  total2 = 0
  face = ['J','K','Q','T']
  no = ['2','3','4','5','6','7','8','9']
  ex = ['A']
  for value in hand:
    if value[:1] in face:
      total = total + 10
      total2 = total2 + 10
    elif value[:1] in no:
      total = total + int(value[:1])
      total2 = total2 + int(value[:1])
    elif value[:1] in ex:
        total = total + 1
        total2 = total2 + 11
    
  if total2 == total:
    return total
  else:
    utotal = [total, total2]
    return utotal

def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

if __name__ == "__main__":
  main()
