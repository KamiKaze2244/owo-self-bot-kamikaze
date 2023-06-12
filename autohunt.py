import pyautogui
import datetime
import time


print("\n")
secim = input("Hangisini İstiyorsun (sell, sc) : ")
print("Bot Başlatılıyor..")
time.sleep(3)
print("""
                                 _  __   _           _   
                               | |/ _| | |         | |  
   _____      _____    ___  ___| | |_  | |__   ___ | |_ 
  / _ \ \ /\ / / _ \  / __|/ _ \ |  _| | '_ \ / _ \| __|
 | (_) \ V  V / (_) | \__ \  __/ | |   | |_) | (_) | |_ 
  \___/ \_/\_/ \___/  |___/\___|_|_|   |_.__/ \___/ \__|
""")
print("CodingBy = KamiKaze#0011")
print("\n")
time.sleep(3)
print("Bot Aktif..")
simdi = datetime.datetime.now()
devam = 1
def wh():
    time.sleep(4)
    pyautogui.write("owoh")
    pyautogui.press('enter')
def wb():
    pyautogui.write("owob")
    pyautogui.press('enter')

if secim == "sc":
    def ws():
        pyautogui.write("owo sc all")
        pyautogui.press('enter')
elif secim == "sell":
    def ws():
        pyautogui.write("owo sell all")
        pyautogui.press('enter')
        
else:
    time.sleep(4)
    print("Hata Yanlış Giriş Sadece 'sell, sc' Yazabilirsin!")
    devam = 0

while True:
    if devam == 1:
        time.sleep(3)
        wh(), print("owoh ", simdi)
        time.sleep(20)
        wb(), print("owob ", simdi)
        time.sleep(15)
        ws(), print("owo sell&sc all ", simdi)
        time.sleep(4)