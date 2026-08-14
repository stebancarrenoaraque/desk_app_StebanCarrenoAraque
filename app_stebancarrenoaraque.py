# --------------------------------------------------
# Desktop app No. 3 - Perfil Personal y Proyecto
# --------------------------------------------------

from tkinter import *
from tkinter import messagebox


COLOR_VENTANA = "#18181B"   
COLOR_FRAME = "#27272A"     
COLOR_TEXTO = "#F4F4F5"     
COLOR_BOTON_BG = "#3F3F46"  
COLOR_BOTON_FG = "#F4F4F5"  
COLOR_SALIR_BG = "#E11D48"  
COLOR_SALIR_FG = "#FFFFFF"  

# --------------------------------------------------
# ventana principal de la app
# --------------------------------------------------

ventana_principal = Tk()
ventana_principal.title("Perfil Personal - Informacion")
ventana_principal.geometry("500x520")
ventana_principal.resizable(False, False)
ventana_principal.config(bg=COLOR_VENTANA)

# --------------------------------------------------
# funcion para abrir ventanas secundarias
# --------------------------------------------------

def mostrar_info(titulo, mensaje, ruta_imagen=None):
    ventana_secundaria = Toplevel(ventana_principal)
    ventana_secundaria.title(titulo)
    # Aumentamos un poco la altura a 300 para que quepa bien la foto y el texto
    ventana_secundaria.geometry("320x300")
    ventana_secundaria.resizable(False, False)
    ventana_secundaria.config(bg=COLOR_VENTANA)
    
    ventana_secundaria.grab_set()

    # Frame interno
    frame_secundario = Frame(ventana_secundaria, bg=COLOR_FRAME)
    frame_secundario.place(x=10, y=10, width=300, height=280)

    # --- AGREGAR IMAGEN PNG ---
    if ruta_imagen:
        try:
            # Cargar imagen .png con PhotoImage nativo
            img = PhotoImage(file=ruta_imagen)
            
            # Si la imagen te queda muy grande, descomenta la siguiente línea para reducirla a la mitad:
            # img = img.subsample(2, 2)

            lbl_img = Label(frame_secundario, image=img, bg=COLOR_FRAME)
            lbl_img.pack(pady=(15, 0))
            
            # ¡TRUCO CLAVE DE TKINTER!
            # Tienes que guardar la referencia de la imagen en la etiqueta,
            # si no lo haces, Python la borra de la memoria y la ventana se verá vacía.
            lbl_img.image = img 
            
        except Exception as e:
            print(f"No se pudo cargar la imagen {ruta_imagen}: {e}")

    # Titulo interno
    lbl_titulo = Label(frame_secundario, text=titulo, bg=COLOR_FRAME, fg=COLOR_TEXTO, font=("Helvetica", 11, "bold"))
    lbl_titulo.pack(pady=(10, 5))

    # Mensaje o detalles
    lbl_mensaje = Label(frame_secundario, text=mensaje, bg=COLOR_FRAME, fg="#E4E4E7", font=("Helvetica", 10), justify="center", wraplength=260)
    lbl_mensaje.pack(pady=5)

    # Boton para cerrar
    btn_cerrar = Button(frame_secundario, text="Cerrar", command=ventana_secundaria.destroy, bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=("Helvetica", 9, "bold"), relief="flat")
    btn_cerrar.pack(pady=10)

# --------------------------------------------------
# frame entrada de datos / botones
# --------------------------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg=COLOR_FRAME, width=480, height=480)
frame_entrada.place(x=10, y=10)

# titulo de la app
titulo = Label(frame_entrada, text="Steban Carreño Araque\nINFORMACION PERSONAL", bg=COLOR_FRAME, fg=COLOR_TEXTO)
titulo.config(font=("Helvetica", 16, "bold"))
titulo.place(x=110, y=50)



# --------------------------------------------------
# botones de la app
# --------------------------------------------------

# 1. Lugar y fecha de nacimiento
bt_nacimiento = Button(frame_entrada, text="Lugar y Fecha Nacimiento 🎂", command=lambda: mostrar_info("Nacimiento", "Lugar: San Gil, Santander\nFecha: 19/06/2011","img/sangil.png"))
bt_nacimiento.config(bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=("Helvetica", 10))
bt_nacimiento.place(x=30, y=120, width=200, height=30)

