class Auto:
    def __init__ (self, ide, marca, year, modelo, transmision, precio, estado = "Nuevo", dueno = None):
        self.id = ide
        self.marca = marca
        self.year = year
        self.transmision = transmision
        self.modelo = modelo
        self.precio = precio
        self.estado = estado
        self.dueno = dueno

class Sucursal:
    def __init__(self, nombre, nuevos, usados):
        self.nombre = nombre
        self.nuevos = nuevos
        self.usados = usados

    def AgregarAuto(self, auto):
        if not auto.estado:
            self.usados.append(auto)
        else:
            self.nuevos.append(auto)


class Automotora:
    def __init__ (self, nombre):
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

a = Automotora("lhosgdsd")
print(a)
b = Sucursal("qwerty",[],[])
a.crear_sucursal(b)
c= Auto('001', "toyota", 2009,"jkhkg", "MT", 12000000, estado = "Nuevo")
p = Contacto("belen", "18466323-6", "73395180", "mbfuster@uc.cl")
d=Auto("002","qwr",2012,"oiu{p","MT",15000000, "Usado", p)
print(d.dueno.nombre)

while True:
    r1 = input("trabajador o cliente?")
    if r1 == "cliente" or "Cliente":
        r2c = int(input("¿Qué estás buscando? \n1:Rango de años\n2:Rango de precio\n3:Marca\n4:Tipo de transmision\n5:Usado o nuevo\n"))
        if r2c == 1:
            ano_min=int(input("desde que año"))
            ano_max=int(input("hasta que año"))
