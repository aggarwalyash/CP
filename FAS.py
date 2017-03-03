n = int(input())
list = [int(temp) for temp in input().strip().split(' ')]
count = 0
for i in range(n):
    for j in range(n-1):
        if(list[j]>list[j+1]):
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
            count += 1
print(count)
