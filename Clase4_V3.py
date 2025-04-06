import datetime 
import os
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

    def verPod_b(self):
        return self.__pod_b
    def asignarPod_b(self,f):
        self.__pod_b=f
   
    def verPod_g(self):
        return self.__pod_g
    def asignarPod_g(self,f):
        self.__pod_g=f
    def __str__(self):
        return f"Delta: {self.verPod_d()}, Theta: {self.verPod_t()}, Alfa1: {self.verPod_a1()}, Alfa2: {self.verPod_a2()}, Beta: {self.verPod_b()}, Gamma: {self.verPod_g()}"
class Visita:
    def __init__(self):
        self.__fecha=datetime.datetime.now().strftime('%x')
        self.__registro=''
        self.__notas=''
        self.__indice=Indices()
    def verFecha(self):
        return self.__fecha
    def asignarFecha(self,f):
        self.__fecha=f

    def verRegistro(self):
        return self.__registro
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

    def ingresarVisitas(self, v):
        self.__visitas[v.verFecha()] = v
    
    def validarFecha(self, fecha_str):
        try:
            datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
            return True
        except ValueError:
            print("Fecha inválida. Usa el formato dd/mm/aaaa.")
            return False
    
    def verificarVisita(self,fecha):
        if fecha in self.__visitas:
            return True
        else:
            return False

    def eliminarVisita(self, fecha):
        if fecha in self.__visitas:
            del self.__visitas[fecha]
            return True
        return False
    
    def __str__(self):
        visitas_str = ""
        if self.__visitas:
            for fecha, visita in self.__visitas.items():
                visitas_str += f"\n  - Fecha: {fecha}, Registro: {visita.verRegistro()}, Notas: {visita.verNotas()}, Índices: {visita.verIndice()}"
        else:
            visitas_str = "  No hay visitas registradas."
        return f"Paciente: {self.__nombre}, Cédula: {self.__cedula}, Género: {self.__genero}\nVisitas:{visitas_str}"

        
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
    
    def cargarguardar(self, cedula):
            if cedula in self.__pacientes:
                pac=self.__pacientes[cedula]
                nombrearchivo=f'{cedula}.txt'
                with open(nombrearchivo, "w") as file:
                    file.write(f"Nombre: {pac.verNombre()}\n")
                    file.write(f"Cédula: {pac.verCedula()}\n")
                    file.write(f"Género: {pac.verGenero()}\n")
                    visitas = pac.verVisitas()
                    if visitas:
                        for fecha, visita in visitas.items():
                            file.write(f"Fecha de visita: {visita.verFecha()}\n")
                            file.write(f"Registro: {visita.verRegistro()}\n")
                            file.write(f"Notas: {visita.verNotas()}\n")

                            ind = visita.verIndice()
                            file.write(f"Índices:\n")
                            file.write(f"  pod_d: {ind.verPod_d()}\n")
                            file.write(f"  pod_t: {ind.verPod_t()}\n")
                            file.write(f"  pod_a1: {ind.verPod_a1()}\n")
                            file.write(f"  pod_a2: {ind.verPod_a2()}\n")
                            file.write(f"  pod_b: {ind.verPod_b()}\n")
                            file.write(f"  pod_g: {ind.verPod_g()}\n")
                            file.write("-" * 40 + "\n")
                    else:
                        file.write("No hay visitas registradas.\n")
                print(f"Paciente guardado en el archivo: {nombrearchivo}")
            else:
                print("No se encontró un paciente con esa cédula.")
