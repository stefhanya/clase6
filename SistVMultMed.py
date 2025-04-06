import datetime
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def validarFecha(self, fecha_str):
        try:
            datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
            return True
        except ValueError:
            print("Fecha inválida. Usa el formato dd/mm/aaaa.")
            return False
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
    def eliminarMedicamento(self,d):
        while True:
            print('MEDICAMENTOS DE LA MASCOTA')
            print(d.__verLista_Medicamentos)
            x=input('Ingrese el nombre del medicamento a eliminar:')
            if x in d.__lista_Medicamentos:
                d.__lista_medicamentos.remove(x) 
                return True
            else:
                print('El medicamento no corresponde a los disponibles, Ingrese de nuevo...')
                continue
    def verificarMedicamento(self, nombre_medicamento):
        for med in self.__lista_medicamentos:
            if med.verNombre() == nombre_medicamento:
                return True
        return False

    

class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
        self.__dict_canino={}
        self.__dict_felino={}
    
    def ingresar_dictCanFelino(self, mascota):
        tipo = mascota.verTipo()
        if tipo == '1':
            self.__dict_felino[mascota.verHistoria()] = mascota
        elif tipo == '2':
            self.__dict_canino[mascota.verHistoria()] = mascota

    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None
    
    def verCaninoFelino(self):
        print('-------FELINOS--------')
        for mascota in self.__dict_felino.values():
            print(f"- {mascota.verNombre()}")
        print('-------CANINOS--------')
        for mascota in self.__dict_canino.values():
            print(f"- {mascota.verNombre()}")

        
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)

                if masc.verTipo() == "1":
                    if historia in self.__dict_felino:
                        del self.__dict_felino[historia]
                elif masc.verTipo() == "2":
                    if historia in self.__dict_canino:
                        del self.__dict_canino[historia]

                return True  # Eliminado con éxito
        return False  # No se encontró

    def verMedicamento(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos()
        return None


def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            while True:

                if servicio_hospitalario.verNumeroMascotas() >= 10:
                    print("No hay espacio ...") 
                    continue
                historia=int(input("Ingrese la historia clínica de la mascota: "))
                #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
                if servicio_hospitalario.verificarExiste(historia) == False:
                    nombre=input("Ingrese el nombre de la mascota: ")
                    while True:
                        tipo = input("Ingrese el tipo de mascota (1. felino o 2. canino): ")
                        if tipo == "1" or tipo == "2":
                            break
                        else:
                            print("OPCIÓN NO VÁLIDA. Intente nuevamente.")
                    peso=int(input("Ingrese el peso de la mascota: "))
                    
                    mas= Mascota()
                    mas.asignarNombre(nombre)
                    mas.asignarHistoria(historia)
                    mas.asignarPeso(peso)
                    mas.asignarTipo(tipo)
                    while True:
                            fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                            if mas.validarFecha(fecha):
                                mas.asignarFecha(fecha)
                                nm = int(input("¿Cuántos medicamentos desea registrar?: "))
                                lista_med=[]

                                for i in range(nm):
                                    nm = input(f"Ingrese el nombre del medicamento #{i+1}: ")
                                    
                                    if mas.verificarMedicamento(nm):
                                        print("\n<< Ese medicamento ya está siendo administrado a la mascota, ingrese uno nuevo >>".upper())
                                    else:
                                        dosis = int(input("Ingrese la dosis: "))
                                        medicamento = Medicamento()
                                        medicamento.asignarNombre(nm)
                                        medicamento.asignarDosis(dosis)
                                        # Lo agregas directamente a la lista de la mascota
                                        mas.verLista_Medicamentos().append(medicamento)
                                break

                            else:
                                continue
                    
                    servicio_hospitalario.ingresarMascota(mas)
                    servicio_hospitalario.ingresar_dictCanFelino(mas)

                    print('---MASCOTA INGRESADA CON EXITO---')
                    break
                else:
                    print("Ya existe la mascota con el numero de historia clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))
            servicio_hospitalario.verCaninoFelino()

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            x=input('''Desea salir?
                   1. SI 
                   2. NO
                   ''')
            if x=='1':
                print("Usted ha salido del sistema de servicio de hospitalización...")
                break
            elif x=='2':
                print('Regresó al sistema----')
                continue
            else:
                print("Usted ingresó una opción no válida, intentelo nuevamente...")
                continue

        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

