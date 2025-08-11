try:
    dataFrom= int(input("Enter a no "))
    ans = 10/dataFrom
except ValueError:
    print("Please Enter a valid value ")
except ZeroDivisionError : 
    print("we can not accept Zero as a Denomenator")
except Exception as ex : 
    print(ex)
else : 
    print(f"output is {ans}")
finally : 
    print("Conection is closed now")
    