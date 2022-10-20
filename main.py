import parametros as p
import random

###### INICIO PUNTO 1 ######
### Rellenar Clase Automóvil ###
class Automovil(object):
    def __init__(self,km,ano):
        self.__km = km
        self.ano = ano
        self.ruedas = []
        self.acel = 0
        self.vel = 0

    def avanzar(self, tiempo):
        self.__km += self.vel * tiempo 

    def acelerar(self,tiempo):
        self.acel += tiempo*0.5
        self.vel += self.acel *tiempo * 3.6
        self.avanzar(tiempo)
        self.acel = 0

    def frenar(self,tiempo):
        self.acel = tiempo*0.5
        self.vel += self.acel * tiempo* 3.6
        if self.vel < 0 :
            self.vel = 0
            self.avanzar(tiempo) 
            self.acel = 0
        else:
            self.avanzar(tiempo)
            self.acel = 0
    
    def obtener_kilometraje(self):
        return self.__km

    def reemplazar_rueda(self):
        #VALOR MINIMO DE LA LISTA 
        #ENTREGA EL INDICIE
        # retornar_resistencia = lambda rueda: rueda.resistencia_actual
        tm = min(self.ruedas, key= self.retornar_resistencia)
        print(tm)
        i = self.ruedas.index(tm)

        #METODO PARA BORRAR UN VALOR SEGUN EL INDICE 
        del self.ruedas[i]
        #IMPRIME LA LISTA 
        print(self.ruedas)


        self.ruedas.append(Rueda())

    def retornar_resistencia(self,rueda):
        return rueda.resistencia_actual

r1 = Automovil(500,2015)
r2 = Automovil(680,2017)

rueda = [r1,r2]


        

###### FIN PUNTO 1 ######


###### INICIO PUNTO 2 ######
### Rellenar Clase Moto ###
class Moto(Automovil):
    
    # CONTRUCTOR GRANDE AQUI VAN TODOS LOS ATRIBUTOS 
    def __init__(self,km,ano,cilindra):
        super().__init__(km,ano) #ATRIBUTOS DE LA CLASE PADRE 
        self.cilindra = cilindra
        self.ruedas = [Rueda(),Rueda()] #aqui pase las 2 ruedas 

    def acelerar(self,tiempo):
        super().acelerar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar('Acelerar')
        
        
    def frenar(self,tiempo):
        super().frenar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar('Frenar')

    def __str__(self):
        return f"Moto del año {self.ano}."
###### FIN PUNTO 2 ######


###### INICIO PUNTO 3 ######
### Rellenar Clase Camión ###
class Camion(Automovil):
    
    def __init__(self, km, ano, carga):
        super().__init__(km, ano)
        self.carga = carga
        self.ruedas = [Rueda(),Rueda(),Rueda(),Rueda(),Rueda(),Rueda()]


    def acelerar(self,tiempo):
        super().acelerar(tiempo)
        #lo mismo para camion y para el metodo frenar, pero con 
        for rueda in self.ruedas:
            rueda.gastar('acelerar')

    def frenar(self,tiempo):
        super().frenar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar('Frenar')


    def __str__(self):
        return f"Camión del año {self.ano}."
###### FIN PUNTO 3 ######


### Esta clase está completa, NO MODIFICAR ###
class Rueda:
    def __init__(self):
        self.resistencia_actual = random.randint(*p.RESISTENCIA)
        self.resistencia_total = self.resistencia_actual
        self.estado = "Perfecto"

    def gastar(self, accion):
        if accion == "acelerar":
            self.resistencia_actual -= 5
        elif accion == "frenar":
            self.resistencia_actual -= 10
        self.actualizar_estado()

    def actualizar_estado(self):
        if self.resistencia_actual < 0:
            self.estado = "Rota"
        elif self.resistencia_actual < self.resistencia_total / 2:
            self.estado = "Gastada"
        elif self.resistencia_actual < self.resistencia_total:
            self.estado = "Usada"



