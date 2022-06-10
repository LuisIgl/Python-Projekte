import pyqrcode
from pyqrcode import QRCode


s = "https://www.winsen.de/"

url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("winsen.svg", scale=8)
