import sys
sys.setrecursionlimit(5000)

def fact_loop(n):
    product = 1
    for num in range(n, 0, -1):
        product *= num
    return product


def fact(n):
    if n <= 1: return 1 # base/ending case
    return n * fact(n-1) # recursive case


def main():
    num = int(input("Enter a number: "))
    while num != 0:
        num_fact = fact(num)
        print(f"{num}! = {num_fact}")

if __name__ == '__main__':
    main()
