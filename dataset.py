import os
import re
import shutil

f = open('camerapos-20210131.txt', 'r')

for line in f:
    if not line.startswith('x '):

        column = line.split()
        phi = int(float(column[6]))
        image = (column[8])
        print(image)

        if(phi<0):
            phi=(phi*-1)+100
        
        divider = (phi - (phi % 10)) 
        directory = str(divider)

        try:
            if not os.path.isdir(directory):
                os.makedirs(directory)
                
        except OSError:
            print('erro novo')
            
        shutil.copy(image, directory)