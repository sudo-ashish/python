nnumber = int(input("enter num to see the sum of all even number: "))
even_sum = 0

for i in range(0, nnumber+1):
    if i%2 == 0:
        even_sum = even_sum + i

print("sum is: ", even_sum)

