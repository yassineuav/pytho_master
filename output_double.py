var = int(input('Enter Start balance: '))

print("times  balance")
for i in range(11):
  balance = "{:,}".format(var)
  print(f'{i}    ${balance}')
  var = var *2
