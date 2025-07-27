a = 1
while a < 3:
    if a % 2 == 0:
        return  # Noncompliant: return used outside a function
    a += 1
