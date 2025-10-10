y = [2, 6, 8, 13, 35, 89]
x: int = 0

def trigger(): 
  print('Lets playing with loop for:')
  print(f'Here the initial value of X is: {x}')

  for num in y: 
    res = num * 2
    print(f'{res}')

trigger()