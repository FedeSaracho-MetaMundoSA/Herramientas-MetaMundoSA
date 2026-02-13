# CALCULADOR DE OBJETIVOS - METAMUNDO SA
# CEO: Federico Saracho

sueldo_objetivo_ars = 2000000
tipo_cambio = 1100 

objetivo_usd = sueldo_objetivo_ars / tipo_cambio

print(f"--- METAMUNDO SA: HOJA DE RUTA ---")
print(f"Objetivo mensual: ${objetivo_usd:.2f} USD")

# Calculamos cuántas horas necesitamos trabajar si cobramos 30 USD la hora
horas_necesarias = objetivo_usd / 30

print(f"Horas a trabajar (a $30/h): {horas_necesarias:.1f} hs")
print("¡MetaMundo en marcha! 🚀")
