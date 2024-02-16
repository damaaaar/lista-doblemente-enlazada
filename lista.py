class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def carnet_repetido(self, carnet):
        nodo_actual = self.cabeza
        while (nodo_actual):
            if (nodo_actual.carnet == carnet):
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def insertar_al_inicio(self, nombre, apellido, carnet):
        if (self.carnet_repetido(carnet)):
            print("Numero de carnet repetido, no se hizo el registro\n")
            return

        nuevo_nodo = Nodo(nombre, apellido, carnet)
        nuevo_nodo.siguiente = self.cabeza
        nuevo_nodo.anterior = None
        if (self.cabeza is not None):
            self.cabeza.anterior = nuevo_nodo
        self.cabeza = nuevo_nodo
        if (self.cola is None):
            self.cola = nuevo_nodo

    def insertar_al_final(self, nombre, apellido, carnet):
        if (self.carnet_repetido(carnet)):
            print("Numero de carnet repetido, no se hizo el registro\n")
            return

        nuevo_nodo = Nodo(nombre, apellido, carnet)
        nuevo_nodo.anterior = self.cola
        nuevo_nodo.siguiente = None
        if (self.cola is not None):
            self.cola.siguiente = nuevo_nodo
        self.cola = nuevo_nodo
        if (self.cabeza is None):
            self.cabeza = nuevo_nodo

    def eliminar_por_valor(self, carnet):
        if (self.cabeza is None and self.cola is None):
            print("Lista vacia, primero debe ingresar datos.")
            return

        nuevo_nodo = self.cabeza
        while (nuevo_nodo):
            if (nuevo_nodo.carnet == carnet and nuevo_nodo.siguiente == None and nuevo_nodo.anterior == None):
                self.cabeza = None
                self.cola = None
                nuevo_nodo = None
                print("Lista vacia, se eliminaron todos los datos.")
                break

            elif (nuevo_nodo.anterior == None and nuevo_nodo.carnet == carnet):
                nuevo_nodo = nuevo_nodo.siguiente
                nuevo_nodo.anterior = None
                self.cabeza = nuevo_nodo
                break

            elif (nuevo_nodo.siguiente == None and nuevo_nodo.carnet == carnet):
                nuevo_nodo = nuevo_nodo.anterior
                nuevo_nodo.siguiente = None
                self.cola = nuevo_nodo
                break

            else:
                if (nuevo_nodo.carnet == carnet):
                    nodo_temporal_uno = nuevo_nodo.anterior
                    nodo_temporal_dos = nuevo_nodo.siguiente
                    nodo_temporal_uno.siguiente = nodo_temporal_dos
                    nodo_temporal_dos.anterior = nodo_temporal_uno
                    nuevo_nodo = nodo_temporal_dos
                    break

                elif (nuevo_nodo.siguiente == None and nuevo_nodo.carnet != carnet):
                    print("No se encontro el carnet que busca.")
                    break

                else:
                    nuevo_nodo = nuevo_nodo.siguiente

    def mostrar_datos(self):
        nuevo_nodo = self.cabeza
        literal = "None <- "
        while (nuevo_nodo):
            nodo_datos = f"{
                nuevo_nodo.carnet}: {nuevo_nodo.nombre} {nuevo_nodo.apellido}"
            if (nuevo_nodo.siguiente == None):
                literal += str(nodo_datos) + " -> "
            else:
                literal += str(nodo_datos) + " <-> "
            nuevo_nodo = nuevo_nodo.siguiente
        literal += "None"
        print(literal)
