# Basic Copy-Pasted Script to genereate QR Code and Save it as a PNG
def generate_qrcode(url, image_name):
    import qrcode

    # Data to encode in the QR code
    data = url

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
        box_size=10,  # Size of each box (pixel)
        border=4,  # Border size around the QR code
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(f"{image_name}.png")

# Script to generate specific url to each pariticpant
from Airtable_API_GetData import *

# Defining known CONSTANTS
WB_PUBLIC_URL = 'www.youtube.com'

# Iterating through each participant
for table in daydream_table.iterate():
    for prt in table:
        prt_id = prt['fields']['Id']
        url = WB_PUBLIC_URL + f'/?id={prt_id}'
        generate_qrcode(WB_PUBLIC_URL, str(prt_id))