# foto
cumple = PhotoImage(file="img/foto.png")
lb_cumple = Label(ventana_principal, image=cumple, bg="white")
lb_cumple.place(x=30,y=30)


# 2. Datos médicos
bt_medicos = Button(frame_entrada, text="Datos Médicos Relevantes 🩺", command=lambda: mostrar_info("Datos Médicos", "tipo de sangre: O+\nAlergias: Ninguna\nEstado: buena salud","img/datosmedicos.png"))
bt_medicos.config(bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=("Helvetica", 10))
bt_medicos.place(x=250, y=120, width=200, height=30)

# 3. Información familiar
bt_familiar = Button(frame_entrada, text="Información Familiar", command=lambda: mostrar_info("Familia", "Residencia: San Gil\nIntegrantes: papa, mama,\nmi hermano y mi hermana","img/sangil1.png"))
bt_familiar.config(bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=("Helvetica", 10))
bt_familiar.place(x=30, y=170, width=200, height=30)

# 4. Proceso educativo
bt_educacion = Button(frame_entrada, text="Proceso Educativo", command=lambda: mostrar_info("Educación", "Colegio San José de Guanentá\nGrado: Decimo (10°)\nSan Gil, Colombia","img/csjg.png"))
bt_educacion.config(bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=("Helvetica", 10))
bt_educacion.place(x=250, y=170, width=200, height=30)

# 5. Información de amigos
bt_amigos = Button(frame_entrada, text="Información de Amigos", command=lambda: mostrar_info("Amigos", "Compañeros del colegio Guanentá y amigos del barrio","img/amigos.png"))
bt_amigos.config(bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=("Helvetica", 10))
bt_amigos.place(x=30, y=220, width=200, height=30)

# 6. Hobbies y tiempo libre
bt_hobbies = Button(frame_entrada, text="Hobbies / Tiempo Libre", command=lambda: mostrar_info("Hobbies", "Estar con la familia\nVer documentales o películas de interés.\nTomar fotos con mi celular\ncocinar","img/pasatiempos.png"))
bt_hobbies.config(bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=("Helvetica", 10))
bt_hobbies.place(x=250, y=220, width=200, height=30)

# 7. Horario semanal 24/7
bt_horario = Button(frame_entrada, text="Horario Semanal 24/7", command=lambda: mostrar_info("Horario", "Lunes a Viernes: Colegio por las tardes y aveces en las mañanas y Fines de semana: Descanso","img/horario.png"))
bt_horario.config(bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=("Helvetica", 10))
bt_horario.place(x=30, y=270, width=200, height=30)

# 8. Plan preparación ICFES 2027
bt_icfes = Button(frame_entrada, text="Plan ICFES 2027", command=lambda: mostrar_info("ICFES 2027", "Refuerzo en lectura crítica","img/icfes.png"))
bt_icfes.config(bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=("Helvetica", 10))
bt_icfes.place(x=250, y=270, width=200, height=30)

# 9. Proyecto de vida 2031
bt_proyecto = Button(frame_entrada, text="Proyecto de Vida 2031", command=lambda: mostrar_info("Proyecto 2031", "Graduarme de la universidad, y apoyar a mi familia","img/proyectodevida (1).png"))
bt_proyecto.config(bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=("Helvetica", 10))
bt_proyecto.place(x=30, y=320, width=200, height=30)

# 10. Tema libre
bt_libre = Button(frame_entrada, text="Tema Libre: jugar", command=lambda: mostrar_info("Tema Libre", "jugar mi juego favorito","img/jugar1.png"))
bt_libre.config(bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=("Helvetica", 10))
bt_libre.place(x=250, y=320, width=200, height=30)

# Botón para salir
def salir():
    messagebox.showinfo("Salir", "La app se va a cerrar")
    ventana_principal.destroy()

bt_salir = Button(frame_entrada, text="Salir", command=salir)
bt_salir.config(bg=COLOR_SALIR_BG, fg=COLOR_SALIR_FG, font=("Helvetica", 10, "bold"))
bt_salir.place(x=190, y=380, width=100, height=35)

ventana_principal.mainloop()