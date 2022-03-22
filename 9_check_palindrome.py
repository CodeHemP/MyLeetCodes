

x=121

y=str(x)

print(y)

z=list(y)

print(z)

ln=len(z)
print(ln)

flag=0

if(ln%2!=0):
    print('odd')
    midp=ln//2
    print('Midpoint=',midp)
    for i in range(0,midp):
        print(z[i])
        print(z[i+midp])
        print(ln-1-i)
        if(z[i]==z[ln-1-i]):
            print('Match',i)
        else:
            print('MISMATCH from odd')
            raise TypeError("Not a Palindrome")
            flag=1

elif(ln%2==0):
    print('Even')
    comparisons_no=ln/2
    for i in range(0,int(comparisons_no)):
        print(i)
        if(z[i]==z[ln-1-i]):
            print('Match',i)
        else:
            print('MISMATCH from even')
            raise TypeError("Not a Palindrome")
            flag=1



    

if(flag==0):
    print('String is Palindrome !')

        
    
