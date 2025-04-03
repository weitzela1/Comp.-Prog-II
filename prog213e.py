from cl213e import FamStats


def main():
    try:
        ages = []
        percentages = []
        with open("Langdat/prog213e.dat", 'r') as f:
            for line in f:
                age = int(line)
                if age > 20:
                    ages.append(age)
                    for age in ages:
                    age.calc()
                    print(age)
    except OSError as e:
        print("Error:", e)
        pass



if __name__ == '__main__':
    main()




