from kette import chain

@chain
def add3(x : int) -> int:
    return x+3

p = add3() & 10
print('p: %d' % p)
