import datetime
class Indices:
    def __init__(self):
        self.__pod_d= 0
        self.__pod_t= 0
        self.__pod_a1= 0
        self.__pod_a2= 0
        self.__pod_b= 0
        self.__pod_g= 0

    def verPod_d(self):
        return self.__pod_d
    def asignarPod_d(self,f):
        self.__pod_d=f

    def verPod_t(self):
        return self.__pod_t
    def asignarPod_t(self,f):
        self.__pod_t=f

    def verPod_a1(self):
        return self.__pod_a1
    def asignarPod_a1(self,f):
        self.__pod_a1=f
    
    def verPod_a2(self):
        return self.__pod_a2
    def asignarPod_a2(self,f):
        self.__pod_a2=f

    def verPod_t(self):
        return self.__pod_b
    def asignarPod_t(self,f):
        self.__pod_b=f
    
    def verPod_g(self):
        return self.__pod_g
    def asignarPod_g(self,f):
        self.__pod_g=f
class Visita:
    def __init__(self):
        self.__fecha=datetime.datetime.now().strtime('%x')
        self.__regitro=''
        self.__notas=''
        self.__indice=Indices()
    def verFechas(self):
        return self.__fecha
    def asignarFecha(self,f):
        self.__fecha=f
    
    def verRegistro(self):
        return self.__regitro
    def asignarRegistro(self,f):
        self.__registro=f
    
    def verNotas(self):
        return self.__notas
    def asignarNotas(self,f):
        self.__notas=f

    def verIndice(self):
        return self.__indice
    def asignarindice(self,f):
        self.__indice=f

class Paciente:
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__visitas = {} 
              
    #metodos get    
    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verVisitas(self):
        return self.__visitas 
    # metodos set
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarVisitas(self,v):
        self.__visitas = v 
        
class Sistema:    
    def __init__(self):
        self.__pacientes = {} 
        
    def verificarPaciente(self,c):
        return c in self.__pacientes
        
    def ingresarPaciente(self,pac):
        self.__pacientes[pac.verCedula()]=pac
        return True
    
    def eliminarPaciente(self, c):
        del self.__pacientes[c]
        return True
    
    def verDatosPaciente(self, c):
        return self.__pacientes[c] #si encuentro el paciente lo retorno
    
    def cargarguardar(self):
        #archivos txt


def main():
    sis = Sistema() 
    #probemos lo que llevamos programado
    while True:
        #TAREA HACER EL MENU
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente\n\t--> ")) 
        
        if opcion == 1:
            #ingreso pacientes
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                #3. se almacena en la lista que esta dentro de la clase sistema
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            #1. solicito la cedula que quiero buscar
            c = int(input("Ingrese la cedula a buscar: ")) 
            #le pido al sistema que me devuelva en la variable p al paciente que tenga
            #la cedula c en la lista
            p = sis.verDatosPaciente(c) 
            #2. si encuentro al paciente imprimo los datos
            if p != None:
                print("Nombre: " + p.verNombre()) 
                print("Cedula: " + str(p.verCedula())) 
                print("Genero: " + p.verGenero()) 
                print("Servicio: " + p.verServicio()) 
            else:
                print("No existe un paciente con esa cedula") 
        elif opcion !=0:
            continue 
        else:
            break 

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main() 
        
        
        
        
        
        
        
        
