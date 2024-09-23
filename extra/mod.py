def isnum(val):
    try:
        int(val)
    except ValueError:
        return False
    else:
        return True
    
def isfloat(val):
    try:
        float(val)
    except ValueError:
        return False
    else:
        return True
    
def get_int(ask):
    while True:
        try:
            val = int(input(ask))
        except ValueError:
            continue
        else:
            return val