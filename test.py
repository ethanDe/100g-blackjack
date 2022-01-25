#!python3

utotal = [8,18]
def uValue(utotal):
    string = [str(integer) for integer in utotal]
    string3 = "".join(string)
    integer2 = int(string3)
    print(integer2)
    return integer2

print(utotal)
uValue(utotal)
