class Votaciones:
    def __init__(self):
        # Inicialización de atributos de la clase
        self.votantes = {}  # Diccionario para almacenar información de los votantes (clave: ID, valor: información del votante)
        self.votantesQueYavotaron = set()  # Conjunto para almacenar IDs de votantes que ya han votado
        self.candidatos = ['Juan Martines #10', 'Marcela Andrade #07', 'Agustin Olivares #25', 'Voto en blanco']  # Lista de candidatos
        self.votos = {candidato: 0 for candidato in self.candidatos}  # Diccionario para almacenar los votos por candidato (inicializado a 0)

    def registroVotante(self):
    # Método para registrar un votante
        Id = input("Ingrese el numero del documento de Identidad: ")  # Solicita al usuario ingresar su número de documento de identidad
        nombre = input("Ingrese el nombre y apellidos completos: ").lower()  # Solicita al usuario ingresar su nombre y apellidos completos
        self.votantes[Id] = {"Nombres Completos": nombre}  # Agrega la información del votante al diccionario de votantes, usando el ID como clave
        print("Registro Guardado")  # Imprime un mensaje indicando que el registro ha sido guardado con éxito

    def validacionRegistro(self):
    # Método para validar si un votante puede votar
        Id = input("Ingrese su Numero de documento de identidad: ")  # Solicita al usuario ingresar su número de documento de identidad
        if Id in self.votantes:  # Verifica si el ID está en el diccionario de votantes
                if Id not in self.votantesQueYavotaron:  # Verifica si el votante no ha votado aún
                    self.votar(Id)  # Si el votante no ha votado, llama al método votar para permitirle votar
                else:
                    print("Usted ya ha votado. No puede votar más de una vez.")  # Imprime un mensaje indicando que el votante ya ha votado
        else:
            print("No se ha registrado en el sistema")  # Imprime un mensaje indicando que el votante no está registrado en el sistema

    def votar(self, Id):
    # Método para realizar el proceso de votación
        print("Candidatos disponibles:")
        for i, candidato in enumerate(self.candidatos, start=1):
            print(f"{i}. {candidato}")

        opcion = int(input("Seleccione el número del candidato al que desea votar: "))  # Solicita al usuario seleccionar un candidato mediante un número

        if 1 <= opcion <= len(self.candidatos):  # Verifica si la opción seleccionada está dentro del rango de candidatos
            candidato_votado = self.candidatos[opcion - 1]  # Obtiene el candidato correspondiente a la opción seleccionada
            self.votos[candidato_votado] += 1  # Incrementa el contador de votos para el candidato seleccionado
            self.votantesQueYavotaron.add(Id)  # Agrega el ID del votante a la lista de votantes que ya han votado
            print(f"¡Voto registrado por {self.votantes[Id]['Nombres Completos']}!")  # Imprime un mensaje indicando que el voto ha sido registrado exitosamente
        else:
            print("Opción no válida.")  # Imprime un mensaje indicando que la opción seleccionada no es válida
            
    def mostrarResultados(self):
    # Método para mostrar los resultados de la votación
        print("\nResultados de la votación:")
        for candidato, votos in self.votos.items():
            print(f"{candidato}: {votos} votos")  # Imprime el nombre del candidato y la cantidad de votos que ha recibido

    # Determina el candidato con el mayor número de votos
        maxVotos = max(self.votos.values())
        ganadores = [candidato for candidato, votos in self.votos.items() if votos == maxVotos]

        if len(ganadores) == 1:
        # Un solo ganador
            ganador = ganadores[0]
            print(f"\nGanador: {ganador} con {self.votos[ganador]} votos")  # Imprime el ganador y la cantidad de votos que ha recibido
        else:
        # Empate entre varios candidatos
            print("\nEmpate entre los siguientes candidatos:")
            for candidato in ganadores:
                print(f"{candidato}: {self.votos[candidato]} votos")  # Imprime el candidato y la cantidad de votos que ha recibido en caso de empate
        
        # Muestra el total de votos
        totalVotos = sum(self.votos.values())
        print(f"\nTotal de votos: {totalVotos}")

# Instancia de la clase Votaciones
votos = Votaciones()

# Bucle principal del programa
while True:
    # Muestra las instrucciones y opciones disponibles al usuario
    print("\nPor favor seguir las instrucciones")
    print("\nOpciones")
    print("1. Registro")
    print("2. Votar")
    print("3. Mostrar Resultados")
    print("4. Salir")

    # Solicita al usuario seleccionar una opción
    opcion = input("Seleccione una opción: ")

    # Evalúa la opción seleccionada por el usuario
    if opcion == '1':
        votos.registroVotante()  # Llama al método de registro de votante si la opción es '1'
    elif opcion == '2':
        votos.validacionRegistro()  # Llama al método de validación de registro y votación si la opción es '2'
    elif opcion == '3':
        votos.mostrarResultados()  # Llama al método de mostrar resultados si la opción es '3'
    elif opcion == '4':
        print("Saliendo del programa")  # Imprime un mensaje indicando que el programa está saliendo
        break  # Sale del bucle principal y termina el programa
    else:
        print("Opción no válida, elija una opción válida")  # Imprime un mensaje si la opción seleccionada no es válida

