# Defining URL CONSTANT
WB_PUBLIC_URL = 'www.youtube.com'

# Basic Copy-Pasted Script to genereate QR Code and Save it as a PNG
def generate_qrcode(url, id):
    # Dropbox API Stuff Preparation + QR Code Stuff Preparation
    import qrcode
    import dropbox
    import os

    # Dropbox API Vars && Constants
    DB_ACCESS_TOKEN = os.environ["DROPBOX_ACCESS_TOKEN"]
    qrName = f"prt-{id}.png"
    qrPath = f"/prt-{id}.png"
    # Setting Up
    dbx = dropbox.Dropbox(DB_ACCESS_TOKEN)
    DB_PATH = ""
    fileNames = [entry.name for entry in dbx.files_list_folder(DB_PATH).entries]

    # Checking if qrCode is already in Dropbox
    if qrName in fileNames:
        # Getting LINK already because file ALREADY EXISTS
        links = dbx.sharing_list_shared_links(path=qrPath, direct_only=True)
        qrDb_link = links.links[0].url
        return qrDb_link
    else:
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
        img.save(f'prt-{id}.png')

        # Uploading to DropBox
        with open(qrName, "rb") as f:
            dbx.files_upload(f.read(), qrPath, mode=dropbox.files.WriteMode("overwrite"))

        # Getting link AFTER writing the file
        link_metadata = dbx.sharing_create_shared_link_with_settings(qrPath)
        qrDb_link = link_metadata.url

        return qrDb_link