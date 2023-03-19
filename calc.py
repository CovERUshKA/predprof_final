import numpy as np

speed_max = 2 # максимальная скорость корабля, равная 2 световых года в день;
Reactor_power = 0


def calculate_speed(Reactor_power, Ship_mass):
    return 2 * (Reactor_power/ 80) * (200/Ship_mass)

def calculate_growth_rate(autoclave_temperature, oxygen, SH):
    if oxygen // 60 >= SH:
        oxygen_units = 60
    else:
        oxygen_units = oxygen // SH
        return "dead"
    return  np.sin((np.pi/ 2) + 
                   (np.pi*(autoclave_temperature + 0.5 * oxygen_units)/ 40))

def calculate_new_population(old_population, growth_rate):
    return old_population + old_population * growth_rate

""" Температура в автоклаве должна быть в пределах от 0 до 30 градусов Цельсия """
def calculate_amount_of_electricity(maintain_temperature):
    return sum(range(maintain_temperature + 1)) # проверить!!!!!

""" 
    Весь кислород находящийся в автоклаве распределяется равномерно между единицами SH. 
    Одна единица SH не может усвоить более 60 единиц кислорода. 
    Минимальная популяция SH в автоклаве 8 единиц, меньшие популяции мгновенно вымирают.
"""

def calculate_day(target_SH):
    return np.log2(target_SH) - 2



def main():
    
    
    pass
if __name__ == '__main__':
    main()