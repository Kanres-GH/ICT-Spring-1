a = int(input('Deposit:'))
print('Savings after 1 year:', "%.2f" %(a*0.04+a), '$')
print('Savings after 2 years:', "%.2f" %((a*0.04+a)*0.04+(a*0.04+a)), '$')
print('Savings after 3 years:', "%.2f" %(((a*0.04+a)*0.04+(a*0.04+a))*0.04+((a*0.04+a)*0.04+(a*0.04+a))), '$')