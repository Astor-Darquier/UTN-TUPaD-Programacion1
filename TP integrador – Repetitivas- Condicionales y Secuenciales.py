#ACTIVIDAD 1 - “Caja del Kiosco”

while True:
    nombre = input ("nombre del cliente:  ").strip()
    if nombre.isalpha() and nombre!= "":
        break
    print("error: solo letras y no puede quedar vacio")
while True: 
    cant_str = input ("cantidad de productos: ").strip()
    if cant_str.isdigit() and int(cant_str) > 0:
        break
    print("error: tiene que ser un numero entero positivo")

total_sin = 0
total_con = 0.0

for i in range (1, int(cant_str) +1):
    while True: 
        precio_str = input(f"producto {i} - precio: ").strip()
        if precio_str.isdigit():
            precio = int(precio_str)
            break
        print("Error: precio de ser numerro entero")
    while True:
        desc = input(f"Producto {i} - descuento (s/n): ").strip().lower()
        if desc in ("s", "n"):
            break
    if desc == "s":
        precio_final = precio *0.9
    else:
        precio_final = precio
    
    total_sin += precio
    total_con += precio_final

ahorro = total_sin - total_con
promedio = total_con / int(cant_str)

print(f"total sin descuento: ${total_sin:.2f}")
print(f"total con descuento: ${total_con:.2f}")
print(f"ahorro: ${ahorro:.2f}")
print(f"promedio por producto: ${promedio:.2f}")  

#ACTIVIDAD 2 - “Acceso al Campus y Menú Seguro”

usuario_correcto = "alumno"
contraseña_correcta = "python123"
intentos = 0
acceso = False    

while intentos < 3:
    intentos += 1
    print(f"Intento {intentos}/3")
    usuario = input ("Usuario: ").strip()
    clave = input ("Clave: ").strip()

    if usuario == usuario_correcto and clave == contraseña_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales incorrectas.")

if not acceso:
    print("Cuenta Bloqueada")
else:
    while True:
        print("1) Estado 2) Cambiar clave 3) Mensaje 4 ) Salir")
        while True: 
            opcion_str = input ("opcion: ").strip()
            if opcion_str.isdigit():
                opcion = int(opcion_str)
                if 1 <= opcion <= 4:
                    break
                else:
                    print("Error: Opcion fuera de rango")
            else:
                print("Error: ingrese un numero valido")
        if opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            while True:
                nueva_clave = input("Nueva clave: ").strip()
                if len(nueva_clave) >= 6:
                    confirmacion = input("Confirmar nueva clave: ").strip()
                    if nueva_clave == confirmacion:
                        contraseña_correcta = nueva_clave
                        print("Clave cambiada exitosamente.")
                        break
                    else:
                        print("Error: Las claves no coinciden.")
                else:
                    print("Error: La clave debe tener al menos 6 caracteres.")
        elif opcion == 3:
            print("Bienvenido al campus virtual")
        elif opcion == 4:
            print("Saliendo del sistema...")
            break

#ACTIVIDAD 3 - “Agenda de Turnos con nombres"

while True:
    operador = input("Nombre del operador: ").strip()
    if operador.isalpha() and operador != "":
        break
    print("Error: solo letras y no puede quedar vacío")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

