import cv2 # importacion de la libreria
imagen=cv2.imread('contorno.jpg') # decimos que imagen queremos
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY) # conversiona  grises
_,umbral=cv2.threshold(grises,100,255,cv2.THRESH_BINARY) # creacion de umbral o contorno devuelve el umbral utilizado y imagen  y _ es variable que no existe
contorno,jerarquía = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) # sirve para poner contornos 
cv2.drawContours(imagen,contorno,-1,(251, 63, 52),3)
#Mostrar
cv2.imshow('Imagen original',imagen)
#cv2.imshow('Imagen en grises',grises)
#cv2.imshow('Imagen Umbral',umbral)
cv2.waitKey(0) # Sirve para que no cierre la ventana
cv2.destroyAllWindows()