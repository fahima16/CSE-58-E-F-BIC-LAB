str = input()

num= int(input())   

count = {}

length = len(str)

for i in range(length - num + 1):
    substr = str[i:i+num]
    if substr in count:
        count[substr] += 1
    else:
        count[substr] = 1

max_count = max(count.values())

for substr in count:
    if count[substr] == max_count:
        print (substr, end=" ")
