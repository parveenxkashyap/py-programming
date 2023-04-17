import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10, border=4)

qr.add_data("https://github.com/parveenxkashyap")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("github_colored.png") 


import qrcode
from PIL import Image

# Data for the QR code
data = "https://github.com/parveenxkashyap"

# Create a QR code image directly
img = qrcode.make(data)

# Convert to RGB to apply custom colors
img = img.convert("RGB")

# Change colors
width, height = img.size
pixels = img.load()

for x in range(width):
    for y in range(height):
        if pixels[x, y] == (0, 0, 0):      # Black pixel
            pixels[x, y] = (255, 0, 0)    # Change to red
        else:                              # White pixel
            pixels[x, y] = (0, 0, 255)    # Change to blue

# Save the image
img.save("github_colored.png")
print("QR code created successfully!")
