degree = float(input("Enter temperature: "))
unit=input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  print (f"{degree}° in Fahrenheit is equivalent to {(degree-32)/1.8}° Celsius.")
elif unit == "C" or unit == "c":
  print (f"{degree}° in Celsius is equivalent to {1.8*degree+32}° Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")



 