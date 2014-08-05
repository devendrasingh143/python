#this is comment
t1 = 'a',
print(type(t1),'\n')


t = tuple('lupins')
print(t,'\n')


t = ('a', 'b', 'c', 'd', 'e')
print(t[0]) #print index-wise
print(t[1:3])
t = ('A',) + t[1:] #modification of tuple
print(t,'\n')


addr = 'monty@python.org'
uname, domain = addr.split('@') # spliting one word into two
print(uname)
print(domain,'\n')


t = divmod(7, 3) #fnx which retuurn two values at a time using tuples
print(t,'\n')


quot, rem = divmod(7, 3) #split tupleinto two objects
print(quot)
print(rem)


t = (7, 3)   # scatter 
print(divmod(*t),'\n') # passing two values by one object using *operator


s = 'abc'
t = [0, 1, 2]
print(zip(s, t),'\n')  #use of zip fnx, return iterator


t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:   #traverse a list of tuples
    print(number, letter)
