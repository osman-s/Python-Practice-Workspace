import csv
from zipfile import ZipFile
from time import ctime
from pathlib import Path
import json
# Path(r"C:\Program Files\")
# Path.home()
# path = Path("ecommerce/__init__.py")
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_name("file.txt")
# path = path.with_suffix(".txt")
# print(path)

# 3. Working with Directories
path = Path("shop/ecommerce/__init__.py")
# paths = [p for p in path.iterdir() if p.is_dir()]
print(path.stat())
print(ctime(path.stat().st_ctime))
print("-----------------------------------")

# with ZipFile("files.zip", "w") as zip:
#     for path in Path("Shop/ecommerce").rglob("*.*"):
#         zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())

# 6. Working with CSV
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transcation_id", "product_id", "price_id"])
    writer.writerow([100, 1, 5])
    writer.writerow([1001, 2, 15])

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1993}
]

data = json.dumps(movies)
Path("movies.json").write_text(data)
