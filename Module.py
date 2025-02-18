#Checks if power factor is in range
def check_power_factor(power_factor):
    if 1 < power_factor:
        print('ERROR = Power factor is above 1')
        exit(0)
    elif 0.001 > power_factor:
        print('ERROR = Power factor is below 0')
        exit(0)
    else:
        return power_factor

#Edit last number to change how precise it is (square root of 3)
phase_root = round(3 ** 0.5, 4)

##This is for all the calculating watts with amps options

#Calculates the watts using amps and voltage DC
def amps_to_watts_dc(amps,voltage):
    return amps * voltage

#Calculates the watts using amps and voltage AC 1 phase
def amps_to_watts_ac1(amps,voltage,power_factor):
    safe_power_factor = check_power_factor(power_factor)
    return safe_power_factor * amps * voltage

#Calculates the watts using amps and voltage AC 3 phase (line to line)
def amps_to_watts_ac3l(amps,voltage,power_factor):
    safe_power_factor = check_power_factor(power_factor)
    stage1 = (amps * voltage)
    stage2 = (phase_root * safe_power_factor)
    return stage1 * stage2


##This is for all the calculating amps with watts options

#Calculates the amps using watts and voltage DC
def watts_to_amps_dc(watts,voltage):
    return watts / voltage

#Calculates the amps using watts and voltage AC 1 phase
def watts_to_amps_ac1(watts,voltage,power_factor):
    safe_power_factor = check_power_factor(power_factor)
    return watts / (voltage * safe_power_factor)

#Calculates the amps using watts and voltage AC 3 phase (line to line)
def watts_to_amps_ac3l(watts,voltage,power_factor):
    safe_power_factor = check_power_factor(power_factor)
    return watts / (phase_root * safe_power_factor * voltage)


##Start of script if run from here (this is mostly for testing)
if __name__ == '__main__':

    amps1 = int(input('amps: '))
    voltage1 = int(input('voltage: '))
    power_factor1 = float(input('power factor: '))

    #print(check_power_factor(0.001))
    print(amps_to_watts_ac1(amps1,voltage1,power_factor1))