import time
import logging
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
from pyvirtualdisplay import Display
from time import sleep
from selenium import webdriver

display = Display(visible=0, size=(800,600))
display.start()

logging.basicConfig(level=logging.DEBUG)

#driver = WhatsAPIDriver()
driver = WhatsAPIDriver(username="agrumcito",profile='/home/agrum-user/Projects/visor-whatsapp-api/MozProfile',headless=True)
print("Waiting for QR")
#driver.get_qr()
driver.wait_for_login()

print("Bot started")

while True:
    time.sleep(3)
    print('Checking for more messages')
    for contact in driver.get_unread():
        for message in contact.messages:
            if isinstance(message, Message):  # Currently works for text messages only.
                contact.chat.send_message(message.safe_content)

