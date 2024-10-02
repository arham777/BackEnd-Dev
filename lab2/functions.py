
bill= float(input("Enter Bill "))
rate = float(input('Enter Tax Rate'))

def calcTax(bill, taxRate):
  return (bill* taxRate)/100.00

print('Total Tax: ' ,calcTax(bill, rate))
