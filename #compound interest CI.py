#compound interest CI
#principle P
#rate R
#time T


P=float(input('enter the P amount:'))
R=float(input('enter the R OF interest:'))
T=float(input('enter the T in years:'))

CI=P*((1+R/100)**T)-P

print('the CI is :',CI)
