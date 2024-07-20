def add(a, b):
    return a + b

print(add(1, 2)) # 3

# ================================
def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2)) # 3
# ================================
def add(a: int=10, b: int=20) -> int:
    return a + b

print(add()) # 30
print(add(1)) # 21
print(add(1, 2)) # 3

# ================================
add(1, 2)
add(a=1, b=2)