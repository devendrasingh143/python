def do_twice(f,x):
    f(x)
    f(x)
def print_twice(y):
    print(y)
    print(y)
do_twice(print_twice,'string')    
