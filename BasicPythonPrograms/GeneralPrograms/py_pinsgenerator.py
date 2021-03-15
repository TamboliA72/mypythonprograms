#python Program for Converting PIN's to easy to remember words

print("Welcome")
num = input("Enter the number you want to conver: ")
vowelList = ["a","e","i","o","u"]
consoList = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","y","z"]
num = int(num)
num1 = num
word = ""
#modulous by 100 to get the last two digits
while num > 0:    
    remainder = num%100
    num //= 100
    vowelNum = remainder % 5
    consoNum = remainder // 5
    word = consoList[consoNum] + vowelList[vowelNum] + word
print("Encoding of " + str(num1) + " is: " + word)
    

