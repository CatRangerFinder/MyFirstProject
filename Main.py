#check limits
lower_method_limit = 1
upper_method_limit = 2
lower_mode_limit = 1
upper_mode_limit = 3

from Module import *


def print_screen1():
    print ('-----' * 14)
    print ('|',' ' * 4,'Please type the method you want below valid options:',' ' * 8,'|' )
    print ('|',' ' * 66,'|' )
    print ('|',' ' * 4,"1. calculate watts using amps",' ' * 31,'|' )
    print ('|',' ' * 4,"2. calculate amps using watts (nonfunctional)",' ' * 15,'|' )
    print ('|',' ' * 66,'|' )
    print ('|',' ' * 66,'|' )
    print ('-----' * 14)

    selected_mode = int(input("Mode Selector: "))
    print('-----' * 14)
    # check to see if inputted mode is in range
    if lower_method_limit > selected_mode:
        print('ERROR = Below method limit')
    if upper_method_limit < selected_mode:
        print('ERROR = Above method limit')
    return selected_mode

def print_screen2():
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

#setup functions related to the "calculate watts with amps" mode
def mode_response():
    if selected_mode_amps == 1:
        amps = int(input('Amount of Amps: '))
        voltage = int(input('Amount of Volts: '))
        watts = amps_to_watts_dc(amps,voltage)
        print('-----' * 14)
        print(f'Amount of watts is {watts}')

    elif selected_mode_amps == 2:
        amps = int(input('Amount of Amps: '))
        voltage = int(input('Amount of Volts: '))
        power_factor = float(input('Expected power factor (1 to 0): '))
        watts = amps_to_watts_ac1(amps,voltage,power_factor)
        print('-----' * 14)
        print(f'Amount of watts is {watts}')

    elif selected_mode_amps == 3:
        amps = int(input('Amount of Amps: '))
        voltage = int(input('Amount of Volts: '))
        power_factor = float(input('Expected power factor (1 to 0): '))
        watts = amps_to_watts_ac3l(amps,voltage,power_factor)
        print('-----' * 14)
        print(f'Amount of watts is {watts}')

    else:
        input('ERROR = There was a issue with your selection')


selected_method = print_screen1()

if selected_method == 1:
#print calculate watts with amps selection
    selected_mode_amps = print_screen2()
    mode_response()
    input('\nPress enter to exit: ')
#in the future this will be to calculate the amps using watts
elif selected_method == 2:
    print('Empty')