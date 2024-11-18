### 

[TOC]

El proyecto **Simulador de Propina** es una aplicación simple de consola que permite calcular la cantidad de propina que debe dejarse en un restaurante, basada en el monto total de la cuenta y el porcentaje de propina seleccionado por el usuario. Además, el programa puede mostrar el total a pagar (con la propina incluida) y distribuir el pago entre un número de personas si el usuario lo desea.

# Problema

Cuando vamos a un restaurante, a menudo se nos presenta la necesidad de calcular la propina que dejamos a los camareros. Aunque algunas veces los restaurantes incluyen automáticamente la propina en la cuenta, en muchos casos el cliente tiene que calcularla por su cuenta. Además, la cantidad de propina puede variar dependiendo del servicio recibido (por ejemplo, 10%, 15%, o 20%). Este proyecto tiene como objetivo facilitar ese cálculo y ayudar a los usuarios a determinar el monto de la propina, el total a pagar y cómo dividirlo entre varios comensales.



# Funciones principales:

1. **Ingreso del monto total de la cuenta:**
   - El programa permite al usuario ingresar el monto total de la cuenta del restaurante.
2. **Selección del porcentaje de propina:**
   - El usuario puede seleccionar el porcentaje de propina que desea dejar (por ejemplo, 10%, 15%, 20%).
3. **Cálculo de la propina:**
   - Con el monto total y el porcentaje seleccionado, el programa calcula el valor de la propina.
4. **Cálculo del total a pagar:**
   - El programa suma el monto de la propina al total de la cuenta para mostrar el total que el usuario debe pagar.
5. **División del total entre varias personas:**
   - El programa permite al usuario ingresar la cantidad de personas que van a pagar la cuenta.
6. **Gestión de registros de propinas:**
   - Permite guardar, ver, actualizar y eliminar registros de propinas anteriores.
7. **Búsqueda de propinas:**
   - Facilita la búsqueda de propinas anteriores por monto o fecha.

# Funciones específicas:

1. **`calcular_propina(total, porcentaje)`**:
   - Entrada: monto total de la cuenta y porcentaje de propina.
   - Salida: monto de la propina.
2. **`calcular_total_con_propina(total, propina)`**:
   - Entrada: monto total de la cuenta y monto de la propina.
   - Salida: total a pagar (con la propina incluida).
3. **`dividir_total(total, personas)`**:
   - Entrada: monto total (con propina) y número de personas.
   - Salida: monto que le corresponde a cada persona.
4. **Sistema de almacenamiento:**
   - Guarda los registros de propinas en formato JSON.
   - Permite operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
   - Facilita la búsqueda de registros históricos.

# Menú Principal Simulador de Propina

```bash
=============================================
           SIMULADOR DE PROPINA
=============================================
1. Calcular propina y total a pagar
2. Calcular total a pagar divido entre varias personas
3. Gestionar registros de propinas
4. Buscar propinas
5. Salir
=============================================
Por favor, elige una opción (1-5):
```

## **Si el usuario elige la opción 3 (Gestionar registros):**

```bash
=============================================
        GESTIÓN DE PROPINAS
=============================================
1. Ver todas las propinas
2. Agregar nueva propina
3. Actualizar propina
4. Eliminar propina
5. Volver al menú principal
=============================================
```

## **Si el usuario elige la opción 4 (Buscar propinas):**

```bash
=============================================
        BÚSQUEDA DE PROPINAS
=============================================
Ingrese el término de búsqueda (o 'salir' para volver):
```

## **Si el usuario elige la opción 1:**

```bash
=============================================
  Cálculo de Propina
=============================================
Ingrese el monto total de la cuenta: $____
Ingrese el porcentaje de propina (por ejemplo: 15): ___ %
=============================================
La propina calculada es: $___
El total a pagar es: $___
=============================================
¿Deseas calcular nuevamente? (S/N)
```

------

## **Si el usuario elige la opción 2:**

```bash
=============================================
  Dividir Cuenta entre Varias Personas
=============================================
Ingrese el monto total de la cuenta: $____
Ingrese el porcentaje de propina (por ejemplo: 15): ___ %
Ingrese el número de personas: __
=============================================
La propina calculada es: $___
El total a pagar es: $___
Monto por persona: $___
=============================================
¿Deseas calcular nuevamente? (S/N)
```

------

## **Si el usuario elige la opción 5:**

```bash
=============================================
¡Gracias por usar el Simulador de Propina!
=============================================
```

------

# **Flujo del Menú:**

1. **Menú Principal**: El usuario puede elegir entre cinco opciones:
   - Opción 1: Calcular la propina y el total a pagar
   - Opción 2: Calcular la propina y dividir la cuenta
   - Opción 3: Gestionar registros de propinas (CRUD)
   - Opción 4: Buscar propinas anteriores
   - Opción 5: Salir del programa
2. **Submenú de Cálculo de Propina**: Permite calcular propinas individuales
3. **Submenú de División de Cuenta**: Calcula propinas y divide entre personas
4. **Submenú de Gestión**: Permite administrar los registros de propinas
   - Ver todas las propinas guardadas
   - Agregar nuevos registros
   - Actualizar registros existentes
   - Eliminar registros
5. **Submenú de Búsqueda**: Facilita la búsqueda de propinas anteriores
6. **Salir**: Termina el programa

# Estructura de Datos

Los registros de propinas se almacenan en formato JSON con la siguiente estructura:

```json
{
    "id": 1,
    "total": 100.0,
    "porcentaje": 15,
    "propina": 15.0,
    "fecha": "2024-03-20 10:30:00"
}
```

# Requisitos del Sistema

- Python 3.x
- Sistema de archivos con permisos de escritura para almacenar el archivo JSON
- Directorio 'data' en la raíz del proyecto para almacenamiento


