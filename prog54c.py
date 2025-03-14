from cl54c import Application
def main():
    try:
        rad1 = int(input("Enter radius of Circle: "))
        app = Application(rad1)
        app.calc()
        app.show() # perim, area

    except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
