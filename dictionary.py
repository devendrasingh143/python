eng2sp = dict()
eng2sp['a', 's', 'd']=['z', 'x', 'c']
print(eng2sp)


eng2sp = dict()
eng2sp={'one': 'uno', 'two': 'dos', 'three': 'tres'}
print('\n')
print(eng2sp)
print(len(eng2sp)) #number of keys
print('one' in eng2sp) #it tells whether something appears as a key in the dictionary.
print('uno' in eng2sp)
vals = eng2sp.values()
print('uno' in vals)  #it tells whether something appears as a value in the dictionary.



def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram('brontosaurus')
print('\n')
print(h)
print(h.get('a'))
print(h.get('u', 0))



def print_hist(h):
    for c in h:
        print(c, h[c])
h = histogram('parrot')
print('\n')
print_hist(h)




def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
   # raise ValueError
h = histogram('parrot')
print('\n')
k = reverse_lookup(h, 2)
print(k)
#l = reverse_lookup(h, 3)
#print(l)


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
hist = histogram('parrot')
print('\n')
print(hist)
inverse = invert_dict(hist)
print(inverse)


verbose = True
def example1():
    if verbose:
        print('\nRunning example1')
example1()




