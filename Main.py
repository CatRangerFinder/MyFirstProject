#check limits
lower_mode_limit = 1
upper_mode_limit = 3

from Module import *

def print_screen1():
    print ('-----' * 14)
    print ('|',' ' * 4,'Please type the mode you want below valid options:',' ' * 10,'|' )
    print ('|',' ' * 66,'|' )
    print ('|',' ' * 4,"1. calculate watts with amps (DC)",' ' * 27,'|' )
    print ('|',' ' * 4,"2. calculate watts with amps (1 phase AC)",' ' * 19,'|' )
    print ('|',' ' * 4,"3. calculate watts with amps (3 phase line to line AC)",' ' * 6,'|' )
    print ('|',' ' * 66,'|' )
    print ('|',' ' * 66,'|' )
    print ('-----' * 14)

    selected_mode = int(input("Mode Selector: "))
    print('-----' * 14)
    #check to see if inputted mode is in range
    if lower_mode_limit > selected_mode:
        print('ERROR = Below mode limit')
    if upper_mode_limit < selected_mode:
        print('ERROR = Above mode limit')
    return selected_mode

selected_mode = print_screen1()

#starts function related to the selected mode
if selected_mode == 1:
    amps = int(input('Amount of Amps: '))
    voltage = int(input('Amount of Volts: '))
    watts = amps_to_watts_dc(amps,voltage)
    print('-----' * 14)
    print(f'Amount of watts is {watts}')
    input('\nPress enter to exit: ')

if selected_mode == 2:
    amps = int(input('Amount of Amps: '))
    voltage = int(input('Amount of Volts: '))
    power_factor = float(input('Expected power factor (1 to 0): '))
    watts = amps_to_watts_ac1(amps,voltage,power_factor)
    print('-----' * 14)
    print(f'Amount of watts is {watts}')
    input('\nPress enter to exit: ')

if selected_mode == 3:
    amps = int(input('Amount of Amps: '))
    voltage = int(input('Amount of Volts: '))
    power_factor = float(input('Expected power factor (1 to 0): '))
    watts = amps_to_watts_ac3l(amps,voltage,power_factor)
    print('-----' * 14)
    print(f'Amount of watts is {watts}')
    input('\nPress enter to exit: ')

