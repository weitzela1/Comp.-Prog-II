from cl311 import Application
def main():
        try:
            des2 = int(input("Enter the amount of time spent Designing: "))
            cod2 = int(input("Enter amount of time spent Coding: "))
            debug2 = int(input("Enter amount of time spent Debugging: "))
            test2 = int(input("Enter amount of time spend Testing: "))
            app = Application(des2, cod2, debug2, test2)
            app.calctotal()
            app.calcpercent()
            app.show()



        except Exception as e:
            print("Error:", e)



if __name__ == "__main__":
    main()



