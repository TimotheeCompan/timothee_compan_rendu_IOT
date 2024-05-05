from machine import Pin,PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de reception de signaux analogique
import time # importe dans le code la lib qui permet de gerer le temps

import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

pwm_ledRed = PWM(Pin(16, mode = Pin.OUT))
pwm_ledGreen = PWM(Pin(17, mode = Pin.OUT))
pwm_ledBlue = PWM(Pin(18, mode = Pin.OUT))
pwm_ledRed.freq(1_000) # dont la frequence est de 1000 (default)
pwm_ledGreen.freq(1_000)
pwm_ledBlue.freq(1_000)
pwm_ledRed.duty_u16(0)
pwm_ledBlue.duty_u16(0)
pwm_ledGreen.duty_u16(0)

ssid = 'iPhone de RAYMOND COMPAN'
password = 'mdppartage'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://172.20.10.6:3000/"
print(url)
print("État du WLAN avant la connexion :", wlan.isconnected())
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        test = r.json()["message"]
        print(test)  # traite sa reponse en Json
        r.close() # ferme la demande
        utime.sleep(1)
        if test == "Gryffindor":
            pwm_ledRed.duty_u16(5000)
            pwm_ledGreen.duty_u16(0)
            pwm_ledBlue.duty_u16(0)
        if test == "Ravenclaw":
            pwm_ledRed.duty_u16(0)
            pwm_ledGreen.duty_u16(0)
            pwm_ledBlue.duty_u16(5000)
        if test == "Hufflepuff":
            pwm_ledRed.duty_u16(5000)
            pwm_ledGreen.duty_u16(0)
            pwm_ledBlue.duty_u16(5000)
        if test == "Slytherin":
            pwm_ledRed.duty_u16(0)
            pwm_ledGreen.duty_u16(5000)
            pwm_ledBlue.duty_u16(0)
    except Exception as e:
        print(e)
    