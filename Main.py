from Module import *
from Cli import print_screen1
#import tkinter
#import customtkinter

interface_mode = int(input('input 0 for GUI and 1 for terminal use: '))
if interface_mode == 1:
    print('Starting terminal')
    selected_mode = print_screen1()
else:
    #todo finish making GUI
    print('Starting GUI')
    exit(0)

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

