# First of all, install the toast notification library this way:
# python -m pip install win10toast

#----------------------------------------------------------------

# Now we import the toast library and time library
from win10toast import ToastNotifier
import time

# Now we initialize the toaster
toaster = ToastNotifier()

# Show notifications every certain time

# Declare notification variable time
timeNotif = 2

# Now we create the notification
toaster.show_toast("Notification!",  # Title
                    "This is an alert!!! Wiii!", # Body
                    threaded=True,
                    icon_path=None, # Icon
                    duration = timeNotif )

# Now we hold the notification there
while toaster.notification_active():
    time.sleep(0.3)
