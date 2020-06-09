# Primero, instalamos la libreria de notificaciones toast, de esta forma:
# python -m pip install win10toast

#----------------------------------------------------------------

# Importamos la libreria instalada y la libreria por defecto del tiempo
from win10toast import ToastNotifier
import time

# Iniciamos toaster
toaster = ToastNotifier()

# Declaramos una variable con los segundos en los que se repite una notificacion
timeNotif = 2

# Creamos la notificacion
toaster.show_toast("Notification!",  # Titulo
                    "This is an alert!!! Wiii!", # Mensaje
                    threaded=True,
                    icon_path=None, # Icono
                    duration = timeNotif ) # Llamamos a la variable del tiempo

# Retenmos la notificación haciendola dormir unos segundos(hasta darle click)
while toaster.notification_active():
    time.sleep(0.3)
