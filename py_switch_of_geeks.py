# Function to convert number into string
# Switcher is dictionary data type here
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    # get() method of dictionary data type returns value of passed argument if it is present otherwise 2nd will be passed
    return switcher.get(argument, "nothing")
 
# Driver program
if __name__ == "__main__":
    a = int(input("Enter 0 - 2 for the following arguments:"))
    argument = a
    print(numbers_to_strings(argument))
