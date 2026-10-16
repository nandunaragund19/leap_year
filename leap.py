import sys

def leapyear(year):
    if (year % 400 == 0):
        print("leap year")
    else:
        print("not a leap year")

if __name__ == "__main__":
    year = int(sys.argv[1])
    print(leapyear(year))

    




    
    