text = input()

#k = int(input())
#d = int(input())

k, d = map(int, input().split())

#k, d = input().split()
#k = int(k)
#d = int(d)

letters = ['A', 'C', 'G', 'T']

pattern = [""] 

for i in range(k):
    new_pat = []
    for p in pattern:
        for ch in letters:
            new_pat.append(p + ch)
    pattern = new_pat

count = {}

for pat in pattern:
    total = 0

    for i in range(len(text)-k+1):
        mismatch = 0

        for j in range(k):
            if(pat[j] != text[i+j]):
                mismatch += 1

        if(mismatch <=d):
            total += 1

    count[pat] = total

max_count = max(count.values())
for pat in count:
    if(count[pat] == max_count):
        print(pat, end = " ")
