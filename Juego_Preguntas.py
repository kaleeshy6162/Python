bienvenida = """Bienvenida al 🔎 “Algoritmo de la verdad” 👩🏼‍💻 : un juego en el que tendrás que demostrar tus dotes
de data analyst(o detective)🕵🏽‍♀️ y discernir entre la realidad ✅ y la mentira 🤥"""
presentación = """Verás 10 preguntas con 4 opciones con UNA sola respuesta que es CORRECTA (que puede ser VERDAD O MENTIRA).
¡Pero ojo cuidao!👀 No todo es lo que parece y en este juego… ¡Mucho menos!🤯 """
start = "PressEnter"

print(bienvenida)
print("-------------------------------------------------------------------------------------------------------")
print(presentación)
print("-------------------------------------------------------------------------------------------------------")
print(start)
print("-------------------------------------------------------------------------------------------------------")

start_game = input("PressEnter")

nombre_usuario = input("¿Quién se va a poner a prueba? 🧐 Dinos tu nombre🫵🏼:")

print(f"Ahora sí que sí...🥁🥁🥁 {nombre_usuario} ¡Estamos ready para empezar el “Algoritmo de la verdad”!🚀🚀🚀")
print("-------------------------------------------------------------------------------------------------------")

# Hacemos un diccionario de secciones para que guarde las preguntas agrupadas:
secciones = {
    "Sección 1: LA REALIDAD SUPERA A LA FICCIÓN, ¿O NO?": {
        1: {
            "pregunta": " - ¿Cuál de estas historias sobre inteligencia artificial es VERDAD?🤖",
            "respuestas": {
                "a)": "Una IA escribió una novela que ganó un premio literario en Japón.",
                "b)": "Una IA fue nombrada CEO de una empresa tecnológica en Silicon Valley.",
                "c)": "Un programa de IA creó una obra de arte vendida por millones de dólares en una subasta.",
                "d)": "Un robot con IA ganó una competición de ajedrez contra el campeón mundial sin entrenamiento previo."
            },
            "opcion_correcta": "c",
            "respuesta_correcta": "C. En 2018, una obra creada por IA se vendió en una subasta por 432.500 dólares.💸"
        },
        2: {
            "pregunta": " - ¿Cuál de estas noticias sobre avances médicos es MENTIRA 👩🏻‍⚕️?",
            "respuestas": {
                "a)": "Un científico chino modificó genéticamente a dos bebés para que sean inmunes al VIH.",
                "b)": "En 2025, se espera que los órganos impresos en 3D estén disponibles para trasplantes humanos.",
                "c)": "Un hospital en Alemania curó una enfermedad genética rara mediante terapia de genes.",
                "d)": "Un equipo en Islandia logró clonar un mamut utilizando ADN prehistórico."
            },
            "opcion_correcta": "d",
            "respuesta_correcta": "D. Aunque se ha investigado la clonación de mamuts, aún no se ha logrado..🦣"
        }
    },
    "Sección 2: DEMASIADO BUENO PARA SER VERDAD": {
        3: {
            "pregunta": " - ¿Cuál de estas noticias sobre animales es VERDAD?",
            "respuestas": {
                "a)": "Un perro salvó a su dueño de un incendio en su casa en Londres.",
                "b)": "Un gato fue premiado por guiar a un turista perdido en los Alpes hasta un refugio.",
                "c)": "Un delfín rescató a un grupo de buceadores en una cueva subterránea en Australia.",
                "d)": "Un elefante se unió a una protesta en defensa de los derechos animales en Tailandia."
            },
            "opcion_correcta": "b",
            "respuesta_correcta": "B. Existen reportes de un gato que guió a un turista en los Alpes hasta un lugar seguro.😻"
        },
        4: {
            "pregunta": " - ¿Cuál de estos hechos es MENTIRA?🤥",
            "respuestas": {
                "a)": "Un niño en Canadá creó un dispositivo que limpia los océanos y fue premiado por la ONU.",
                "b)": "Un proyecto en Países Bajos convierte casas abandonadas en refugios para abejas.",
                "c)": "Un grupo de jubilados en España plantó 10.000 árboles en un solo día.",
                "d)": "Un programa en Suecia permite a las personas donar su energía sobrante de paneles solares a hospitales."
            },
            "opcion_correcta": "a",
            "respuesta_correcta": "A. No existe ningún niño en Canadá que haya creado un dispositivo para limpiar océanos.🌊"
        }
    },
    "Sección 3: THE PRESENT IS FEMALE": {
        5: {
            "pregunta": " - ¿Cuál de estos logros es VERDAD?🏆",
            "respuestas": {
                "a)": "Una científica desarrolló una vacuna contra el cáncer de piel.",
                "b)": "Una ingeniera mexicana inventó una prótesis que puede ser controlada por la mente.",
                "c)": "Una activista de 16 años creó una fundación para enseñar a niñas a codificar.",
                "d)": "Una deportista de 55 años ganó una medalla de oro en natación en los Juegos Olímpicos."
            },
            "opcion_correcta": "c",
            "respuesta_correcta": "C. Alexandria Villaseñor, una activista juvenil, fundó una organización para combatir el cambio climático y para enseñar a niñas a codificar."
        },
        6: {
            "pregunta": " - ¿Cuál de estas noticias es MENTIRA 📰?",
            "respuestas": {
                "a)": "Una mujer fue elegida primera ministra de su país a los 25 años.",
                "b)": "Una activista ganó el Nobel de la Paz por sus esfuerzos en promover la educación de las niñas en África.",
                "c)": "Una astronauta pasó 1 año en el espacio sin regresar a la Tierra.",
                "d)": "Una escritora se convirtió en la mujer más joven en ganar el premio Pulitzer por una novela."
            },
            "opcion_correcta": "a",
            "respuesta_correcta": "A. No ha habido ninguna mujer elegida primera ministra a los 25 años, pero tiempo al tiempo😉"
        }
    },
    "Sección 4: ¿LEYENDAS URBANAS O REALIDADES INVEROSÍMILES?": {
        7: {
            "pregunta": " - ¿Cuál de las siguientes historias, aunque parezca inverosímil, es VERDAD?",
            "respuestas": {
                "a)": "Un hombre logró sobrevivir cayendo desde un avión sin paracaídas gracias a una pila de heno que amortiguó su caída.",
                "b)": "Un grupo de científicos descubrió un tiburón de más de 500 años nadando en el Ártico.",
                "c)": "Se reportó que un gato callejero atravesó medio país para volver con su dueño después de que lo dieron en adopción.",
                "d)": "Una mujer fue rescatada en el Himalaya por un Yeti después de quedar atrapada en una avalancha."
            },
            "opcion_correcta": "b",
            "respuesta_correcta": "B. Se descubrió un tiburón de Groenlandia que tiene más de 500 años.🦈"
        },
        8: {
            "pregunta": " - ¿Cuál de estas historias por muy creíble que parezca, es MENTIRA? 😮‍💨",
            "respuestas": {
                "a)": "Un millonario japonés compró una isla desierta para construir un parque temático inspirado en películas de terror.",
                "b)": "Un grupo de arqueólogos en América del Sur descubrió una ciudad perdida con tecnología avanzada desconocida para la época.",
                "c)": "Un magnate de Silicon Valley declaró que se está preparando para congelar su cuerpo y revivirlo en el futuro.",
                "d)": "Una tribu aislada en el Amazonas fue contactada por primera vez en 2023 tras décadas de permanecer desconocida para la humanidad."
            },
            "opcion_correcta": "b",
            "respuesta_correcta": "B. Aunque se han encontrado ruinas antiguas en América del Sur, nunca se ha descubierto una ciudad con tecnología avanzada para su época.🫠"
        }
    },
    "Sección 5: Y PARA ACABAR… ¡SE VIENE SALSEO!": {
        9: {
            "pregunta": " - ¿Cuál de las siguientes noticias, a pesar de ser surrealistas, es VERDAD?",
            "respuestas": {
                "a)": "David Bustamante anunció su retiro de la música para abrir una granja en Cantabria.",
                "b)": "Anabel Pantoja fue sorprendida organizando una quedada de fans en un karaoke en la playa, con disfraces de tiburones incluidos.",
                "c)": "Isabel Pantoja lanzará una línea de perfumes inspirados en las noches de Cantora.",
                "d)": "Kiko Rivera se ha propuesto hacer una gira nacional de DJ... ¡pero solo en bodas y bautizos!"
            },
            "opcion_correcta": "c",
            "respuesta_correcta": "C. Isabel Pantoja lanzará una línea de perfumes inspirados en las noches de Cantora.💃🏽"
        },
        10: {
            "pregunta": " - ¿Cuál de las siguientes historias sobre Belén Esteban es MENTIRA🍗?",
            "respuestas": {
                "a)": "Rompió un plato en directo durante una discusión acalorada en televisión.",
                "b)": "Participó en una campaña para defender el uso de protectores solares.",
                "c)": "Hizo un directo accidental en Instagram mientras dormía.",
                "d)": "Fue acusada de tener problemas con la seguridad del aeropuerto por llevar un perfume en la maleta."
            },
            "opcion_correcta": "b",
            "respuesta_correcta": "B. Belén nunca participó en una campaña de protectores solares. Las demás son reales.😱"
        }
    }
}

