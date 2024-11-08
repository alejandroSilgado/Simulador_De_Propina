import os
from menu.mainMenu import design as designOpcion
from menu.calculateTipMenu import design as designOpcion1
from menu.divideAmountsMenu import design as designOpcion2
from menu.thankYou import design as designOpcion3 



while True:
    try:
        option = designOpcion()
        
        if option == 1:
            designOpcion1()

        elif option == 2:
            designOpcion2()
        
        elif option == 3:
            designOpcion3()
        
        break
    
        
    except ValueError:
        print(f"ingrese un numero valido")
    
    