def main():
    sis = Sistema()
    def validarFloat(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print("Por favor, ingrese un número válido (usar punto para decimales, no coma).")

    while True:
        opcion = int(input('''--------Sistema de Gestión de Registros Electrofisiológicos------------
        1. Ingresar nuevo paciente
        2. Editar paciente existente
        3. Eliminar paciente
        4. Ver paciente
        5. Guardar pacientes en archivo
        6. Salir
                           
        ---Digite una opción:  '''))
        if opcion == 1:
            while True:
                cedula = input("Ingrese la cédula del paciente: ")
                if sis.verificarPaciente(cedula):
                    print("\nYa existe un paciente con esa cédula.\n")
                else:
                    break
            nombre = input("Ingrese el nombre: ")
            genero = input("Ingrese el género: ")
            pac = Paciente()
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)

            agregar_visitas = input("¿Desea agregar visitas ahora? (si/no): ").lower()
            while agregar_visitas == 'si':
                fecha = input("Ingrese la fecha de la visita (dd/mm/aaaa): ")
                if pac.validarFecha(fecha):
                    if pac.verificarVisita(fecha):
                        print("Ya hay una visita registrada en esa fecha.")
                    else:
                        registro = os.getcwd()
                        notas = input("Notas del técnico: ")
                        visita = Visita()
                        visita.asignarFecha(fecha)
                        visita.asignarRegistro(registro)
                        visita.asignarNotas(notas)

                        indices = Indices()
                        indices.asignarPod_t(validarFloat("Potencia theta: "))
                        indices.asignarPod_a1(validarFloat("Potencia alfa1: "))
                        indices.asignarPod_a2(validarFloat("Potencia alfa2: "))
                        indices.asignarPod_b(validarFloat("Potencia beta: "))
                        indices.asignarPod_g(validarFloat("Potencia gamma: "))

                        visita.asignarindice(indices)
                        pac.ingresarVisitas(visita)
                        print("Visita registrada.")

                    agregar_visitas = input("¿Desea agregar otra visita? (si/no): ").lower()
                    if agregar_visitas=='si':
                        fecha = input("Ingrese la fecha de la visita (dd/mm/aaaa): ")
                        if pac.verificarVisita(fecha):
                            print("Ya hay una visita registrada en esa fecha.")
                        else:
                            registro = os.getcwd()
                            notas = input("Notas del técnico: ")
                            visita = Visita()
                            visita.asignarFecha(fecha)
                            visita.asignarRegistro(registro)
                            visita.asignarNotas(notas)

                            indices = Indices()
                            indices.asignarPod_d(float(input("Potencia delta: ")))
                            indices.asignarPod_t(float(input("Potencia theta: ")))
                            indices.asignarPod_a1(float(input("Potencia alfa1: ")))
                            indices.asignarPod_a2(float(input("Potencia alfa2: ")))
                            indices.asignarPod_b(float(input("Potencia beta: ")))
                            indices.asignarPod_g(float(input("Potencia gamma: ")))

                            visita.asignarindice(indices)
                            pac.ingresarVisitas(visita)
                            print("\nVisita agregada.\n")
                else: 
                    continue

            sis.ingresarPaciente(pac)
            print("Paciente y visitas registrados correctamente.")

        elif opcion == 2:
            cedula = input("Ingrese la cédula del paciente a editar: ")
            if sis.verificarPaciente(cedula):
                pac = sis.verDatosPaciente(cedula)
                sub_opcion = int(input("1. Agregar visita\n2. Eliminar visita\nSeleccione: "))
                if sub_opcion == 1:
                    while True:
                        fecha = input("Ingrese la fecha de la visita (dd/mm/aaaa): ")
                        if pac.verificarVisita(fecha):
                            print("Ya hay una visita registrada en esa fecha.")
                        else:
                            break
                    registro = os.getcwd()
                    notas = input("Notas del técnico: ")
                    visita = Visita()
                    visita.asignarFecha(fecha)
                    visita.asignarRegistro(registro)
                    visita.asignarNotas(notas)

                    indices = Indices()
                    indices.asignarPod_d(float(input("Potencia delta: ")))
                    indices.asignarPod_t(float(input("Potencia theta: ")))
                    indices.asignarPod_a1(float(input("Potencia alfa1: ")))
                    indices.asignarPod_a2(float(input("Potencia alfa2: ")))
                    indices.asignarPod_b(float(input("Potencia beta: ")))
                    indices.asignarPod_g(float(input("Potencia gamma: ")))

                    visita.asignarindice(indices)
                    pac.ingresarVisitas(visita)
                    print("Visita agregada.")
                elif sub_opcion == 2:
                    fecha = input("Ingrese la fecha de la visita a eliminar (dd/mm/aaaa): ")
                    if pac.eliminarVisita(fecha):
                        print("Visita eliminada.")
                    else:
                        print("No existe una visita en esa fecha.")
                else:
                    print("Paciente no encontrado.")
        elif opcion == 3:
                cedula = input("Ingrese la cédula del paciente a eliminar: ")
                if sis.verificarPaciente(cedula):
                    sis.eliminarPaciente(cedula)
                    return("Paciente eliminado.")
                else:
                    print("Paciente no encontrado.")
                    
        elif opcion == 4:
                cedula = input("Ingrese la cédula del paciente: ")
                if sis.verificarPaciente(cedula):
                    print(pac)
                else:
                    print("Paciente no encontrado.")
        elif opcion == 5:
                cedula = input("Ingrese la cédula del paciente a guardar: ")
                sis.cargarguardar(cedula)

        elif opcion == 6:
                print("Saliendo del sistema...")
                break
        else:
            print("Opción no válida.")

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main()