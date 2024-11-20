while (1):
    try:
        m = int(input("m: "))
    except ValueError:
         continue
    else:
        break
    
E = m * (3 * 10**8)**2
print(E)
