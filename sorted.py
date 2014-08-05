a=['c','b','a']

def is_sorted(t):
    res=list(t)
    t.sort()
    #print(t)
    if(res==t):
        print('true')
    else:
        print('false')
is_sorted(a)
    
