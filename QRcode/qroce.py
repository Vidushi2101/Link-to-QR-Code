import qrcode
from PIL import Image

def generate_qr_code(link, fill_color="black", back_color="white", filename="qrcode.png"):
    # Create QR code instance
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr_code.add_data(link)
    qr_code.make(fit=True)

    # Create an image from the QR code instance with custom colors
    img = qr_code.make_image(fill_color=fill_color, back_color=back_color)

    # Save the image
    img.save(filename)
    print(f"QR code saved as {filename}")

# Input link and colors from the user
link = input("Enter the link: ")
fill_color = input("Enter the fill color (default is black): ") or "black"
back_color = input("Enter the background color (default is white): ") or "white"
filename = input("Enter the filename (default is qrcode.png): ") or "qrcode.png"

# Generate QR code
generate_qr_code(link, fill_color, back_color, filename)
