'''Read in a Fahrenheit temperature. Calculate and display
 the equivalent centigrade temperature. The following 
 formula is used for the conversion: C = (5 / 9) * (F – 32)'''
def fahrenheit_to_celsius(F):
    C = (5/9)*(F - 32)
    return C
F = float(input("Fahrenheit temperature: "))
print("Conversion: ",fahrenheit_to_celsius(F))
