
#Addition
def addition(x, y):
    return x + y


#Subtraktion
def subtraktion(x, y):
    return x - y


#Multiplikation
def multiplikation(x, y):
    return x * y


#Division
def division(x, y):
    return x / y


print("Welche mathematische Operation möchten Sie durchführen?")
print("1.Addition")
print("2.Subtraktion")
print("3.Multiplikation")
print("4.Division")

while True:

    choice = input("(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Erste Zahl: "))
        num2 = float(input("Zweite Zahl: "))

        if choice == '1':
            print(num1, "+", num2, "=", addition(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtraktion(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplikation(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))


        next_calculation = input("Möchten Sie weitere Operationen durchführen? (ja/nein): ")
        if next_calculation == "nein":
            break

    else:
        print("Invalid Input")