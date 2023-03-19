from calc import calculate_speed
import numpy as np
from time import sleep
"""
Перед стартом полёта закупочные цены таковы, что 10 единиц кислорода стоят столько же, 
сколько 7 единиц ядерного топлива. 2 единицы кислорода стоят 14 кредитов.
=>  1 единица кислорода = 7  кредитов
    10 единиц кислорода = 7 единиц ядерного топлива = 70 кредитов

Каждый день полёта мощность реактора можно направить на двигатель 
и на выработку электрической энергии. 

Каждая расходуемая единица ядерного топлива в день даёт 1% вырабатываемой мощности 
от максимальной. 
1 единица ядерного топлива = 1% максимальной мощности 


действительная максимальная мощности = 80 %
=> максимум 80 единица ядерного топлива за день

Из-за конструктивных особенностей больше 80 % максимальной мощности реактора
направить на двигатель не получится.

Каждый процент мощности реактора, направленный на выработку электроэнергии, 
приносит 11 единиц электроэнергии в день. 
=> 11 единиц электроэнергии = 1% максимальной мощности 

Электроэнергия не запасается, 
неизрасходованная энергия в конце дня утекает в пространство.
    
    
"""

slow_T = 20

def calc_mission(target_SH, distance):
    #start 
    oxygen = 0
    nuclear_fuel = 0
    # target
    #target_SH = 504
    #distance = 38
    
    dictance_to_target = 0
    SH_population = 8
    days = np.log2(target_SH) - 2
    print(days)
    need_oxygen = 0
    
    distance//2 - days
    day = 0
    speed_day = distance//2 - days 
    while dictance_to_target < distance:
        nuclear_fuel_for_SH = 36 // 11 + (36 % 11 == 0)
        autoclave_temperature = 10
        nuclear_fuel_for_reactor = 80
        # nuclear_fuel_for_SH + nuclear_fuel_for_reactor <= nuclear_fuel
        Ship_mass = 192 + SH_population
        speed = calculate_speed(nuclear_fuel_for_reactor, Ship_mass)
        print(speed)
        dictance_to_target += int(speed) + 1
        if speed <= 1 or SH_population >= target_SH:
            autoclave_temperature = 21
            nuclear_fuel_for_SH = 20
        if speed_day <= day:
            autoclave_temperature = 8
        nuclear_fuel_for_SH = sum(range(autoclave_temperature + 1))
        oxygen_units = 60
        oxygen -= oxygen_units * SH_population
        
        need_oxygen += oxygen_units * SH_population
        growth_rate = np.sin(
                        ((-np.pi) / 2) * 
                        ((np.pi*(autoclave_temperature + 0.5 * oxygen_units)) / 40))
        
        SH_population = SH_population * (float(growth_rate) + 1 )
        
        nuclear_fuel += nuclear_fuel_for_SH + nuclear_fuel_for_reactor
        #nuclear_fuel += 84
        print(need_oxygen, dictance_to_target, int(SH_population))
        sleep(1)
    print(need_oxygen, nuclear_fuel, dictance_to_target, int(SH_population)*2)
    return need_oxygen, nuclear_fuel

if __name__ == '__main__':
    calc_mission(504, 36)