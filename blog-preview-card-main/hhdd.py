def get_name():
    name = input("Enter You name; ")
    print("Hello : " + name)

def get_age():
    age = int(input("Enter You age; "))

    if age >= 18:
        print("You are an adult")
        return True
    else:
        print("You are not an adult")
        return False

#

def get_puzzle():
    puzzle = int(input("Have a puzzle?"))
  
    if puzzle 