import os
import json
import cv2
path = os.getcwd()
name = str(input('NOME DO PROCURADO:'))

for root, dirs, files in os.walk(path):
    if name in files:
        print(os.path.join(root, name))
        nome = open('./ficha/' + name + '/' + name)
        ficha = json.load(nome)
        print(json.dumps(ficha, indent= 2))
        mugshot = './ficha/' + name + '/' + name + '.jpg'
        mugimg = cv2.imread(mugshot)
        fingerprint = './database/' + name + '.jpg'
        fingerread = cv2.imread(fingerprint)
        cv2.imshow('fingerprint', fingerread)
        cv2.imshow("mugshot", mugimg)
        cv2.waitKey(2621440)
        cv2.destroyAllWindows()
       
    else:
        print('nada encontrado')