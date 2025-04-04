from cl213e import FamStats
def main():
    g1 = 0
    g2 = 0
    g3 = 0
    g4 = 0
    g5 = 0
    total = 0

    try:
        nums = [17, 80, 79, 60, 21, 20, 1, 39, 40, 59, 61, 4, 16, 47, 61, 4, 16, 47, 52, 35, 54, 85, 21, 15, 48, 49, 50]
        for num in nums:
            if num < 20:
                g1 += 1
            elif num >= 20 and num < 40:
                g2 += 1
            elif num >=40 and num < 60:
                g3 += 1
            elif num >= 60 and num < 80:
                g4 += 1
            elif num >= 80:
                g5 += 1
            else:
                pass
            total = g1 + g2 + g3 + g4 + g5
        print("The amount of people <20:", g1)
        print("The amount of people 20-39:", g2)
        print("The amount of people 40-59:", g3)
        print("The amount of people 60-79:", g4)
        print("The amoutn of people over 80:", g5)

    except OSError as e:
        print("Error:", e)
    pass



if __name__ == '__main__':
    main()




