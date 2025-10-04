x: int

def increment_more():
  res: int = 0
  while res < 100:
    res += 1
    if (res % 2 == 0):
      print(f'Número par => {res}')  
    else:
      print(f'Número ímpar => {res}')

increment_more()