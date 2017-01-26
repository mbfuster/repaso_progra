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
        if auto.estado == "Usado" or auto.estado=="usado":
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
b1 = Sucursal("LasCondes",[],[])
b2 = Sucursal("Vitacura",[],[])
b3 = Sucursal("Ñuñoa",[],[])
b4 = Sucursal("Providencia",[],[])
a.crear_sucursal(b1)
a.crear_sucursal(b2)
a.crear_sucursal(b3)
a.crear_sucursal(b4)

p1 = Contacto("belen", "18466323-6", "73395180", "mbfuster@uc.cl")
p2 = Contacto("Juan","72440145","76543210","juanin@31min.com")

c1= Auto('001', "toyota", 2009,"jkhkg", "MT", 12000000, estado = "Nuevo")
c2=Auto("002","qwr",2012,"oiu{p","MT",15000000, "Usado", p1)
c3=Auto("003","honda",2013,"kshgo","AT",13500000,estado="Nuevo")
c4=Auto("004","audi",2011,"A3","MT",20000000,"Usado",p2)
print(c2.dueno.nombre)


#filtro para año y precio, donde parametro ("param") va a corresponder a "año" o a "precio"
def FiltroPorValor(v_max,v_min,automotora,param):
    lista_autos = []
    if param == "año":
        a = aut.year
    else:
        a = aut.precio
    for suc in automotora.sucursales:
        lista_temp = []
        lista_temp.append(suc.nombre)
        for aut in suc.nuevos:
            if a <= v_max and a >= v_min:
                lista_temp.append(aut)
        for aut in suc.usados:
            if a <= v_max and a >= v_min:
                lista_temp.append(aut)
        lista_autos.append(lista_temp)
        lista_temp = []
        return lista_autos

#def FiltroPorMarca(marca,automotora):
#    for suc in



while True:
    r1 = input("trabajador o cliente?")
    if r1 == "cliente" or "Cliente":
        lista_cliente=[]
        r2c = int(input("¿Qué estás buscando? \n1:Rango de años\n2:Rango de precio\n3:Marca\n4:Tipo de transmision\n5:Usado o nuevo\n"))
        if r2c == 1:
            ano_min=int(input("desde que año"))
            ano_max=int(input("hasta que año"))
            l1=FiltroPorValor(ano_max,ano_min,a,"año")


