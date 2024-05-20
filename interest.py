# take principal (p), Period (N), rae of interest (R) %.a.and
P = float(input('Please enter Principal in INR:  '))
N = float(input('Please enter period in Years : '))
R = float (input('Please enter rate of iterest in %.p.a: '))

# Calculate Simple Intrest
I = (P*N*R)/100

# Calculate Amount
A = P + I 

# Print above results
print(f'Simple Intrest for given values is {I:.2f} INR')
print(f'Amount is {A:.2f} INR')