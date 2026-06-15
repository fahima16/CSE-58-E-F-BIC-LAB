text = input()
pattern = input()

length = len(pattern)

count = 0;

for i in range(len(text)-length+1):
    if(text[i:i+length] == pattern):
        count += 1

print(count)
