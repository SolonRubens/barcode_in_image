from PIL import Image
from barcode import EAN13
from barcode.writer import ImageWriter

barcodes = []

for i in range(1, 61):
    barcodes.append(str(i).zfill(12))

for i in barcodes:
    my_code = EAN13(i, writer=ImageWriter())

    my_code = EAN13(i, writer=ImageWriter())
    my_code.write("./src/codes/barcode.png")

    base = Image.open("./lib/Zeitreisenpass_Rückseite.png", "r")
    code = Image.open("./src/codes/barcode.png")

    code_s = code.resize((code.width // 3, code.height // 3))

    new_img = base.copy()
    new_img.paste(code_s, (400, 440))

    new_img.save(f"./src/generated/barcode_{i}.png")
