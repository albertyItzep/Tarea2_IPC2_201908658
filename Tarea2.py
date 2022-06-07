# ------------ Nodo ----------------------
class NodoNumero:
    def __init__(self,numero:int):
        self.numero=numero
        self.nextNodo=None
        self.previusNodo=None


# ------------ lista ---------------------
class ListaCircular:
    def __init__(self):
        self.root:NodoNumero = None
        self.endRoot:NodoNumero = None
        self.size = 0
    
    def push(self,numero:int):
        nuevo_Nodo = NodoNumero(numero)
        self.size += 1
        if self.root == None:
            self.root = nuevo_Nodo
            self.endRoot = nuevo_Nodo
            self.endRoot.nextNodo = nuevo_Nodo
        else:
            self.endRoot.nextNodo = nuevo_Nodo
            nuevo_Nodo.previusNodo = self.endRoot
            self.endRoot = nuevo_Nodo
            self.endRoot.nextNodo = self.root
    
    def getNodo(self, number:int):
        if self.size > 0:
            tmp = self.root
            for x in range(self.size):
                anterior = "No tiene"
                actual = "No tiene"
                siguiente = "No tiene"
                if tmp.numero == number:
                    if tmp.previusNodo != None:
                        anterior = tmp.previusNodo.numero
                        actual = tmp.numero
                        siguiente = tmp.nextNodo.numero
                        return anterior,actual,siguiente
                    else:
                        actual = tmp.numero
                        siguiente = tmp.nextNodo.numero
                        return anterior,actual,siguiente
                tmp = tmp.nextNodo
            anterior = ""
            actual = ""
            siguiente = ""
            return anterior,actual,siguiente
    def printList(self):
        tmp=self.root
        for x in range(self.size):
            print(tmp.numero)
            tmp = tmp.nextNodo
        
# ------------ main ----------------------

lista_Numeros=ListaCircular()
lista_Numeros.push(1)
lista_Numeros.push(3)
lista_Numeros.push(7)
lista_Numeros.push(11)
lista_Numeros.push(15)
lista_Numeros.push(21)
lista_Numeros.printList()
try:
    print("ingrese numero a verificar:")
    number = int(input())
    anterior,actual,siguiente = lista_Numeros.getNodo(number)
    print("-*-------------*---------")
    if anterior != "" and actual != "" and siguiente != "":
        print(" el numero Anterior es : " + str(anterior)+", el numero actual es: " + str(actual) + ", el numero siguiente es: " + str(siguiente))
        print("-*-------------*---------")
    else:
        print(" el numero seleccionado no existe!")
except:
    print("El valor ingresado es incorrecto")
