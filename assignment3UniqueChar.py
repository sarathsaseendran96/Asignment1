  



# check unique charecters in a string

def has_unique_char(s):

    for i in range(len(s)):

        for j in range(i+1,len(s)):
            
            if s[i]==s[j]:

                return False

    return True

s=input("enter a string  :")        

print(has_unique_char(s))