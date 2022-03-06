list_1=[3,7,5,4]
mn=min(list_1)
mx=max(list_1)
print('minimum', mn)
print('maximum', mx)

sum1=0
for i in range(mn,mx+1):
    print('i=',i)
    sum1=sum1+i
print('Total sum=',sum1)

sum2=0
for j in list_1:
    sum2=sum2+j
    
print('Actual sum=',sum2)

print('Missing number=',sum1-sum2)

