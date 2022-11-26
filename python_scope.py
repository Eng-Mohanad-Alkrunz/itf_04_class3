import builtins

a = 40

def outer_function():
    c = 30 # local variable
    d = 50
    # global a
    print("a from outer_function before modified",globals()['a'])
    globals()['a'] = 60
    a = 20
    builtins.print()

    def inner_function():
        b = 30
        a = 30
        print("a from inner function",a)

    inner_function()
    print("a from outer_function", a)

outer_function()
print("a from global scope",a)