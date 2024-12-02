def f_to_c(f):
    return 5*(f-32)/9

fh=int(input("Enter temperature in F: "))
ce=f_to_c(fh)
print(f"{round(ce,2)} degree C")