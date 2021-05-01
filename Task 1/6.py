c = float(input('Cost of the meal:'))
print('Tax:', "%.2f" % (c*0.18))
print('Tip:', "%.2f" % (c*0.05))
print('Total:', "%.2f" %(c*0.18+c*0.05+c))