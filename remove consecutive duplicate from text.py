def RemoveDuplicate(str1):
    if(len(str1) < 2):
        return

    j=0

    for i in range(len(str1)):
        if(str1[j]!=str1[i]):
            j+=1
            str1[j]=str1[i]

    j+=1
    str1=str1[:j]
    return str1

str1=input("Enter string=")
str1=list(str1.rstrip())
str1=RemoveDuplicate(str1)
print(str1)
