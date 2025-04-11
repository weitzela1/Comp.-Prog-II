import sys
sys.setrecursionlimit(5000)
def sum(first, last):
    if first > last:
        return 0
    else:
        return first + sum(first + 3, last)
total = sum(3, 9669)
print("The sum of the multiples of 3, from 3 to 9669 is", total)
