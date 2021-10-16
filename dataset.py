import os
import re
import shutil

f = open('camerapos-20210131.txt', 'r')
for line in f:
    if not line.startswith('x '):
        #print(line)
        collum = line.split()
        phi = int(float(collum[6]))
        img = (collum[8])
        print(img)
        if(phi<0):
            phi=(phi*-1)+100
        
        div = (phi - (phi % 10)) 

        diretorio = str(div) 

        try:
            if not os.path.isdir(diretorio):
                os.makedirs(diretorio)
                
        except OSError:
            print('erro')
        
        shutil.copy(img,diretorio)