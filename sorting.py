a=[2,70,4,36,76,99,22,344,2,100,6700,2323,3,44,56,332,556,432,77,333334,544]
for i in range(0,len(a)):
    for j in range(i+1, len(a)):
        if(a[i]>a[j]):
            a[i], a[j]=a[j], a[i]
            print(a)
            
            

print(a)
