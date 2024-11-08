from Formula.logic import calcular_propina, calcular_total_con_propina, dividir_total
import os

def design():
    opcion = 1
    while opcion:
        print(f""" 
        =============================================
         Dividir Cuenta entre Varias Personas
        ============================================= """)
        total = float(input("Ingrese el monto total de la cuenta: "))
        porcentaje = int(input("Ingrese el porcentaje de propina (por ejemplo: 15): "))
        personas = int(input("Ingrese el número de personas: "))
        propina = calcular_propina(total, porcentaje)
        totalMaspropina = calcular_total_con_propina(total, propina)
        print(f"""
        =============================================
        La propina calculada es: $ {propina}
        El total a pagar es: $ {totalMaspropina}
        Monto por persona: $ {dividir_total(totalMaspropina, personas)}
        =============================================  
        """)
        opcion = int(input("deseas calcular nuevamente? (1 = Si, 0 = NO): "))
        os.system("clear")