while True:
    print("1. Reservar turno")
    print("2. Cancelar turno (por nombre)")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    while True:
        opcion_str = input("Opción: ").strip()
        if opcion_str.isdigit():
            opcion = int(opcion_str)
            if 1 <= opcion <= 5:
                break
            else:
                print("Error: opción fuera de rango.")
        else:
            print("Error: ingrese un número válido.")
    if opcion == 1:  
        while True:
            dia_str = input("Elegir día (1=Lunes, 2=Martes): ").strip()
            if dia_str.isdigit() and int(dia_str) in [1, 2]:
                dia = int(dia_str)
                break
            print("Error: ingrese 1 o 2")
        while True:
            paciente = input("Nombre del paciente: ").strip()
            if paciente.isalpha() and paciente != "":
                break
            print("Error: solo letras y no puede quedar vacío")    
        repetido = False
        if dia == 1:
            if (paciente == lunes1 or paciente == lunes2 or 
                paciente == lunes3 or paciente == lunes4):
                repetido = True
        else:
            if (paciente == martes1 or paciente == martes2 or paciente == martes3):
                repetido = True
        
        if repetido:
            print("Error: el paciente ya tiene turno ese día")
            continue
        guardado = False
        if dia == 1:
            if lunes1 == "":
                lunes1 = paciente
                guardado = True
            elif lunes2 == "":
                lunes2 = paciente
                guardado = True
            elif lunes3 == "":
                lunes3 = paciente
                guardado = True
            elif lunes4 == "":
                lunes4 = paciente
                guardado = True
        else:
            if martes1 == "":
                martes1 = paciente
                guardado = True
            elif martes2 == "":
                martes2 = paciente
                guardado = True
            elif martes3 == "":
                martes3 = paciente
                guardado = True
        
        if guardado:
            print("Turno reservado exitosamente")
        else:
            print("Error: el día está completo")
    elif opcion == 2: 
        while True:
            dia_str = input("Elegir día (1=Lunes, 2=Martes): ").strip()
            if dia_str.isdigit() and int(dia_str) in [1, 2]:
                dia = int(dia_str)
                break
            print("Error: ingrese 1 o 2")
        while True:
            paciente = input("Nombre del paciente: ").strip()
            if paciente.isalpha() and paciente != "":
                break
            print("Error: solo letras y no puede quedar vacío")
        cancelado = False
        if dia == 1:
            if paciente == lunes1:
                lunes1 = ""
                cancelado = True
            elif paciente == lunes2:
                lunes2 = ""
                cancelado = True
            elif paciente == lunes3:
                lunes3 = ""
                cancelado = True
            elif paciente == lunes4:
                lunes4 = ""
                cancelado = True
        else:
            if paciente == martes1:
                martes1 = ""
                cancelado = True
            elif paciente == martes2:
                martes2 = ""
                cancelado = True
            elif paciente == martes3:
                martes3 = ""
                cancelado = True
        
        if cancelado:
            print("Turno cancelado exitosamente")
        else:
            print("Paciente no encontrado en ese día")
    
    elif opcion == 3:
        while True:
            dia_str = input("Elegir día (1=Lunes, 2=Martes): ").strip()
            if dia_str.isdigit() and int(dia_str) in [1, 2]:
                dia = int(dia_str)
                break
            print("Error: ingrese 1 o 2")
        
        if dia == 1:
            print("\nAgenda Lunes:")
            print(f"Turno 1: {lunes1 if lunes1 else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 else '(libre)'}")
        else:
            print("\nAgenda Martes:")
            print(f"Turno 1: {martes1 if martes1 else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 else '(libre)'}")
    
    elif opcion == 4:  
        ocup_lunes = 0
        if lunes1 != "": ocup_lunes += 1
        if lunes2 != "": ocup_lunes += 1
        if lunes3 != "": ocup_lunes += 1
        if lunes4 != "": ocup_lunes += 1
        disp_lunes = 4 - ocup_lunes
        
        ocup_martes = 0
        if martes1 != "": ocup_martes += 1
        if martes2 != "": ocup_martes += 1
        if martes3 != "": ocup_martes += 1
        disp_martes = 3 - ocup_martes
        
        print(f"\nLunes - Ocupados: {ocup_lunes} | Disponibles: {disp_lunes}")
        print(f"Martes - Ocupados: {ocup_martes} | Disponibles: {disp_martes}")
        
        if ocup_lunes > ocup_martes:
            print("Día con más turnos: Lunes")
        elif ocup_martes > ocup_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate entre Lunes y Martes")
    
    elif opcion == 5:
        print(f"Sistema cerrado. Hasta luego, {operador}!")
        break

#ACTIVIDAD 4 - “Escape Room: La Bóveda”

