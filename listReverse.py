list = [1, 2, 3, 4, 5]
reverseList = [list[-i-1] for i in range(len(list))]
print(reverseList)