str= input()
str1 = input()
 
k= len(str)
k1 = len (str1)

for i in range(k1-k+1):
    if(str1[i:i+k] == str):
        print(i, end = " ")
