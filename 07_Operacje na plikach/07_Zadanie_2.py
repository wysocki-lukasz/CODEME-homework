import os as os
statinfo = os.stat('cytat.txt')
print(statinfo)
size_file = statinfo.st_size
print('Wielkosc pliku to %s kb' %size_file)