import string, random
def genPass(num):
    upper_ = string.ascii_uppercase
    lower_ = upper_.lower()
    special_ = ['!','",','£','$','%','^','&','*','(',')','_','+','-']
    char = []
    pword = []
    password = ""
    for i in upper_:
        char.append(i)
    for i in lower_:
        char.append(i)
    for i in range(0,10):
        char.append(i)
    for i in special_:
        char.append(i)
    for i in range(0,num+1):
        ran = random.randrange(0,len(char))
        pword.append(char[ran])
    for i in pword:
        password += str(i)
    print(password)
    
for i in range(10):
    genPass(8)        
