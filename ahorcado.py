import random
import string
import pickle

class Jugador:
    
    def __init__(self, nombre):
        self.nombre=nombre
        self.puntuacion=0
    
    def getNombre(self):
        return self.nombre
    def getPuntuacion(self):
        return self.puntuacion
    def setPuntuacion(self,valor):
        self.puntuacion=valor
    
""" class PC (Jugador):
    def __init(self, nombre):
        super.__init__(nombre)
        self.puntuacion=0 """

def ahorcado():
    
    listapalabras= ["apoyo","cerrar","imaginacion","amenaza","toque","viernes","hayan","roto","piloto","marca","combate","manejar","seccion","profundo","tantos","conocido","serie","contrato","americano","paseo","aviones","balas","repente","cambia","tropas","uso","detener","sabia","negra", "selva","museo","racismo","tractor","prensa","inspeccion"]
    palabraelegida= random.choice(listapalabras)
    letras_palabra=set()
    alfabeto= set(string.ascii_letters)
    letras_usadas=set()
    errores=0
    puntos_juego=0
    
    jugador1 = Jugador(input("Ingrese su nombre: "))

    print("Palabra: ")
    
    for letra in palabraelegida:
        letras_palabra.add(letra)
    
    while errores<6 and len(letras_palabra) >0:
        lista_mostrar=[]
        print("\nIntentos fallidos: ",errores)
        if len(letras_usadas)>0:
            print("\nLetras usadas: ",', '.join(letras_usadas))

        for letra in palabraelegida:  
            if letra in letras_usadas:
                lista_mostrar.append(letra)
            else:
                lista_mostrar.append("_")
        
        #lista_mostrar=[letra if letra in letras_usadas else '_' for letra in palabraelegida]

        print(' '.join(lista_mostrar))

        letraj= input("\nIngrese una letra: ")

        if letraj in alfabeto and letraj not in letras_usadas:
            letras_usadas.add(letraj)
            if letraj in letras_palabra:
                letras_palabra.remove(letraj)
                puntos_juego+=1 
            else:
                print("Letra incorrecta")
                errores+=1
                puntos_juego-=1 
        elif(letraj not in alfabeto):
            print("Letra inválida")
        elif(letraj in letras_usadas):
            print("Letra ya utilizada")
        

        

    if len(letras_palabra) == 0:
        print("\n",palabraelegida.upper())
        jugador1.setPuntuacion(puntos_juego)
        print(f'\nGanaste {jugador1.getNombre()}!')
    else:
        print("\nPerdiste.")

    print(f'\nTu puntuación es {jugador1.getPuntuacion()}')
    respuesta = input("¿Desea guardar su puntuación? SI(s) o NO (n): ")
    if respuesta == 's':
        f = open('puntuaciones.dat', 'ab+')
        pickle.dump(jugador1,f)
        f.close()
    
    puntuaciones_totales=[]
    l = open('puntuaciones.dat','rb')
    try:
        datos = pickle.load(l)
        puntuaciones_totales.append(datos)
    except EOFError:
        pass

    print(puntuaciones_totales)
    
    print(f'Nombre: {datos.nombre} \nPuntuación: {datos.puntuacion}')
    l.close()
        
ahorcado()


        