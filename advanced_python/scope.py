var1 = "I'm a global variable"
var2 = "I'm also a global variable"

def scope_test():
    var3 = "I'm either an enclosing or local variable"
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"
        
    def print_variables():
        var1 = "I'm a local variable"
        print("Inside print_variables, var1 is:", var1)
        print("Inside print_variables, var2 is:", var2)
        print("Inside print_variables, var3 is:", var3, "\n")

    spam = "test spam"
    do_local()
    print("After local assignment, spam is:", spam)
    do_nonlocal()
    print("After nonlocal assignment, spam is:", spam)
    do_global()
    print("After global assignment, spam is:", spam, "\n")
    
    print_variables()
    print("Inside scope_test, var1 is:", var1)
    print("Inside scope_test, var2 is:", var2)
    print("Inside scope_test, var3 is:", var3, "\n")

scope_test()
print("In global scope:", spam)
print("In global scope, var1 is:", var1)
print("In global scope, var2 is:", var2)
try:
    print("In global scope, var3 is:", var3)
except Exception as e:
    print("In global scope, var3 is not defined")
    print("Error:", e)
