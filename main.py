from calc import calculate_speed
import numpy as np
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



def main():
    #start 
    oxygen = 0
    nuclear_fuel = 0
    # target
    SH = 504
    distance = 38
    
    dictance_to_target = 0
    SH_population = 8
    day = 0
    while dictance_to_target < distance and SH_population >= 8:
        nuclear_fuel_for_SH = 0
        nuclear_fuel_for_reactor = 0
        # nuclear_fuel_for_SH + nuclear_fuel_for_reactor <= nuclear_fuel
        Ship_mass = 192 + SH_population
        dictance_to_target -= calculate_speed(nuclear_fuel_for_reactor, Ship_mass)
        
        autoclave_temperature = sum(range(nuclear_fuel_for_SH + 1))
        
        if oxygen // 60 >= SH:
            oxygen_units = 60
        else:
            oxygen_units = oxygen // SH
            print("dead")
            break
        oxygen -= oxygen_units * SH_population
        growth_rate = np.sin(np.divide(np.pi, 2) + 
                      np.divide(np.pi*(autoclave_temperature + 0.5 * oxygen_units), 40))
        
        SH_population = SH_population * (growth_rate + 1 )
        
        
        
        

        day += 1
    pass

if __name__ == '__main__':
    main()