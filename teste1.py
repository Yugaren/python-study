def test_variables():
    a = "abc" # string str
    b = 123 # integer int
    c = 123.456 # float
    d = False # boolean bool
    e = [] # list
    f = {} # dictionary dict

    print(a) 
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

    print(type(a)) 
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f)) 

def test_function(arg1, arg2):
    print(arg1)
    print(arg2)
   
# my_func = test_variables 
# my_func()

test_function(123, "feijao")
test_function("qualquer", 345)
