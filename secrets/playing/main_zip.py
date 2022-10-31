import zipfile
with zipfile.ZipFile("artifacts.zip","r") as zip_ref:
    zip_ref.extractall()
