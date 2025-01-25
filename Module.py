#edit last number to change how precise it is
phase_root = round(3 ** 0.5, 4)

#calculates the watts using amps and voltage DC
def amps_to_watts_dc(amps,voltage):
    return amps * voltage

#Check if power factor is in range
def check_power_factor(power_factor):
    if 1 < power_factor:
        print('ERROR = Power factor is above 1')
        exit(0)
    elif 0.001 > power_factor:
        print('ERROR = Power factor is below 0')
        exit(0)
    else:
        return power_factor

#calculates the watts using amps and voltage AC 1 phase
def amps_to_watts_ac1(amps,voltage,power_factor):
    safe_power_factor = check_power_factor(power_factor)
    return safe_power_factor * amps * voltage

#calculates the watts using amps and voltage AC 3 phase (line to line)
def amps_to_watts_ac3l(amps,voltage,power_factor):
    stage1 = (amps * voltage)
    safe_power_factor = check_power_factor(power_factor)
    stage2 = (phase_root * safe_power_factor)
    return stage1 * stage2

#start of script if run from here (this is mostly for testing)
if __name__ == '__main__':
    #this is how to calculate square root
    #print(round(3 ** 0.5, 3))

    amps1 = int(input('amps: '))
    voltage1 = int(input('voltage: '))
    power_factor1 = float(input('power factor: '))

    #print(check_power_factor(0.001))
    print(amps_to_watts_ac1(amps1,voltage1,power_factor1))