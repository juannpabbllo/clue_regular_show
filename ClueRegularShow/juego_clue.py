import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

# ==========================================
# 1. DATOS DEL JUEGO
# ==========================================

personajes = [
    {"nombre": "Mordecai", "img": "mordecai.jpg", "desc": "Jardinero. Intenta ser responsable, pero siempre se distrae."},
    {"nombre": "Rigby", "img": "rigby.jpg", "desc": "Flojo, impulsivo y experto en tomar atajos que salen mal."},
    {"nombre": "Benson", "img": "benson.jpg", "desc": "Gerente del parque. Máquina de chicles con problemas de ira."},
    {"nombre": "Musculoso", "img": "musculoso.jpg", "desc": "Mantenimiento. Hace bromas pesadas y tiene higiene cuestionable."},
    {"nombre": "Skips", "img": "skips.jpg", "desc": "Yeti inmortal. Ha visto de todo y sabe solucionar problemas místicos."}
]

locaciones = [
    {"nombre": "Oficina de Benson", "img": "oficina.jpg", "desc": "Llena de reportes sin archivar y un ambiente tenso."},
    {"nombre": "Cafeteria", "img": "cafeteria.jpg", "desc": "Lugar ideal para evadir el trabajo comiendo alitas."},
    {"nombre": "Trailer de Musculoso", "img": "trailer.jpg", "desc": "Caótico, lleno de basura y con un olor peculiar."},
    {"nombre": "Casa de Skips", "img": "casa de skips.jpg", "desc": "Rodeada de naturaleza y artefactos antiguos."},
    {"nombre": "Garage", "img": "garage.jpg", "desc": "Lleno de herramientas y el carrito de golf."}
]

armas = [
    {"nombre": "Camiseta sudada", "img": "camiseta.jpg", "desc": "Arma biológica. Su olor asfixia al instante."},
    {"nombre": "Llave inglesa", "img": "llave.jpg", "desc": "Contundente y pesada de metal sólido."},
    {"nombre": "Pluma", "img": "pluma.jpg", "desc": "Letal si se usa como objeto punzante burocrático."},
    {"nombre": "Disco de gym", "img": "disco.jpg", "desc": "Objeto de 20 kilos, perfecto para un aplastamiento."},
    {"nombre": "Cafetera", "img": "cafetera.jpg", "desc": "Produce quemaduras o una sobredosis de cafeína."}
]

# ==========================================
# 2. LÓGICA Y DISEÑO MODERNO
# ==========================================

BG_COLOR = "#1e1e2e"       
PANEL_COLOR = "#313244"    
TEXT_COLOR = "#cdd6f4"     
ACCENT_COLOR = "#f38ba8"   
BUTTON_COLOR = "#89b4fa"   
WIN_COLOR = "#a6e3a1"      # Verde pastel para la victoria
FONT_MAIN = ("Segoe UI", 11)
FONT_TITLE = ("Segoe UI", 22, "bold")

