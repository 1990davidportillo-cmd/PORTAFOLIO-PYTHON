import os
import shutil

ruta = "C:\\Users\\david\\Desktop\\carpeta"

os.makedirs(os.path.join(ruta, "HTML"), exist_ok=True)
os.makedirs(os.path.join(ruta, "CSS"), exist_ok=True)
os.makedirs(os.path.join(ruta, "PDFs"), exist_ok=True)

for archivo in os.listdir(ruta):

    if archivo.endswith(".html"):
        shutil.move(
            os.path.join(ruta, archivo),
            os.path.join(ruta, "HTML", archivo)
        )

    elif archivo.endswith(".css"):
        shutil.move(
            os.path.join(ruta, archivo),
            os.path.join(ruta, "CSS", archivo)
        )

    elif archivo.endswith(".pdf"):
        shutil.move(
            os.path.join(ruta, archivo),
            os.path.join(ruta, "PDFs", archivo)
        )

print("Archivos organizados por tipo correctamente")
