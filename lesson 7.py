'''try:
    try:
        ss = [1,2,3]
        print("122122")
        print(ss[10])
        print(10/0)
        print("222")
    except NameError:
        print("ABUBAKR")
    except ZeroDivisionError:
        print("ZERO!!!")
    except (IndexError, TypeError) as error:
        print("1.", error)
except:
    print("supererror.")
finally:
    print("kapec.")'''

class MyTypeError(Exception):
    def __init__(self, var=None):
        self.var = var
    def __str__(self):
        return f"Type [var] is {type(self.var)}!!!"

def checker(st):
    if type(st) != str:
        raise TypeError(f"Type [st] is {type(st)}!!")
    else:
        return st

var1 = "kriven"
var2 = 10.3
try:
    print(checker(var1))
except TypeError as error:
    print(error)