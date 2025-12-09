str = "assfsfuh"
count = 0
for char in str:
    count = str.count(char)
    if count == 1:
        print(char)
        break

