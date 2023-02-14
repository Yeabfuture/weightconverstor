weight = input('Your Weight: ')
unit = input('(L)bs or (K)g: ').lower()
if unit == 'l':
    weight_new = float(weight)*0.45
    new_unit = 'Kg'
else:
    weight_new = float(weight)*2.2
    new_unit = 'Lbs'
print(f'You are {weight_new} {new_unit}')