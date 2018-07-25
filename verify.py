import pyotp

totp = pyotp.TOTP('mhayk')
#print("Current OTP:", totp.now())

while True:
    #print(totp.now())
    pin = input("Enter your OTP: ")
    if pin == totp.now():
        print("Nice baby!")
    else:
        print("Oh gosh! run away!")
