from data.tip_storage import TipStorage
import os
from datetime import datetime

def design():
    storage = TipStorage()
    while True:
        print("""
        =============================================
                GESTIÓN DE PROPINAS
        =============================================
        1. Ver todas las propinas
        2. Agregar nueva propina
        3. Actualizar propina
        4. Eliminar propina
        5. Volver al menú principal
        =============================================
        """)
        
        option = int(input("Seleccione una opción (1-5): "))
        
        if option == 1:
            tips = storage.load_tips()
            for tip in tips:
                print(f"\nID: {tip['id']}")
                print(f"Monto: ${tip['monto']}")
                print(f"Propina: ${tip['propinaa']}")
                print(f"Total a Pagar: ${tip['montoTotalPagar']}")
                print(f"Porcentaje: {tip['porcentaje']}%")
                print("=====================")
                
        elif option == 2:
            total = float(input("Ingrese el monto total: "))
            porcentaje = int(input("Ingrese el porcentaje de propina: "))
            propina = total * (porcentaje/100)
            
            tip_data = {
                "total": total,
                "porcentaje": porcentaje,
                "propina": propina
            }
            
            storage.save_tip(tip_data)
            print("Propina guardada exitosamente!")
            
        elif option == 3:
            tip_id = input("Ingrese el ID de la propina a actualizar: ")
            total = float(input("Ingrese el nuevo monto total: "))
            porcentaje = int(input("Ingrese el nuevo porcentaje de propina: "))
            propina = total * (porcentaje/100)
            
            tip_data = {
                "total": total,
                "porcentaje": porcentaje,
                "propina": propina
            }
            
            storage.update_tip(tip_id, tip_data)
            print("Propina actualizada exitosamente!")
            
        elif option == 4:
            tip_id = input("Ingrese el ID de la propina a eliminar: ")
            if storage.delete_tip(tip_id):
                print("Propina eliminada exitosamente!")
            else:
                print("Error al eliminar la propina")
            
        elif option == 5:
            break
            
        input("\nPresione Enter para continuar...")
        os.system("clear") 