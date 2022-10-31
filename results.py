import TLux_package


print(TLux_package.kaya_fct.__doc__)

germany_co2 = TLux_package.kaya_fct(82.4, 44, 5, 0.05)
germany_carbon = TLux_package.kaya_fct(82.4, 44, 5, 0.05, 'C')
print('CO2 emissions of Germany: ', germany_co2)
print('Carbon emissions of Germany: ', germany_carbon)