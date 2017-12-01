from fractions import Fraction
ct=0
x=Fraction(3,2)
for i in range(1000):
    y=1/(Fraction(1,1)+x)+Fraction(1,1)
    x=y
    if(len(str(y.numerator))>len(str(y.denominator))):
        ct=ct+1
print(ct)
