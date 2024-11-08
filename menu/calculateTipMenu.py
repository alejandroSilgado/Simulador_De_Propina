from Formula.logic import calcular_propina, calcular_total_con_propina
import os

def design():
 opcion = 1
 while opcion: 
    print(f"""  
    =============================================
           calculo de propina
    =============================================""")
    total = float(input("    Ingrese el monto total de la cuenta: "))
    porcentaje = int(input("    Ingrese el porcentaje de propina (por ejemplo:10, 15, 20): "))
    propina = calcular_propina(total, porcentaje)
    total1 = calcular_total_con_propina(total, propina)
    print(f"""
    =============================================
    La propina calculada es: ${propina}
    El total a pagar es: $ {total1}
    =============================================
    """)
    opcion = int(input("/t¿Desea calcular otra propina? (1 = Si, 0 = No): "))
    os.system("clear")
