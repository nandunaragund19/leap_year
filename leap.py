import sys

def leapyear(year):
    if (year % 400 == 0):
        print("not leap year")
    else:
        print("leap year")

if __name__ == "__main__":
    year = int(sys.argv[1])
    print(leapyear(year))

    




    
    