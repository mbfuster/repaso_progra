class Auto:
    def __init__(self, ide, marca, year, modelo, transmision, precio, estado="Nuevo", dueno=None):
        self.id = ide
        self.marca = marca
        self.year = year
        self.transmision = transmision
        self.modelo = modelo
        self.precio = precio
        self.estado = estado
        self.dueno = dueno

    def __str__(self):
        string = '{0.modelo} {0.year} - {0.marca}'.format(self)
        string += '. Dueño:{}'.format(self.dueno.nombre) if self.dueno else ''
        return string


class Sucursal:
    def __init__(self, nombre, nuevos, usados):
        self.nombre = nombre
        self.nuevos = nuevos
        self.usados = usados

    def AgregarAuto(self, auto):
        if auto.estado == "Usado" or auto.estado == "usado":
            self.usados.append(auto)
        else:
            self.nuevos.append(auto)


class Automotora:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sucursales = []

    def crear_sucursal(self, sucursal):
        self.sucursales.append(sucursal)


class Contacto:
    def __init__(self, nombre, rut, telefono, correo):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
        self.correo = correo


# filtro para año y precio, donde parametro ("param") va a corresponder a "año" o a "precio"
def FiltroPorValor(v_max, v_min, automotora, param):
    lista_autos = []
    for suc in automotora.sucursales:
        lista_temp = []
        lista_temp.append(suc.nombre)
        for aut in suc.nuevos:
            if param == "año":
                a = aut.year
            else:
                a = aut.precio
            if a <= v_max and a >= v_min:
                lista_temp.append(aut)
        for aut in suc.usados:
            if param == "año":
                a = aut.year
            else:
                a = aut.precio
            if a <= v_max and a >= v_min:
                lista_temp.append(aut)
        lista_autos.append(lista_temp) if len(lista_temp) > 1 else ''
        lista_temp = []
    return lista_autos


def FiltroPorMarca(marca, automotora):
    lista_autos = []
    for suc in automotora.sucursales:
        lista_temp = []
        lista_temp.append(suc.nombre)
        for aut in suc.nuevos:
            if aut.marca == marca:
                lista_temp.append(aut)
        for aut in suc.usados:
            if aut.marca == marca:
                lista_temp.append(aut)
        lista_autos.append(lista_temp) if len(lista_temp) > 1 else ''
        lista_temp = []
    return lista_autos


def FiltroPorTransmision(transmision, automotora):
    lista_autos = []
    for suc in automotora.sucursales:
        lista_temp = []
        lista_temp.append(suc.nombre)
        for aut in suc.nuevos:
            if aut.transmision == transmision:
                lista_temp.append(aut)
        for aut in suc.usados:
            if aut.transmision == transmision:
                lista_temp.append(aut)
        lista_autos.append(lista_temp) if len(lista_temp) > 1 else ''
        lista_temp = []
    return lista_autos


def FiltroPorEstado(estado, automotora):
    lista_autos = []
    for suc in automotora.sucursales:
        lista_temp = []
        lista_temp.append(suc.nombre)
        if estado == "nuevo" or "Nuevo":
            lista_temp.append(suc.nuevos)
            lista_autos.append(lista_temp)
            lista_temp = []
        if estado == "usado" or "Usado":
            lista_temp.append(suc.usados)
            lista_autos.append(lista_temp) if len(lista_temp) > 1 else ''
            lista_temp = []
    return lista_autos


def CompararListas(lista1, lista2):
    lista_autos = []
    for i in lista1:
        for j in lista2:
            if i == j:
                lista_autos.append(i)
    return lista_autos


a = Automotora("Automotriz Mavrik")

b1 = Sucursal("LasCondes", [], [])
b2 = Sucursal("Vitacura", [], [])
b3 = Sucursal("Ñuñoa", [], [])
b4 = Sucursal("Providencia", [], [])
a.crear_sucursal(b1)
a.crear_sucursal(b2)
a.crear_sucursal(b3)
a.crear_sucursal(b4)

p1 = Contacto("belen", "18466323-6", "73395180", "mbfuster@uc.cl")
p2 = Contacto("Juan", "18244014-5", "76543210", "juanin@31min.com")

c1 = Auto('001', "toyota", 2009, "camioneta", "MT", 12000000, estado="Nuevo")
c2 = Auto("002", "MG", 2012, "MG3", "MT", 15000000, "Usado", p1)
c3 = Auto("003", "honda", 2013, "kshgo", "AT", 13500000, estado="Nuevo")
c4 = Auto("004", "audi", 2011, "A3", "MT", 20000000, "Usado", p2)
c5 = Auto("005", "Great Wall", 2007, "haval", "AT", 30000000, "nuevo")
c6 = Auto("006", "kia", 2009, "morning", "MT", 13000000, "usado", p1)

