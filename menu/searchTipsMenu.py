from data.tip_storage import TipStorage
import os

def design():
    storage = TipStorage()
    while True:
        print("""
        =============================================
                BÚSQUEDA DE PROPINAS
        =============================================
        1. Buscar por monto
        2. Ver todas las propinas
        3. Volver al menú principal
        =============================================
        """)
        
        option = int(input("Seleccione una opción (1-3): "))
        
        if option == 1:
            monto = float(input("Ingrese el monto a buscar: "))
            results = storage.search_by_date(monto)
            if results:
                print("\nResultados encontrados:")
                for tip in results:
                    print(f"\nID: {tip['id']}")
                    print(f"Monto: ${tip['monto']}")
                    print(f"Propina: ${tip['propinaa']}")
                    print(f"Total a Pagar: ${tip['montoTotalPagar']}")
                    print(f"Porcentaje: {tip['porcentaje']}%")
                    print("=====================")
            else:
                print("\nNo se encontraron resultados.")
        
        elif option == 2:
            tips = storage.load_tips()
            for tip in tips:
                print(f"\nID: {tip['id']}")
                print(f"Monto: ${tip['monto']}")
                print(f"Propina: ${tip['propinaa']}")
                print(f"Total a Pagar: ${tip['montoTotalPagar']}")
                print(f"Porcentaje: {tip['porcentaje']}%")
                print("=====================")
                
        elif option == 3:
            break
            
        input("\nPresione Enter para continuar...")
        os.system("clear")