rows=int(input("Number of rows: "))
pattern=input("Pattern: ").strip()
if len(pattern)>1:
    pattern=input("Pattern: ").strip()

print(f"{pattern} ".rjust((rows + 1) * 2 + 2))

for i in range(1,rows + 1):
    string= f"{pattern} " * i
    print(string.rjust((rows + 1) * 2) + f"{pattern} " + f"{pattern} " * i)

for i in range(rows + 1, -1, -1):
    if i != 0:
        string = f"{pattern} " * i
        print(string.rjust((rows + 1) * 2)+ f"{pattern} " + f"{pattern} " * i)

print(f"{pattern} ".rjust((rows + 1) * 2 + 2))