import random
import string
import pickle
import sqlite3
from pprint import pprint

#base de datos para las puntuaciones
conn = sqlite3.connect('db_puntuaciones.db')
cursor= conn.cursor()
#q1='CREATE TABLE Puntuaciones (id integer PRIMARY KEY, Nombre text NOT NULL, Puntuacion integer NOT NULL);'
#conn.execute(q1)

#clase jugador
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
    
    listapalabras= ["apoyo","cerrar","imaginacion","amenaza","toque","viernes","hayan","roto","piloto","marca","combate","manejar","seccion","profundo","tantos","conocido","serie","contrato","americano","paseo","aviones","balas","repente","cambia","tropas","uso","detener","sabia","negra", "selva","museo","racismo","tractor","prensa","inspeccion","acertijo", "helicoptero","negligencia"]
    palabraelegida= random.choice(listapalabras)
    letras_palabra=set()
    alfabeto= set(string.ascii_letters)
    letras_usadas=set() #set de letras usadas
    errores=0
    puntos_juego=0
    
    jugador1 = Jugador(input("Ingrese su nombre: "))

    print("Palabra: ")
    
    for letra in palabraelegida:
        letras_palabra.add(letra)
    
    while errores<6 and len(letras_palabra) >0: #mientras haya menos de 6 intentos fallidos y la lista de letras de la palabra tenga letras se repite el input
        lista_mostrar=[] #lista que muestra las letras adivinadas y líneas en lugar de las no adivinadas
        print("\nIntentos fallidos: ",errores)
        if len(letras_usadas)>0:
            print("\nLetras usadas: ",', '.join(letras_usadas))

        for letra in palabraelegida:  
            if letra in letras_usadas:
                lista_mostrar.append(letra) #si es correcta se agrega la letra a la lista mostrar 
            else:
                lista_mostrar.append("_") #sino se agrega una línea
        
        #lista_mostrar=[letra if letra in letras_usadas else '_' for letra in palabraelegida]

        print(' '.join(lista_mostrar))

        letraj= input("\nIngrese una letra: ")

        if letraj in alfabeto and letraj not in letras_usadas: #si el carácter es correcto y no fue usado se evalúa
            letras_usadas.add(letraj)
            if letraj in letras_palabra: #si la letra es correcta se saca una letra de la lista de caracteres de la palabra para poder terminar el juego cuando todas hayan sido adivinadas
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
        

        
 ############### evaluación puntaje ###############
    if len(letras_palabra) == 0: 
        print("\n",palabraelegida.upper())
        jugador1.setPuntuacion(puntos_juego)
        print(f'\nGanaste {jugador1.getNombre()}!')
    else:
        print("\nPerdiste.")

    print(f'\nTu puntuación es {jugador1.getPuntuacion()}')
    respuesta = input("¿Desea guardar su puntuación? SI(s) o NO (n): ")
    
    if respuesta == 's':
        q2=f'INSERT into Puntuaciones(Nombre,Puntuacion) VALUES("{jugador1.getNombre()}",{jugador1.getPuntuacion()});'
        cursor.execute(q2)
        conn.commit()

    q3 = 'SELECT * FROM Puntuaciones;'
    cursor.execute(q3)
    print('Puntuaciones: \n' )
    for fila in cursor.fetchall():
        print('Nombre: ', fila[1],'\n',
              'Puntuación: ', fila[2])
    
    """ if respuesta == 's':
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
    l.close() """
         
    
    
if __name__ == '__main__':
    ahorcado()



        