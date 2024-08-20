from plyer import notification
import time

print("if you have to continue program\n"
      "then run the program and minimize the window\n"
      "for close program colse the window ") 
 
notification_title = "water"
notification_message = 'take a break and dirnk a glass of water!.' 


while True:
    time.sleep(3)
    notification.notify(  
        title = notification_title,  
        message = notification_message,  
        timeout = 3,  
        toast = False  
        )
              