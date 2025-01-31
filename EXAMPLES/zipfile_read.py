# from MODULE import THING (where THING is a CLASS)
from zipfile import ZipFile  # zipfile.py contains "class ZipFile ...."

x = list()

# read & extract from zip file
zip_in = ZipFile("../DATA/textfiles.zip")  # Open zip file for reading
print(zip_in.namelist())  # Print list of members in zip file
info = zip_in.getinfo('parrot.txt')
print(f"{info.filename = }")
print(f"{info.file_size = }")
print(f"{info.compress_size = }")
print(f"{info.date_time = }")


tyger_text = zip_in.read('tyger.txt').decode()  # Read (raw binary) data from member and convert from bytes to string
print(tyger_text[:100], '\n')
zip_in.extract('parrot.txt')  # Extract member

