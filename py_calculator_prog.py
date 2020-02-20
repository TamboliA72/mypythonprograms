    #Program for the calculator Operation.....
#The different datatypes....
#c = 5
#b = 2.8
#d = "soumya"
#To print the datatypes of the variables
#print(c,"is of type: ",type(c))
#print(b,"is of type: ",type(b))
#print(d,"is of type: ",type(d))
#----------------------------------------------------------

print("Welcome to the calculator.....!")

a = float(input("Enter the 1st no: "))
b = float(input("Enter the 2nd no: "))

print("Choose:\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n"+"Enter your choice: ")
argument = input()
#print("a= {0} & b= {1}".format(a,b))
def switch_demo(argument):
    switcher = {
        1:      print("The addition is: "+str(a + b)),
        2:      print("The substraction is: "+str(a-b)),
        3:      print("The multiplication is: "+str(a*b)),
        4:      print("The division is: "+str(a/b)),
    }
    return switcher.get(argument, "nothing")

if __name__ == "__main__":
    print(switch_demo(argument))
