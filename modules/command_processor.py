def procesar_comando(text, estado_label, resultado_label, ventana):
    """Procesa el texto reconocido y actualiza la GUI según el comando."""
    text = text.lower().strip()
    if "enciende" in text:
        estado_label.config(text="Motor: ON", bg="#00cc00", fg="black")
        resultado_label.config(text="✅ Motor encendido") 
    elif "apaga" in text:
        estado_label.config(text="Motor: OFF", bg="#333", fg="white")
        resultado_label.config(text="🛑 Motor apagado") 
    elif "salir" in text:
        resultado_label.config(text="👋 Cerrando programa...") 
        ventana.after(1000, ventana.destroy)
    elif text == "":
        resultado_label.config(text="❌ No se detectó voz clara.") 
    else:
        resultado_label.config(text=f" Comando no reconocido: {text}") 