class ClueRegularShow:
    def __init__(self, root):
        self.root = root
        self.root.title("Clue: Un Show Más")
        self.root.geometry("900x750")
        self.root.configure(bg=BG_COLOR)

        self.victima = "Papaleta"
        
        # Primero creamos toda la interfaz visual
        self.crear_interfaz()
        # Luego iniciamos las variables del primer caso
        self.iniciar_nueva_partida()

    def iniciar_nueva_partida(self):
        """Sortea todo de nuevo y limpia la interfaz para un nuevo juego"""
        self.culpable_real = random.choice(personajes)
        self.locacion_real = random.choice(locaciones)
        self.arma_real = random.choice(armas)

        # Limpiar selecciones
        self.lista_personajes.selection_clear(0, tk.END)
        self.lista_locaciones.selection_clear(0, tk.END)
        self.lista_armas.selection_clear(0, tk.END)

        # Limpiar imagen y descripción
        self.lbl_imagen.config(image='')
        self.lbl_descripcion.config(text="Selecciona un elemento de las listas para verlo aquí.")

        # Limpiar y reiniciar el panel de pistas
        self.txt_log.config(state="normal")
        self.txt_log.delete('1.0', tk.END)
        self.txt_log.insert(tk.END, f"🚨 ¡ALERTA! El cuerpo de {self.victima} ha sido hallado sin vida en el parque. Nadie sabe qué pasó. ¡Debes investigar!\n")
        self.txt_log.config(state="disabled")

    def crear_interfaz(self):
        tk.Label(self.root, text="MISTERIO EN EL PARQUE", font=FONT_TITLE, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

        main_frame = tk.Frame(self.root, bg=BG_COLOR)
        main_frame.pack(fill="both", expand=True, padx=20)

        # --- COLUMNA IZQUIERDA ---
        col_izq = tk.Frame(main_frame, bg=PANEL_COLOR, padx=15, pady=15)
        col_izq.pack(side="left", fill="both", expand=True, padx=10)

        marco_img = tk.Frame(col_izq, width=280, height=280, bg="black")
        marco_img.pack_propagate(False)
        marco_img.pack(pady=10)

        self.lbl_imagen = tk.Label(marco_img, bg="black")
        self.lbl_imagen.pack(fill="both", expand=True)

        self.lbl_descripcion = tk.Label(col_izq, text="", font=FONT_MAIN, bg=PANEL_COLOR, fg=TEXT_COLOR, wraplength=280)
        self.lbl_descripcion.pack(pady=10)

        # --- COLUMNA DERECHA (Pistas Dinámicas) ---
        col_der = tk.Frame(main_frame, bg=BG_COLOR)
        col_der.pack(side="right", fill="both", expand=True, padx=10)

        lbl_pistas = tk.Label(col_der, text="🔍 PANEL DE INVESTIGACIÓN", font=("Segoe UI", 12, "bold"), bg=BG_COLOR, fg=BUTTON_COLOR)
        lbl_pistas.pack(pady=(0, 5))

        self.txt_log = tk.Text(col_der, height=10, width=40, font=("Segoe UI", 10), bg=PANEL_COLOR, fg=TEXT_COLOR, 
                               relief="flat", wrap="word", state="disabled")
        self.txt_log.pack(pady=5)

        btn_frame = tk.Frame(col_der, bg=BG_COLOR)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="🗣 Interrogar Sospechoso Seleccionado", bg=BUTTON_COLOR, fg="black", relief="flat", 
                  font=("Segoe UI", 10, "bold"), command=self.interrogar).pack(fill="x", pady=5)
        tk.Button(btn_frame, text="📹 Inspeccionar Lugar Seleccionado", bg=BUTTON_COLOR, fg="black", relief="flat", 
                  font=("Segoe UI", 10, "bold"), command=self.inspeccionar).pack(fill="x", pady=5)
        tk.Button(btn_frame, text="🔬 Revisar Arma Seleccionada", bg=BUTTON_COLOR, fg="black", relief="flat", 
                  font=("Segoe UI", 10, "bold"), command=self.revisar).pack(fill="x", pady=5)

        # --- PANEL INFERIOR ---
        panel_listas = tk.Frame(self.root, bg=BG_COLOR)
        panel_listas.pack(pady=15)

        def crear_lista(master, titulo, datos, col):
            tk.Label(master, text=titulo, bg=BG_COLOR, fg=TEXT_COLOR, font=("Segoe UI", 12, "bold")).grid(row=0, column=col, padx=15)
            lista = tk.Listbox(master, height=5, font=FONT_MAIN, bg=PANEL_COLOR, fg=TEXT_COLOR, 
                               selectbackground=ACCENT_COLOR, relief="flat", highlightthickness=0, exportselection=False)
            for d in datos: lista.insert(tk.END, d["nombre"])
            lista.grid(row=1, column=col, padx=15, pady=5)
            lista.bind("<<ListboxSelect>>", lambda e: self.mostrar_info(lista, datos))
            return lista

        self.lista_personajes = crear_lista(panel_listas, "Sospechosos", personajes, 0)
        self.lista_locaciones = crear_lista(panel_listas, "Locaciones", locaciones, 1)
        self.lista_armas = crear_lista(panel_listas, "Armas", armas, 2)

        btn_acusar = tk.Button(self.root, text="🚨 ¡HACER ACUSACIÓN FINAL!", font=("Segoe UI", 14, "bold"), 
                               bg=ACCENT_COLOR, fg="black", relief="flat", command=self.hacer_acusacion, padx=20, pady=5)
        btn_acusar.pack(pady=5)

    def escribir_log(self, mensaje):
        self.txt_log.config(state="normal")
        self.txt_log.insert(tk.END, mensaje + "\n")
        self.txt_log.see(tk.END)
        self.txt_log.config(state="disabled")

    def mostrar_info(self, listbox, lista_datos):
        seleccion = listbox.curselection()
        if not seleccion: return
        item = lista_datos[seleccion[0]]
        
        self.lbl_descripcion.config(text=f"【 {item['nombre']} 】\n{item['desc']}")
        
        ruta_img = os.path.join(os.path.dirname(os.path.abspath(__file__)), item["img"])
        if os.path.exists(ruta_img):
            img = Image.open(ruta_img).resize((280, 280), Image.Resampling.LANCZOS)
            foto = ImageTk.PhotoImage(img)
            self.lbl_imagen.config(image=foto)
            self.lbl_imagen.image = foto
        else:
            self.lbl_imagen.config(image='', text="[ Imagen no encontrada ]", fg="white")

    # --- LÓGICA DE PISTAS DINÁMICAS ---
    def interrogar(self):
        sel = self.lista_personajes.curselection()
        if not sel:
            self.escribir_log("-> [Error] Selecciona un Sospechoso en la lista primero.")
            return
        p = personajes[sel[0]]
        es_culpable = (p == self.culpable_real)
        
        if p["nombre"] == "Mordecai": res = "Estaba trabajando solo en el jardín... creo." if es_culpable else "Estaba jugando videojuegos con Rigby, él te lo puede confirmar."
        elif p["nombre"] == "Rigby": res = "¡¿Por qué me miras a mí?! ¡No tengo nada que ver!" if es_culpable else "¡Yo no fui! Estaba dormido en el trampolín toda la tarde."
        elif p["nombre"] == "Benson": res = f"Papaleta me sacó de quicio, ¡pero yo no le haría daño!" if es_culpable else "Estaba revisando inventarios en mi computadora, no salí en horas."
        elif p["nombre"] == "Musculoso": res = "No sé de qué hablas, viejo. Yo estaba... por ahí." if es_culpable else "Estaba con Starla en el centro comercial, pregúntale a mi mami."
        elif p["nombre"] == "Skips": res = "A veces... hay que tomar decisiones difíciles por el bien del parque." if es_culpable else "Los espíritus me dijeron que esto pasaría. Yo estaba meditando."
        
        self.escribir_log(f"-> {p['nombre']}: '{res}'")

    def inspeccionar(self):
        sel = self.lista_locaciones.curselection()
        if not sel:
            self.escribir_log("-> [Error] Selecciona una Locación en la lista primero.")
            return
        l = locaciones[sel[0]]
        es_lugar = (l == self.locacion_real)
        
        if l["nombre"] == "Oficina de Benson": res = "Hay un cajón roto y marcas de zapatos recientes." if es_lugar else "No hay rastros de lucha, solo papeles de impuestos."
        elif l["nombre"] == "Cafeteria": res = "Hay una silla tirada y manchas sospechosas en el suelo." if es_lugar else "Las mesas están limpias, nadie ha entrado aquí hoy."
        elif l["nombre"] == "Trailer de Musculoso": res = "La puerta fue forzada y hay algo escondido bajo la alfombra." if es_lugar else "Apesta como siempre, pero no hay señales de un crimen."
        elif l["nombre"] == "Casa de Skips": res = "Un artefacto antiguo está fuera de su lugar." if es_lugar else "Todo está en perfecto orden zen, ni una mosca ha entrado."
        elif l["nombre"] == "Garage": res = "Falta una herramienta en el panel y hay huellas extrañas." if es_lugar else "Las herramientas están cubiertas de polvo, sin usar."
        
        self.escribir_log(f"-> {l['nombre']}: {res}")

    def revisar(self):
        sel = self.lista_armas.curselection()
        if not sel:
            self.escribir_log("-> [Error] Selecciona un Arma en la lista primero.")
            return
        a = armas[sel[0]]
        es_arma = (a == self.arma_real)
        
        if a["nombre"] == "Camiseta sudada": res = "Tiene desgarros frescos, como si alguien hubiera forcejeado." if es_arma else "Huele fatal, pero no tiene marcas de violencia."
        elif a["nombre"] == "Llave inglesa": res = "Se ven marcas de haber golpeado algo recientemente." if es_arma else "Está oxidada, hace meses que no se usa."
        elif a["nombre"] == "Pluma": res = "La punta está rota y le falta tinta de forma sospechosa." if es_arma else "Aún tiene la tapa puesta y está impecable."
        elif a["nombre"] == "Disco de gym": res = "Está tirado en el suelo, fuera de su lugar habitual." if es_arma else "Está guardado perfectamente en su estante."
        elif a["nombre"] == "Cafetera": res = "Aún está caliente y el cristal está trizado." if es_arma else "Está completamente fría, vacía y limpia."
        
        self.escribir_log(f"-> {a['nombre']}: {res}")

    def hacer_acusacion(self):
        sel_c = self.lista_personajes.curselection()
        sel_l = self.lista_locaciones.curselection()
        sel_a = self.lista_armas.curselection()

        if not sel_c or not sel_l or not sel_a:
            messagebox.showwarning("Información incompleta", "Debes seleccionar 1 sospechoso, 1 locación y 1 arma de las listas de abajo (haz clic en ellas).")
            return

        c = personajes[sel_c[0]]
        l = locaciones[sel_l[0]]
        a = armas[sel_a[0]]

        victoria = (c == self.culpable_real and l == self.locacion_real and a == self.arma_real)
        self.mostrar_pantalla_final(victoria)

    def mostrar_pantalla_final(self, victoria):
        """Crea una pantalla estilo videojuego para mostrar si ganaste o perdiste"""
        # Crear nueva ventana encima del juego
        ventana_final = tk.Toplevel(self.root)
        ventana_final.title("Fin de la Partida")
        ventana_final.geometry("700x450")
        ventana_final.configure(bg=BG_COLOR)
        ventana_final.transient(self.root) # La mantiene por encima de la principal
        ventana_final.grab_set() # Bloquea la ventana principal hasta que cierres esta

        c_nombre = self.culpable_real["nombre"]
        l_nombre = self.locacion_real["nombre"]
        a_nombre = self.arma_real["nombre"]
        v = self.victima
        
        # Historia dinámica
        historia = ""
        if c_nombre == "Benson": historia = f"Benson llegó a su límite. Persiguió a {v} hasta la {l_nombre}. Cegado por la ira, tomó el/la {a_nombre} y acabó con él."
        elif c_nombre == "Rigby": historia = f"Rigby estaba harto. En medio de una discusión con {v} en la {l_nombre}, agarró el/la {a_nombre} y atacó sin pensar."
        elif c_nombre == "Mordecai": historia = f"Mordecai estaba estresado y {v} lo arrinconó en la {l_nombre}. Usando el/la {a_nombre}, cometió el crimen."
        elif c_nombre == "Musculoso": historia = f"'¿Sabes quién más odiaba a {v}? ¡MI MAMI!'. Usó el/la {a_nombre} en la {l_nombre} para silenciarlo."
        elif c_nombre == "Skips": historia = f"Skips sabía que {v} estaba poseído. Lo citó en la {l_nombre} sabiendo que el único objeto capaz de purgarlo era el/la {a_nombre}."

        # Configuración visual dependiendo de si ganó o perdió
        if victoria:
            color_titulo = WIN_COLOR
            texto_titulo = "¡CASO RESUELTO: HAS GANADO!"
            subtitulo = "Eres un verdadero detective. Aquí está lo que pasó:"
        else:
            color_titulo = ACCENT_COLOR
            texto_titulo = "¡TE EQUIVOCASTE: HAS PERDIDO!"
            subtitulo = "¡Benson te ha despedido por mal detective!\nLa verdadera historia era esta:"

        # Elementos de la pantalla final
        tk.Label(ventana_final, text=texto_titulo, font=("Segoe UI", 26, "bold"), bg=BG_COLOR, fg=color_titulo).pack(pady=(30, 10))
        tk.Label(ventana_final, text=subtitulo, font=("Segoe UI", 12), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
        
        tk.Label(ventana_final, text=historia, font=("Segoe UI", 14, "italic"), bg=PANEL_COLOR, fg="white", 
                 wraplength=600, justify="center", padx=20, pady=20, relief="flat").pack(pady=20)

        # Botones de Acción Final
        frame_botones = tk.Frame(ventana_final, bg=BG_COLOR)
        frame_botones.pack(pady=20)

        def reiniciar():
            ventana_final.destroy()
            self.iniciar_nueva_partida()

        tk.Button(frame_botones, text="🎮 JUGAR DE NUEVO", font=("Segoe UI", 14, "bold"), bg=BUTTON_COLOR, fg="black", 
                  relief="flat", command=reiniciar, padx=20, pady=10).pack(side="left", padx=20)
        
        tk.Button(frame_botones, text="❌ SALIR DEL JUEGO", font=("Segoe UI", 14, "bold"), bg=ACCENT_COLOR, fg="black", 
                  relief="flat", command=self.root.quit, padx=20, pady=10).pack(side="right", padx=20)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = ClueRegularShow(ventana)
    ventana.mainloop()