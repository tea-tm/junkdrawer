def find_gold(mine):
  for ore in range(len(mine)):
    if type(mine[ore]) == list:
      print('Digging.')
      find_gold(mine[ore])
      print('Going back.')
    elif mine[ore] == "coal":
      print('.')
    elif mine[ore] == "gold":
      print('Yee Haw! I\'m rich!') 
    

find_gold(["coal", "coal", ["coal","coal"], [[["coal"]]], ["coal", ["gold", "coal"]]])

def add_digits(num):
  sum = 0
  while num > 0:
    sum += num%10
    num = num//10
  return sum
