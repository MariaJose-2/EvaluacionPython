#creamos una clase llamada votaciones
class Votaciones:
    #metodo init constructor de la clase votaciones 
    def __init__(self):
        #Inicializa un diccionario vacio para almacenar la informacion de los votantes
        self.votantes={}
        #Inicializa una lista para almacenar los candidatos
        self.candidatos=['Juan Martines #10','Marcela Andrade #07', 'Agustin Olivares #25']

#metodo para registrar un votante con su informacion
    def registroVotante(self):
         #Solicita al votante ingresar su Id (identificacion, numero de documento)
        Id = input("Ingrese el numero del documento de Identidad: ")
        #Solicita al votante ingresar sus nombres y apellidos completos
        nombre = input("Ingrese el nombre y apellidos completo: ").lower()
        #se almacena la informacion de vontantes en el diccionario llamado votantes
        self.votantes[Id] = {"Nombres Completos": nombre}
        #imprime un mensaje indicando que se ha registrado correctamente
        print("Registro Guardado")
        
#metodo para validar si el votante se encuentra registrado en el sistema pasra asi poder pasar a la segunda opcion de votar
    def validacionRegistro(self):
        Id = input("Ingrese su Numero de documento de identidad: ")
        if Id in self.votantes:
            self.votantes(Id)
        else:
            print("No se ha registrado en el sistema")

#se crea una instancia de la clase Votaciones con el nombre de votos
votos = Votaciones()

#se crea un bucle principal del programa
while True:
    #Imprime el menu de opciones para el usuario
    print("\nOpciones")
    print("1. Registro")
    print("2. votar")
    print("3. Salir")
    
    #Solicita al votante seleccionar una opcion del menu
    opcion = input("Seleccione una opcion: ")

    #Evalua la opcion seleccionada por el votante y realiza la accion correspondiente
    if opcion == '1':
        #llama la instancia 'votos' y el nombre del metodo 'registroVotante'
       votos.registroVotante()

    elif opcion == '2':
        #llama la instancia 'votos' y el nombre del metodo 'validacionRegistro'
       votos.validacionRegistro()

    elif opcion == '3':
        #Imprime un mensaje indicando que el votante salio del programa y sale del bucle
        print("Salio del programa")
        break #termina el programa
    else:
        #Imprime un mensaje indicando que la opcion seleccionada por el votante no es valida
        print("Opcion no valida, elija una opcion valida")