b1.AgregarAuto(c1)
b2.AgregarAuto(c2)
b3.AgregarAuto(c6)
b4.AgregarAuto(c3)
b1.AgregarAuto(c4)
b2.AgregarAuto(c5)

while True:
    r1 = input("trabajador o cliente?\n")
    if r1 == "cliente" or r1 == "Cliente":
        while True:
            lista_cliente = []
            r2c = int(input(
                "¿Qué estás buscando? \n1:Rango de años\n2:Rango de precio\n3:Marca\n4:Tipo de transmision\n"
                "5:Usado o nuevo\n"))
            if r2c == 1:
                ano_min = int(input("desde que año"))
                ano_max = int(input("hasta que año"))
                l1 = FiltroPorValor(ano_max, ano_min, a, "año")
                if len(lista_cliente) != 0:
                    lista_cliente = CompararListas(lista_cliente, l1)
                else:
                    lista_cliente = l1
                for q in lista_cliente:
                    for w in q:
                        print(w)

            elif r2c == 2:
                precio_min = int(input("desde que precio"))
                precio_max = int(input("hasta que aprecio"))
                l2 = FiltroPorValor(precio_max, precio_min, a, "precio")
                if len(lista_cliente) != 0:
                    lista_cliente = CompararListas(lista_cliente, l2)
                else:
                    lista_cliente = l2
                for q in lista_cliente:
                    for w in q:
                        print(w)

            elif r2c == 3:
                marca = input("qué marca?\n")
                l3 = FiltroPorMarca(marca, a)
                if len(lista_cliente) != 0:
                    lista_cliente = CompararListas(lista_cliente, l3)
                else:
                    lista_cliente = l3
                for q in lista_cliente:
                    for w in q:
                        print(w)

            elif r2c == 4:
                trans = input("qué tipo de transmisión?\n")
                l4 = FiltroPorTransmision(trans, a)
                if len(lista_cliente) != 0:
                    lista_cliente = CompararListas(lista_cliente, l4)
                else:
                    lista_cliente = l4
                for q in lista_cliente:
                    for w in q:
                        print(w)

            elif r2c == 5:
                estado = input("'usado' o 'nuevo'?\n")
                l5 = FiltroPorEstado(estado, a)
                if len(lista_cliente) != 0:
                    lista_cliente = CompararListas(lista_cliente, l5)
                else:
                    lista_cliente = l5
                for q in lista_cliente:
                    for w in q:
                        print(w)
            r3c = input("Quieres agregar otro filtro? (si o no)\n")
            if r3c == "si" or r3c == "Si":
                r2c = int(input(
                    "¿Qué estás buscando? \n1:Rango de años\n2:Rango de precio\n3:Marca\n4:Tipo de transmision\n5:Usado o nuevo\n"))
            else:
                break

    elif r1 == "trabajador":
        r2t = int(input("Quieres:\n1:Cambiar el precio a un auto?\n2:Buscar un auto en la base de datos\n"))
        while True:
            if r2t == 1:
                ide = input("Inserte el ID del auto al que desee cambiar el precio")
                for suc in a.sucursales:
                    for aut in suc.usados:
                        if aut.id == ide:
                            print(aut)
                            precio_nuevo = int(
                                input("Inserte nuevo precio(recuerde que debe ser divisible por 500.000)\n"))
                            if precio_nuevo % 500000 == 0:
                                aut.precio = precio_nuevo
                                r3t = input("precio cambiado existosamente\n¿Deseas realizar otra accion?(si o no)")
                                if r3t == "si":
                                    r2t = int(input(
                                        "Quieres:\n1:Cambiar el precio a un auto?\n2:Buscar un auto en la base de datos\n"))
                            else:
                                precio_nuevo = int(input("valor invalido, intente nuevamente"))
            elif r2t == 2:
                ide = input("Inserte el ID del auto que desee buscar")
                for suc in a.sucursales:
                    for aut in suc.usados:
                        if aut.id == ide:
                            print(aut)
                            r3t = input("¿Deseas realizar otra accion?(si o no)")
                            if r3t == "si":
                                r2t = int(input(
                                    "Quieres:\n1:Cambiar el precio a un auto?\n2:Buscar un auto en la base de datos\n"))
