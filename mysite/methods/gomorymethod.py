from mysite.methods.simplex import simplex_v2

def gomory_method(m,c,b,cB,A,cR):
    z = simplex_v2(m,c,b,cB,A,cR)

    print(A)
    return z