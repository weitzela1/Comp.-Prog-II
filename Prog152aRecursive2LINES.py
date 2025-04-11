import sys
sys.setrecursionlimit(5000)
def sum(first, last):
    while first < last:
        return first + sum(first + 3, last)
    else:
        pass

total = sum(3, 9669)
print(total)
