horas = float(input('\nIngrese horas: '))
tarifa = float(input('\nIngrese tarifa por horas: '))

sueldo_bruto = 40 * tarifa
 
horas_extra = (horas - 40) * (tarifa * 1.5)

sueldo_final = sueldo_bruto + horas_extra

print(sueldo_final)
