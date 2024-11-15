#crear la ventana de la interfaz grafica
ckt.set_appearance_mode("dark") #modo oscuro por defecto
ckt.set_default_color_theme("blue") #Tema azul por defecto

window = ckt.CTk() #Usar CTk en lugar de Tk
window.title("CONTROL PIC")
window.geometry("1250x840) # largo - ancho
def on_meassage(client, userdate, message):
   try: 
      temperature = float(message.payload.decode("utf-8"))
      temp_queue.put(temperature)
   except ValueError:
      print(f"Error de conversion: {message.payload.decode('utf-8')}

def connect_mqtt():
   global broker_address, port, topic
   broken_address = broken_entry.get()

                
             
