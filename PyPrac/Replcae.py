number = "+49 (176) 123-4567"

print("Before:", number)
print("After:", number.replace("+", "00").replace(" ", "").replace("-", "").replace("(", "").replace(")", ""))
