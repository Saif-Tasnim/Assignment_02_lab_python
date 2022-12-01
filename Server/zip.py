
import glob
import shutil
import os
from zipfile import ZipFile

# print("Hello")

source_path = '../source/*'
server_path = '.'
destination_path = '../Destination/'
lines=list()

# print(source_object)
postfix = [1,2,3]
while True:
    
    source_object = glob.glob(source_path)
    
    if len(source_object)>0:
       
        object_path = source_object[0] 
        # print(type(object_path))
        shutil.copy(object_path,server_path)

        # file name in server
        ob_name = object_path.split('\\')[-1]
        # print(type(ob_name))

        object_name = ob_name.split('.')
        # print(object_name)

        prefix = object_name[0]
        postfix2 = object_name[1]

        zip_file_name = f'{prefix}.zip'

        new_zip = ZipFile(zip_file_name,'w')

        # print(prefix, "  " , postfix2)

        for item in postfix:
            filename = f'{prefix}_{item}.{postfix2}'
            print(filename)
            # destination = f'{destination_path}{filename}'
            # print(destination)
            if (postfix2 == 'py'):
                continue
            shutil.copy(object_path,f'{server_path}{filename}')
            with open(object_path,"r") as file:
                    lines = file.readlines()
            file.close()
            # print(item)

            with open(f'{server_path}{filename}',"w") as file:
                for index,line in enumerate(lines):
                    if index < item*10:
                        file.write(line)
                
            new_zip.write(f'{server_path}{filename}')        
            file.close()
            os.remove(f'{server_path}{filename}')
        new_zip.close()

        shutil.copy(zip_file_name , f'{destination_path}{zip_file_name}')
        # zip_path = f'{destination_path}{zip_file_name}'
        shutil.unpack_archive(f'{zip_file_name}',f'{destination_path}{prefix}.{postfix2}')

        unzip_path = f'{destination_path}{prefix}.zip'
        # unzip_object = glob.glob(unzip_path)
        jhamela_path = f'{destination_path}source.txt'

        os.remove(object_path)
        os.remove(ob_name)
        os.remove(zip_file_name)
        os.remove(unzip_path)
        # os.remove(jhamela_path)

                          




