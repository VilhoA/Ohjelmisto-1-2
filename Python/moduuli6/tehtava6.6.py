import math

def price(diameter, price):
    r= diameter / 2
    area_sq_cm= math.pi * r **2
    price_cm= price
    price_sq_cm = price_cm / area_sq_cm
    price_sq_m=  price_sq_cm * 10000
    return price_sq_m

#print(price(20, 5))

pizza1= price ((float(input('syötä ensimmäisen pitsan halkaisija senttimetreinä: '))), (float(input('anna pitsan hinta: '))))
pizza2= price ((float(input('syötä toisen pitsan halkaisija senttimetreinä: '))), (float(input('anna pitsan hinta: '))))

print(f'pitsan 1 hinta per neliömetri: {pizza1:.2f} €')
print(f'pitsan 2 hinta per neliömetri: {pizza2:.2f} €')
print('')

if pizza1 < pizza2:
    print ('pitsa 1 on parempi vastine rahalle')
else:
    print ('pitsa 2 on parempi vastine rahalle')