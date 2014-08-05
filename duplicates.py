a=[7,2,3,2,5]
a.sort()
print(a)

def has_duplicates(t):
    s=list(t)
    if(len(s)==len(set(a))):
        print('no')
    else:
        print('duplicates')
has_duplicates(a)       
    
    
