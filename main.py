total1 = 0
for number in range (2,101,2):  # go up by 2 every time
  total1 += number
print(total1)  # 2550

total2 = 0
for number in range (1,101):
  if number % 2 == 0 :
   total2 += number
print(total2)    # result is the same total1 : 2550
