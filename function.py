def do_twice(f,x):
    f(x)
    f(x)
def print_spam(y):
    print(y)
do_twice(print_spam,2)    
