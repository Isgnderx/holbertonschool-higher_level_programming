#!/usr/bin/python3

def add_integer(a, b=98):
    sum = a + b
    return sum

if __name__ == "__main__":
    import doctest
    doctest.testmod()
