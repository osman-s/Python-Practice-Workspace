from time import ctime
from pathlib import Path
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
path = Path("ecommerce/__init__.py")
# paths = [p for p in path.iterdir() if p.is_dir()]
print(path.stat())
print(ctime(path.stat().st_ctime))