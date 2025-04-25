#Script check limits
lower_method_limit = 1
upper_method_limit = 2
lower_mode_limit = 1
upper_mode_limit = 3
#Import Modules required for the script
from Module import *


def print_screen_method():
    print(
        '----------------------------------------------------------------\n'
        '|     Please type the method you want below valid options:     |\n'
        '|                                                              |\n'
        '|     1. calculate watts using amps                            |\n'
        '|     2. calculate amps using watts                            |\n'
        '|                                                              |\n'
        '|                                                              |\n'
        '----------------------------------------------------------------'
        )


    selected_mode = int(input("Mode Selector: "))
    #Check to see if inputted method is in range
    if lower_method_limit > selected_mode:
        print('ERROR = Below method limit')
    if upper_method_limit < selected_mode:
        print('ERROR = Above method limit')
    return selected_mode

##Everything here is for the amps method
def print_screen_amps():
    print(
        '----------------------------------------------------------------\n'
        '|      Please type the mode you want below valid options:      |\n'
        '|                                                              |\n'
        '|      1. calculate watts with amps (DC)                       |\n'
        '|      2. calculate watts with amps (1 phase AC)               |\n'
        '|      3. calculate watts with amps (3 phase line to line AC)  |\n'
        '|                                                              |\n'
        '|                                                              |\n'
        '----------------------------------------------------------------'
        )

    selected_mode = int(input("Mode Selector: "))
    print('-----' * 14)
    #Check to see if inputted mode is in range
    if lower_mode_limit > selected_mode:
        print('ERROR = Below mode limit')
    if upper_mode_limit < selected_mode:
        print('ERROR = Above mode limit')
    return selected_mode

#Setup functions related to the "calculate watts with amps" method
def mode_response_amps():
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

##Everything here is for the watts method

def print_screen_watts():
    print(
        '----------------------------------------------------------------\n'
        '|    Please type the mode you want below valid options:        |\n'
        '|                                                              |\n'
        '|    1. calculate amps with watts (DC)                         |\n'
        '|    2. calculate amps with watts (1 phase AC)                 |\n'
        '|    3. calculate amps with watts (3 phase line to line AC)    |\n'
        '|                                                              |\n'
        '|                                                              |\n'
        '----------------------------------------------------------------'
        )


    selected_mode = int(input("Mode Selector: "))
    print('-----' * 14)
    #Check to see if inputted mode is in range
    if lower_mode_limit > selected_mode:
        print('ERROR = Below mode limit')
    if upper_mode_limit < selected_mode:
        print('ERROR = Above mode limit')
    return selected_mode

#Setup functions related to the "calculate amps with watts" method
def mode_response_watts():
    if selected_mode_watts == 1:
        watts = int(input('Amount of watts: '))
        voltage = int(input('Amount of Volts: '))
        amps = watts_to_amps_dc(watts,voltage)
        print('-----' * 14)
        print(f'Amount of amps is {amps}')

    elif selected_mode_watts == 2:
        watts = int(input('Amount of watts: '))
        voltage = int(input('Amount of Volts: '))
        power_factor = float(input('Expected power factor (1 to 0): '))
        amps = watts_to_amps_ac1(watts,voltage,power_factor)
        print('-----' * 14)
        print(f'Amount of amps is {amps}')

    elif selected_mode_watts == 3:
        watts = int(input('Amount of watts: '))
        voltage = int(input('Amount of Volts: '))
        power_factor = float(input('Expected power factor (1 to 0): '))
        amps = watts_to_amps_ac3l(watts,voltage,power_factor)
        print('-----' * 14)
        print(f'Amount of amps is {amps}')

    else:
        input('ERROR = There was a issue with your selection')


selected_method = print_screen_method()

if selected_method == 1:
    #Print calculate watts with amps selection
    selected_mode_amps = print_screen_amps()
    mode_response_amps()
    input('\nPress enter to exit: ')

elif selected_method == 2:
    #Print calculate amps with watts selection
    selected_mode_watts = print_screen_watts()
    mode_response_watts()
    input('\nPress enter to exit: ')
    pass