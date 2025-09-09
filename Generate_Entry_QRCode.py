# Dropbox API Stuff Preparation

# Defining URL CONSTANT
WB_PUBLIC_URL = 'www.youtube.com'

# Basic Copy-Pasted Script to genereate QR Code and Save it as a PNG
def generate_qrcode(url, id):
    import qrcode
    import dropbox # To store qrcodes

    # Data to encode in the QR code
    data = url + f"/{id}"

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

    return img