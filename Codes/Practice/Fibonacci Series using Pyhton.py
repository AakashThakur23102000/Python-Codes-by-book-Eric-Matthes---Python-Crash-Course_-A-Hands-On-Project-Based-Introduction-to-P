#do fabonacci series till 10      0 1 1 2 3 5 8 13 21 34
count = int(input("Enter the no of rounds you want output - "))

i = 0
j = 1
sum = 0
for rn in range(count):
    
    print(sum)
    i = j
    j = sum
    sum = i + j
