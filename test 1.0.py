turn= 'yes'
while turn == 'yes':
    file = input("Would you want to creat a new file, or use an old one. new:0 old:1")
    joined="anything"
    lst=["0","1"]

    while file not in lst:
        file = input("invalid input try again")
        
    if file == "0":
        filename = open('Original.txt','w')
        writing = input(" Type the input you want")
        filename.write(writing)
        filename.close()
        filename= "Original.txt"
        
    elif file=="1":
        filename=input("enter the filename").title()+ ".txt"

    order1=input("Do you want to Encrypt or Decrypt your file. for Encrypt:0 , for Decrypt: 1, count:2")
    
##########
    def Ceaser (filename,wheresave,num,joined):
        f = open(filename,'r')
        answer = open(wheresave,'w')
        string =""
        for i in f:
            x=i.split()
            n=0
            for j in x:
                string+=(" ")
                n+=1
                m=0
                for z in j:
                    if z.isupper():
                        Q=chr(65+((ord(z)+(num-65))%26))
                    else:
                        Q=chr(97+((ord(z)+(num-97))%26))
                    string+=(Q)
                    m+=1
                    if n == len(x)and m == (len(j)):
                        string+=("\n")
        answer.write(string)
        if joined != "false":
            if num>0:
                print ("encrypted text:",'\n',string)
            else:
                print ("dicrypt text:",'\n',string)
        f.close()
        answer.close()
        return (answer)
###############
    
    def indexLocator (char,cipherKeyMatrix):
        indexOfChar = []
        if char == "J":
            char = "I"
        for i,j in enumerate(cipherKeyMatrix):
            for k,l in enumerate(j):
                if char == l:
                    indexOfChar.append(i) 
                    indexOfChar.append(k) 
        return indexOfChar
    
#############################
    
    def playfair (f,wheresave,n,key,joined):
        m = open(filename,'r')
        line = m.readlines()
        new = ' '.join([str(i) for i in line])
        f = new.replace(" ","").upper()
        lng=f.replace("\n","")
        f=lng
        answer = open(wheresave,'w')
        string=""
        for s in range(0,len(f)+1,2):
            if s<len(f)-1:
                if f[s] == f[s+1]:
                    f = f[:s+1]+'X'+f[s+1:]
        if len(f)%2 != 0:
            f = f[:]+'Q'
        matrix_5x5 = [[0 for i in range (5)] for j in range(5)]
        simpleKeyArr = []
        for c in key:
            if c not in simpleKeyArr:
                if c == 'J':
                    simpleKeyArr.append('I')
                else:
                    simpleKeyArr.append(c)

        is_I_exist = "I" in simpleKeyArr
        for i in range(65,91):
            if chr(i) not in simpleKeyArr:
                if i == 73 and not is_I_exist:
                    simpleKeyArr.append("I")
                    is_I_exist = True
                elif i == 73 or i == 74 and is_I_exist:
                    pass
                else:
                    simpleKeyArr.append(chr(i))
        index = 0
        for i in range(0,5):
            for j in range(0,5):
                matrix_5x5[i][j] = simpleKeyArr[index]
                index += 1

        keyMatrix = matrix_5x5
        i = 0
        while i < len(f):
            n1 = indexLocator(f[i],keyMatrix)
            n2 = indexLocator(f[i+1],keyMatrix)
            if n1[1] == n2[1]:
                i1 = (n1[0] + n) % 5
                j1 = n1[1]

                i2 = (n2[0] + n) % 5
                j2 = n2[1]
                string+=(keyMatrix[i1][j1]+keyMatrix[i2][j2])
            elif n1[0] == n2[0]:
                i1 = n1[0]
                j1 = (n1[1] + n) % 5

                i2 = n2[0]
                j2 = (n2[1] + n) % 5
                string+=(keyMatrix[i1][j1]+keyMatrix[i2][j2])
            else:
                i1 = n1[0]
                j1 = n1[1]

                i2 = n2[0]
                j2 = n2[1]
                string+=(keyMatrix[i1][j2]+keyMatrix[i2][j1])
            i += 2
        
        if n==-1:
            newstring=string
            for i in range(len(string)-2):
                i+=1
                if string[i]=="X" and string[i-1]==string[i+1]:
                    newstring=string[:i]+string[i+1:]
            if string[-1]=="Q":
                newstring=newstring[:len(newstring)-1]
            answer.write(newstring)

    
        else:
            answer.write(string)
        m.close()
        answer.close()
        if joined != "true":
            if n==-1:
                print("Decrypted text:",'\n',newstring)
            else:
                print("encrypted text:",'\n',string)
        return (answer)
###############
    
    def counter (filename):
        f = open(filename,'r')
        list2 = []
        count = 0
        letter = 0
        chara = 0
        num = 0
        list = [0 for i in range(26)]
        line = f.readlines()
        numlines = len(line)
        print(line)
        for i in line:
            x = i.split()
            o = len(x)-1
            num = num+o
            for j in x:
                count += 1
                list2.append("  ")
                for z in j:
                    chara += 1
                    if z.isalpha():
                        letter += 1
                        z = z.upper()
                        for m in range(26):
                           if (m+65) == ord(z):
                               list[m] += 1      
        f.close()
        print("number of lines:",numlines)
        print("number of words:",count)
        print("number of characters",chara+num)
        print("number of letters:",letter)
        print()
        for i in range(26):
            print ("The letter",chr(i+65),"occured",list[i])
        return (chara)
    
###############
    lst.append("2")
    while order1 not in lst:
        order1 = input("invalid input try again")
        
    if order1 == '0':
        type1 = input("Enter type of Encrypt Ceaser:0 , Playfair:1, joined:2")
        while type1 not in lst:
                type1=input("invalid input try again")
                
        wheresave='Ciphered.txt'
        n=1
        if type1 == '0':
            num = int(input("enter the ciphered shift"))
            Encrypt = Ceaser(filename,wheresave,num,joined)
        elif type1 =='1':
            key = input("enter the ciphere key").replace(" ","").upper()
            Encrypt = playfair (filename,wheresave,n,key,joined)
        elif type1 =='2':
            joined= "false"
            num = int(input("enter the ciphered shift"))
            key = input("enter the ciphere key").replace(" ","").upper()
            Encrypt = Ceaser(filename,wheresave,num,joined)
            filename='Ciphered.txt'
            Encrypt = playfair (filename,wheresave,n,key,joined)

    elif order1 == '1':
        type2 = input("Enter type of Decrypt Ceaser:0 , Playfair:1, joined:2")
        while type2 not in lst:
            type2=input("invalid input try again")
        wheresave='Deciphered.txt'
        n=-1
        if type2 == '0':
            num = int(input("enter the ciphered shift"))*(-1)
            Decrypt = Ceaser(filename,wheresave,num,joined)
        elif type2 == '1':
            key = input("enter the ciphere key").replace(" ","").upper()
            Decrypt = playfair (filename,wheresave,n,key,joined)
        elif type2 =='2':
            joined = "true"
            num = int(input("enter the ciphered shift"))*(-1)
            key = input("enter the ciphere key").replace(" ","").upper()
            Decrypt = playfair (filename,wheresave,n,key,joined)
            filename='Deciphered.txt'
            Decrypt = Ceaser(filename,wheresave,num,joined)
            
    elif order1 == '2':
        count = counter(filename)
    turn = input("would you like to continue , type 'yes'").lower()
print ("thank you for using my code")
