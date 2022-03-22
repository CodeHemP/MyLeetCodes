s=input('Enter a Roman number:')
print('Entered:',s)
ls1=list(s)
print('list is:',ls1)

ln=len(ls1)
tot_val=0
for i in range(0,ln):
    f_comb=0
    print('element is',ls1[i])
    #print('next is',ls1[i+1])
    a=ls1[i]
    if(i!=ln-1):
        b=ls1[i+1]
    else:
        b='U'
    if(a=='I' and b=='V'):
        val=4
        f_comb=1
        ls1[i+1]='U'
    elif(a=='I' and b=='X'):
        val=9
        f_comb=1
        ls1[i+1]='U'
    elif(a=='X' and b=='L'):
        val=40
        f_comb=1
        ls1[i+1]='U'
    elif(a=='X' and b=='C'):
        val=90
        f_comb=1
        ls1[i+1]='U'
    elif(a=='C' and b=='D'):
        val=400
        f_comb=1
        ls1[i+1]='U'
    elif(a=='C' and b=='M'):
        val=900
        f_comb=1
        ls1[i+1]='U'
    else:
        f_comb=0
        if(a=='I'):
            val=1
        elif(a=='V'):
            val=5
        elif(a=='X'):
            val=10
        elif(a=='L'):
            val=50
        elif(a=='C'):
            val=100
        elif(a=='D'):
            val=500
        elif(a=='M'):
            val=1000
        else:
            val=0
       
    tot_val=tot_val+val
    
    print(tot_val)
    
print('Final=',tot_val)
        
    


