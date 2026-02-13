price_rice=45
price_sugar=40
price_oil=130
quantity_rice=3
quantity_sugar=2.5
quantity_oil=1.8
total_price_rice=price_rice*quantity_rice
total_price_sugar=price_sugar*quantity_sugar
total_price_oil=price_oil*quantity_oil
final_total_price=total_price_rice+total_price_sugar+total_price_oil
print("Total price of rice=",total_price_rice,'Rs')
print("Total price of sugar=",total_price_sugar,'Rs')
print("Total price of oil=",total_price_oil,'Rs')
print("Total price of all items=",final_total_price,'Rs')

final_total_price_int=int(final_total_price)
print('Total price as int=',final_total_price_int)
final_total_price_str=str(final_total_price)
print('Total price as string=',final_total_price_str)

import random
delivery_charge=random.randrange(5,10)

final_bill=final_total_price_int+delivery_charge
print('Final bill amount=',final_bill,'Rs')