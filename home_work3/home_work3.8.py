s=0
sh=0
for i in range (int(1e6)):
    n1r= int(i%10)
    n2r= int((i%100)//10)
    n3r= int((i%1000)//100)

    n1l= int((i//1e3)%10)
    n2l= int((i//1e5)%10)
    n3l= int((i//1e5)%10)
    sr=n1r+n2r+n3r
    sl=n1l+n2l+n3l

    if sr==sl:
        s+=1
    elif n1l+n2l+n3l==13:
        sh+=1
    
print(f'{s}\n{sh}')
