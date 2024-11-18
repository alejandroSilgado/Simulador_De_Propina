import os
from menu.mainMenu import design as designOpcion
from menu.calculateTipMenu import design as designOpcion1
from menu.divideAmountsMenu import design as designOpcion2
from menu.thankYou import design as designOpcion3
from menu.manageTipsMenu import design as designOpcion4
from menu.searchTipsMenu import design as designOpcion5

while True:
    try:
        option = designOpcion()
        
        if option == 1:
            designOpcion1()
        elif option == 2:
            designOpcion2()
        elif option == 3:
            designOpcion4()
        elif option == 4:
            designOpcion5()
        elif option == 5:
            designOpcion3()
        
        if option == 5:
            break
            
    except ValueError:
        print("Ingrese un número válido")
    
    