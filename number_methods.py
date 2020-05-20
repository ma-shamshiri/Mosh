import math

print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))

x = int(input("x = "))
y = x + 1
print(f"x = {x}, y = {y}")

print(type(x))

# Type Converting
# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy Values
# 0
# ""
# None

print(f"0 is interpreted as {bool(0)}")
print(f"-1 is interpreted as {bool(-1)}")
print(f"1 is interpreted as {bool(1)}")
print(f"5 is interpreted as {bool(5)}")
print(f"\"\" is interpreted as {bool('')}")
print(f"None is interpreted as {bool(None)}")
print(f"False is interpreted as {bool('False')}")
