hrs = input("Enter Hours:")
h = float(hrs)
per = input("Enter the value per hour")
p = float(per)

if (h <= 40):
    print (h * p)
else:
    print(40 * p + (h-40)*1.5*p)
    