while True:
    nombre = input("Nombre del agente: ").strip()
    if nombre.isalpha() and nombre != "":
        break
    print("Error: solo letras y no puede quedar vacío")

print(f"Bienvenido, agente {nombre}. Tienes 100 de energía y 12 horas. ¡Abre la bóveda!\n")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0 

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVADA' if alarma else 'DESACTIVADA'} | Código parcial: {codigo_parcial}")

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    while True:
        opcion_str = input("Opción: ").strip()
        if opcion_str.isdigit():
            opcion = int(opcion_str)
            if 1 <= opcion <= 3:
                break
            else:
                print("Error: opción fuera de rango.")
        else:
            print("Error: ingrese un número válido.")
    
    if opcion == 1: 
        if racha_forzar == 2:
            energia -= 20
            tiempo -= 2
            print("¡La cerradura se trabó por forzar demasiado! Alarma activada.")
            alarma = True
            racha_forzar = 0
        else:
            energia -= 20
            tiempo -= 2
            
            if energia < 40:
                while True:
                    num_str = input("Riesgo de alarma! Elige 1-3: ").strip()
                    if num_str.isdigit() and int(num_str) in [1, 2, 3]:
                        num = int(num_str)
                        break
                    print("Error: ingrese 1, 2 o 3")
                if num == 3:
                    alarma = True
            
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta con fuerza!")
            
            racha_forzar += 1  
    
    elif opcion == 2:  
        energia -= 10
        tiempo -= 3
        print("Iniciando hackeo del panel...")
        for paso in range(1, 5):
            print(f"Paso {paso}/4: Conectando...")
            codigo_parcial += "A"
        print("Hackeo completado! Código parcial:", codigo_parcial)
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Cerradura abierta automáticamente por el código!")
        racha_forzar = 0 
    
    elif opcion == 3: 
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        print("Descansando... Energía recuperada.")
        if alarma:
            energia -= 10
            print("¡La alarma drena energía extra!")
        racha_forzar = 0
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("¡Sistema bloqueado por alarma y poco tiempo! Derrota.")
        break
    
    if energia <= 0 or tiempo <= 0:
        print("¡Energía o tiempo agotados! Derrota.")
        break
if cerraduras_abiertas == 3:
    print("\n¡VICTORIA! Has abierto las 3 cerraduras. ¡La bóveda es tuya!")
else:
    print("\nDerrota. La misión ha fallado.")

#ACTIVIDAD 5 - “Escape Room:"La Arena del Gladiador"

while True:
    nombre = input("Nombre del Gladiador: ").strip()
    if nombre.isalpha() and nombre != "":
        break
    print("Error: Solo se permiten letras")

print(f"=== INICIO DEL COMBATE ===\n")
hp_jugador = 100
hp_enemigo = 100
pociones = 3
dano_pesado = 15
dano_enemigo = 12
while hp_jugador > 0 and hp_enemigo > 0:
    print(f"{nombre} (HP: {hp_jugador}) vs Enemigo (HP: {hp_enemigo}) | Pociones: {pociones}")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    while True:
        opcion_str = input("Opción: ").strip()
        if opcion_str.isdigit():
            opcion = int(opcion_str)
            if 1 <= opcion <= 3:
                break
            else:
                print("Error: ingrese un número válido.")
        else:
            print("Error: ingrese un número válido.")
    
    if opcion == 1:
        if hp_enemigo < 20:
            dano = dano_pesado * 1.5
        else:
            dano = dano_pesado
        hp_enemigo -= dano
        print(f"¡Atacaste al enemigo por {dano} puntos de daño!")
    
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for _ in range(3):
            hp_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
    
    elif opcion == 3:
        if pociones > 0:
            hp_jugador += 30
            pociones -= 1
            print("¡Te curaste 30 puntos!")
        else:
            print("¡No quedan pociones!")
    if hp_jugador > 0 and hp_enemigo > 0:
        hp_jugador -= dano_enemigo
        print("¡El enemigo te atacó por 12 puntos de daño!")
    
    print("=== NUEVO TURNO ===")
if hp_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")