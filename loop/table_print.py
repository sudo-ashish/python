num = int(input("ente r the number to print table: "))

for i in range(0, 11):
    if i == 5:
        continue
    else:
        print(num," * ",i," = ",num*i)
