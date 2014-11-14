a = [5, 3, 10, 3, 5, 7, 90, 15]

def comparator_greater(x, y):
    if x > y:
        return -1
    elif x == y:
        return 0
    else:
        return 1

def cmp_to_key(comparator):
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __lt__(self, other):
            return comparator(self.value, other.value) == -1

    # return lambda x: MyClass(x)
    return MyClass

# x, y
# cmp_to_key(comparator_greater)(x) <?
# cmp_to_key(comparator_greater)(y)

a.sort(key=cmp_to_key(comparator_greater))
print(a)
