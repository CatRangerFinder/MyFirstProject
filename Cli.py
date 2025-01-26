from variable import lower_mode_limit, upper_mode_limit


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


#testing use only
if __name__ == '__main__':
    print(print_screen1())