"""-Añade un título con un print() para la pizzería, algo como -> Pizzería PF <-.
-El usuario introducirá el dinero que quiera. Guárdalo en una variable.
-Crea una lista donde ir añadiendo los ingredientes extra. Pista: métodos de adición en listas.
-Habrá mínimo tres tipos de pizzas para elegir (pon las que quieras).
-Cada pizza tendrá un coste diferente.
-El usuario podrá elegir solo una pizza.
-Una vez elegida la pizza, se le informará al usuario del total que lleva por el momento.
Se le debe solicitar, si quiere o no, añadir ingredientes extra (estos harán subir el precio final).
Añade al menos 3 ingredientes extra. El usuario podrá elegir ninguno, uno o varios de estos.
No hay límite de ingredientes extra. Si se pasa del dinero que tiene, se le dirá que no le llega y que vuelva a realizar el pedido.
Las pizzas e ingredientes, tendrán sus precios almacenados en variables o constantes (piensa que los precios son los que son y no deben variar en todo el programa).
Con cada ingrediente extra, se le debe ir sumando el precio al total y mostrárselo al usuario con el cambio que le queda.
Si el usuario no quiere ingredientes extra, puede pagar directamente sin añadir ninguno.
Finalmente, se le debe presentar el ticket (imprimido en la consola) con el total gastado, el cambio y todos
los elementos que se han añadido al pedido, pizza, ingredientes extra y precios."""


def eleccion():
    global costetotal
    costetotal = 0
    print(pizzas)
    pizza = input("Que pizza desea?:").title()
    pizzaSeleccionada.append(pizza)
    for i in pizzas:
        costetotal = float(pizzas[i])
        if i == pizza:
            print("Has elegido la pizza:", i, "Y su costo es :", costetotal)
            extra = input("Desea añadir extras?(Todos los extras cuestan 1 euro) si/no:")
            if extra == "si":
                print(extras)
                bucle1 = True
                while bucle1:
                    extra1 = input("Que extra desea?:").title()
                    if extra1 in extras:
                        print("Añadiste:", extra1)
                        pizzaSeleccionada.append(extra1)
                        costetotal = costetotal + extras[i]
                        seguir = input("Otro mas? si o no:")
                        if seguir == "si":
                            bucle1 = True
                        else:
                            bucle1 = False
                    else:
                        print("No se encuentra el extra.")
            elif extra == "no":
                break


def pagar1(num):
    num1 = 0
    if num < costetotal:
        num1 = num - costetotal
        print("Saldo insuficiente , le falta:", num1)
    else:
        num1 = costetotal - num
        print("Pedido completado , le sobran: ", num1)


pizzaSeleccionada = []
extras = {"Tomate": 1, "Queso Gouda": 1, "Salami": 1, "Queso Parmesano": 1}
global credito
extra = []
pizzas = {"Margarita": 5.50, "Bolognesa": 9.10, "Hawai": 6.99}
bucle = True
credito=int(input("Que saldo desea introducir?:"))
while bucle:
    entrada = int(input(
        "Bienvenido a :\n"
        "------------------->PIZZERIA LABUENAMASA<----------------------\n"
        "1.Elegir pizza y extras .\n"))
    if entrada == 1:
        eleccion()
        bucle = False
    if entrada == 2:
        print("Se termino.")
        bucle = False
print(f'Su pedido es', pizzaSeleccionada, f' Y el coste de la pizza es :  {costetotal}')
pagar = input("Desea pagar?")
if pagar == "si":
    print("Su saldo es :", credito)
    pagar1(credito)
