from cl54c import Application
def main():
        try:
            num = int(input("Enter circle radius: "))
            app = Application(num)
            app.calc()
            app.show()

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