# Añadimos el puntaje a 0: 
puntaje = 0

# Recorremos las secciones: 
for nombre_seccion, preguntas in secciones.items():
    print(f"--- {nombre_seccion} ---")
    input("Dale al Enter para ponerte a prueba 🤓 con esta sección...")
    
    # Recorremos las preguntas dentro de cada sección
    for numero, pregunta_actual in preguntas.items():
        print(pregunta_actual["pregunta"])
        print("--")
        for letra, respuesta in pregunta_actual["respuestas"].items():
            print(f"{letra} {respuesta}")
        
        respuesta_usuario = input("Esoge la respuesta... ¿Será la correcta? (a, b, c, d): ").lower()

        # Añadimos un bucle while para que hasta que la letra introducida no sea válida, te siga pidiendo una respuesta
        while respuesta_usuario not in ["a", "b", "c", "d"]:
            print("Ui ⛓️‍💥 creo que no estás poniendo una letra válida🤯")
            respuesta_usuario = input("Otra oportunidad... ¿Será la correcta? (a, b, c, d): ").lower()

        # Verificamos si la respuesta es correcta
        if respuesta_usuario == pregunta_actual["opcion_correcta"]:
            print("Esto es... CORRECTO 😎 Cada vez te acercas más a superar al Algoritmo de la verdad.")
            puntaje += 1  # Suma 1 punto si la respuesta es correcta
        else:
            print(f"Esto es... INCORRECTO 🤧 La respuesta correcta es: {pregunta_actual['respuesta_correcta']}.")
        
        # Mostrar la respuesta correcta siempre
        print(f"La respuesta correcta es: {pregunta_actual['respuesta_correcta']}.")

        print("-------------------------------------------------------------------------------")
        input("Dale al Enter para seguir poniéndote a prueba🤓")

# Mostrar el puntaje final
print(f"Bueno, bueno, bueno... Has conseguido {puntaje} puntos. ¿Estás satisfecha con el resultado?😌")

# Personalizamos los mensajes según los puntos obtenidos en puntaje
if puntaje == 10:
    print(f"Podemos llamarte {nombre_usuario}, pero creemos que te pega más: 👑 REINA DEL ALGORITMO DE LA VERDAD 👑👏🏼👏🏼👏🏼")
elif puntaje >= 7:
    print("¡Vaya crack!, how wonderful life is, now you're in the world🎶🫶🏼")
elif puntaje >= 4:
    print("Es un raspao pero, oye, lo importante es participar, ¿no?😉")
else:
    print("¡No te vengas abajo, seguro que a la próxima lo petas💪🏼")
