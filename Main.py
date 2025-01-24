#calculates the watts using amps and voltage DC
def amps_to_watts_dc(amps,voltage):
    return amps * voltage

#calculates the watts using amps and voltage AC 1 phase
def amps_to_watts_AC1(amps,voltage,power_factor):
    return power_factor * amps * voltage




amps1 = int(input('amps: '))
voltage1 = int(input('voltage: '))

print(amps_to_watts_dc(amps1,voltage1))