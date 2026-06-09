str = input()

rev = ""

for i in str:
    if i == 'A':
        rev = 'T' + rev
    elif i == 'T':
        rev = 'A' + rev
    elif i == 'C':
        rev = 'G' + rev
    elif i == 'G':
        rev = 'C' + rev
    
print (rev)