### Esta funcion está completa, NO MODIFICAR ###
def seleccionar():
    for indice in range(len(vehiculos)):
        print(f"[{indice}] {str(vehiculos[indice])}")

    elegido = int(input())
    while elegido < 0 or elegido >= len(vehiculos):
        print('Intente nuevamente')
        elegido = int(input())
    
    vehiculo = vehiculos[elegido]
    print('se selecciono el vehiculo',str(vehiculo))
    return vehiculo
###### INICIO PUNTO 4.2 ######
### Se debe completar cada opción según lo indicado en el enunciado ###
def accion(vehiculo, opcion):
    if opcion == 2: #Acelerar
        t = int(input('Ingresar el tiempo para acelerar :  '))
        vehiculo.acelerar(t)
        print('--------------------------------------------------------------------------------')
        print('Se ha acelerado ',t,' segundos llegando un velocidad de ', vehiculo.vel,' km/h')
        print('--------------------------------------------------------------------------------')

    elif opcion == 3: #Frenar
        t = int(input('Ingresar el tiempo para frenar : '))
        vehiculo.frenar(t)
        print('--------------------------------------------------------------------------------')
        print('Se ha frenado por ',t,'segundos llegando a una velocidad de ', vehiculo.vel,'km/h')
        print('--------------------------------------------------------------------------------')
        
    elif opcion == 4: #Avanzar
        t = int(input(' Ingrese el tiempo para avanzar : '))
        vehiculo.avanzar(t)
        print('--------------------------------------------------------------------------------')
        print('Se ha avanzado ',t,' segundos a una velocidad de ', vehiculo.vel,' km/h ',)
        print('--------------------------------------------------------------------------------')
    elif opcion == 5: #Cambiar Rueda
        vehiculo.reemplazar_rueda()
        print('Se ha remplazado una rueda con exito ')
    elif opcion == 6: #Mostrar Estado
        print('----------------------------------------------')
        print('ESTADO DEL VEHICULO ',vehiculo, 'es el siguente :')
        print('AÑO DEL VEHICULO : ',vehiculo.ano)
        print('VELOCIDAD DEL VEHICULO : ',vehiculo.vel)
        print('kILOMETRAJE DEL VEHICULO : ',vehiculo.obtener_kilometraje())   
        print('----------------------------------------------')
        print(' ')
        for i in range(len(vehiculo.ruedas)):
            print(f'El estado de la rueda {i+1} es : {vehiculo.ruedas[i].estado} ')

###### FIN PUNTO 4.2 ######


if __name__ == "__main__":

    ###### INICIO PUNTO 4.1 ######
    ### Aca deben instanciar los vehiculos indicados
    ### en el enunciado y agregarlos a la lista vehiculos
    m = Moto(500,2017,500)
    c = Camion(15854,2000,150)
    vehiculos = [m,c]


    ###### FIN PUNTO 4.1 ######


    ### El codigo de abajo NO SE MODIFICA ###
    vehiculo = vehiculos[0] # Por default comienza seleccionado el primer vehículo  

    dict_opciones = {1: ("Seleccionar Vehiculo", seleccionar),
                     2: ("Acelerar", accion),
                     3: ("Frenar", accion),
                     4: ("Avanzar", accion),
                     5: ("Reemplazar Rueda", accion),
                     6: ("Mostrar Estado", accion),
                     0: ("Salir", None)
                    }

    op = -1
    while op != 0:
        
        for k, v in dict_opciones.items():
            print(f"{k}: {v[0]}")
        
        try:
            op = int(input("Opción: "))
        
        except ValueError:
            print(f"Ingrese opción válida.")
            op = -1
        
        if op != 0 and op in dict_opciones.keys():
            if op == 1:
                vehiculo = dict_opciones[op][1](vehiculos)
            else:
                dict_opciones[op][1](vehiculo, op)
        elif op == 0:
            pass
        else:
            print(f"Ingrese opción válida.")
            op = -1
