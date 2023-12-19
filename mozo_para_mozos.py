"""
Cosas que no tiene el programa:

1) Funcion- take_beverage_order: 
            Que haya una forma de salir de la misma, aunque haya entrado
            (en el hipotetico caso que la tercer linea de main() dio True, pero despues no quizo pedir nada)

2) Funcion- ambas:
            A) Que si el user pidió por ejemplo x plato n veces, y despues pidio el mismo plato otra cant
            de veces, seria mejor que acople la segunda orden a la primera en vez de generar
            2 (o más) diccionarios de un mismo producto

            B) Que si el user dio de input que directamente no existe, estaria mejor
            que le diga 1 sola vez algo como "no hay eso"


"""
import difflib # encuentra busquedas parecidas
from my_exceptions import ZeroError, is_zero, IsHundredError, is_hundred

orden_lista = []

total = 0

menu_comida = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

bebidas_menu = {
    "Agua": 1.0,
    "Coca": 2.5,
    "Soda": 1.5,
}


def main():

    take_food_order()
    if quiere_tomar():
        take_beverage_order()
    print(ticket(orden_lista))



def take_food_order():
    global orden_lista
    global total
    while True:
        orden = input("\nWhat do you want to eat?: ").title().strip()
        if orden in menu_comida:
            cuantos = cuantos_o(orden)
            orden_lista.append({"Plato": orden, "Cantidad": cuantos, "Total": menu_comida[orden] * cuantos})
            total += menu_comida[orden] * cuantos
            while True:
                otro_plato = input("\nQuiere otro plato?: ").lower().strip()
                if otro_plato == "y":
                    break
                elif otro_plato == "n":
                    return
                else:
                    print("Y OR N.")
                    continue

        else:
            for i in menu_comida:
                if difflib.SequenceMatcher(None, orden, i).ratio() >= 0.7:
                    print(f"\nYou may want \x1B[3m{i}\x1B[0m?")

                    
        
def take_beverage_order():
    global orden_lista
    global total
    while True:
        bebida = input("\nWhat do you want to drink?: ").title().strip()
        if bebida in bebidas_menu:
            cuantas_b = cuantos_o(bebida)
            orden_lista.append({"Bebida" : bebida, "Cuantas" : cuantas_b, "Total": bebidas_menu[bebida] * cuantas_b})
            total += bebidas_menu[bebida] * cuantas_b
            while True:
                extra = input("\nDo you want anything else? (Y for yes, otherwise not): ").lower().strip()
                if extra == "y":
                    break 
                elif extra == "n":
                    return 
                else:
                    print("Invalid input. Please enter 'Y' or 'N'\n")
                    continue
        else:
            for i in bebidas_menu:
                if difflib.SequenceMatcher(None, bebida, i).ratio() >= 0.7:
                    print(f"\nYou may want {i}?")
                    continue

def cuantos_o(orden):
    while True:
        try:
            cuantos = int(input(f"\nCuantos {orden}/s querés?: "))
            is_zero(cuantos)
            is_hundred(cuantos)                    
        except ValueError:
            print("\nOnly numbers allowed")
            continue
        except ZeroError: # no es 100% necesaria, pero aproveche para aprender algo nuevo, y de paso dejar el codigo mas ordenado.
            print(f"\nyou can´t order for 0 {orden}s")
            continue
        except IsHundredError: # Ídem.
            print("\nLimit per order: 100.")
            continue
        
        return cuantos

def quiere_tomar():
    while True:
        s = input("\nquiere tomar? (y||n): ").lower().strip()
        if s == "y":
            return True
        elif s == "n":
            print("\nallright")
            return False
        else:
            continue


def ticket(lista):
    print("\nWe wish you enjoyed it!")
    text = "\n"
    for i in lista:
        if "Plato" in i:
            text += f'{i["Plato"]} x {i["Cantidad"]}  ---  ${i["Total"]}\n'
        elif "Bebida" in i:
            text += f'{i["Bebida"]} x {i["Cuantas"]}  ---  ${i["Total"]}\n'
    text += f"{'-' * 27}\nSubtotal: {total}$\nCon la tecnología de mozoo!\n{'-' * 27}"
    return text

if __name__ == "__main__":
    main()