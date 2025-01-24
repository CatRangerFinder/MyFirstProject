#edit last number to change how precise it is
phase_root = round(3 ** 0.5, 4)

#calculates the watts using amps and voltage DC
def amps_to_watts_dc(amps,voltage):
    return amps * voltage

#calculates the watts using amps and voltage AC 1 phase
def amps_to_watts_ac1(amps,voltage,power_factor):
    return power_factor * amps * voltage

#calculates the watts using amps and voltage AC 3 phase (line to line)
def amps_to_watts_ac3l(amps,voltage,power_factor):
    stage1 = (amps * voltage)
    stage2 = (phase_root * power_factor)
    return stage1 * stage2

#start of script if run from here
if __name__ == '__main__':
    #this is how to calculate square root
    #print(round(3 ** 0.5, 3))

    amps1 = int(input('amps: '))
    voltage1 = int(input('voltage: '))
    print(amps_to_watts_ac3l(amps1,voltage1,1))