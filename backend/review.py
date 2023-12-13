# l = [i**2 for i in range(100) if i%2==1]
# l = {i: i**2 for i in range(100) if i%2==1}
# print(l)

def gen_dig():
    i = 0
    while True:
        yield i
        i+=2
    return i

def decorator(arg):
    def wrapper_for_args(func):
        def wrapper(*args, **kwargs):
            print(arg)
            print("dec")
            func(*args, **kwargs)
        return wrapper
    return wrapper_for_args

@decorator(arg=10)
def print_dig(a):
    print(a)

class Temprature:
    def __init__(self, gradus):
        self.gradus = gradus

    @property
    def gradus(self):
        return self._gradus

    @gradus.setter
    def gradus(self, gradus: float) -> None:
        if gradus >= -273:
            self._gradus = gradus
            return
        raise ValueError

    def __gt__(self, other):
        return self._gradus > other.gradus

if __name__ == '__main__':
    temp1 = Temprature(-3)
    temp2 = Temprature(-100)
    print(temp1>temp2)