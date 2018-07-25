import pyotp
import qrcode_terminal
import io

# key = pyotp.random_base32()
key = 'mhayk'
output = pyotp.totp.TOTP(key).provisioning_uri("mhayklima@firmstep.com", issuer_name="Mhayk Python App")

# stream = io.StringIO()
print(key)
qrcode_terminal.draw(output)