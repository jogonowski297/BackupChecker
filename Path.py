import re
import os
import time

class Path:
    def __init__(self, foldernames):
        self.folder_names = foldernames

    def get_date_and_size(self, path):
        for dirpath, dirnames, filenames in os.walk(path[1:-1]):
            for i in dirnames:
                for j in self.folder_names:
                    x = re.compile(j[1:-1])
                    if(x.search(str(i))):
                        print(j, self.get_folder_size(path[1:-1],i))
                        backup_size = self.humanbytes(self.get_folder_size(path[1:-1],i))
                        if(backup_size == '0.00'):
                            backup_size = f'{self.get_folder_size(path[1:-1],i)} B'
                        date = self.get_date(path, i)
                        return backup_size, date
            break
        return "ERROR", "ERROR"

    def get_date(self, path,  dir_):
        modTimesinceEpoc = os.path.getmtime(path[1:-1] + '\\' + dir_)
        modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))

        return modificationTime

    def get_folder_size(self, path, dir_):
        size = 0
        for file in os.scandir(path + '\\' + dir_):
            size += os.stat(file).st_size
        return size

    def humanbytes(self, B):
        B = float(B)
        KB = float(1024)
        GB = float(KB ** 3)  # 1,073,741,824
        return '{0:.2f}'.format(B / GB)

