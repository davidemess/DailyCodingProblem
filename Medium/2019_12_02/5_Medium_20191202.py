#5 2019/12/02 Medium

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def returnA(a, b):
        return a
    return pair(returnA)

def cdr(pair):
    def returnB(a, b):
        return b
    return pair(returnB)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
