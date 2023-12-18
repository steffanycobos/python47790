
class Products:

    def __init__(self,title, description,price,stock,imagen):
     self.title = title
     self.description = description
     self.price = price
     self.stock= stock
     self.imagen = imagen
       

    def gettitle(self):
        return self.title

    def getprice(self):
        return self.price
    def getimagen(self):
        return self.imagen


producto=Products("Shampoo",'loremlorem',20,20,'nddndd.png')

nombre=producto.gettitle()
precio=producto.getprice()
imagen=producto.getimagen()

if type(nombre) is  str:
   print('Prueba Exitosa')
else:
   print('Prueba Fallida')

if type(precio) is int or float:
   print('Prueba Exitosa')
else:
   print('Prueba Fallida')

if '.jpg' or '.png' in imagen:
   print('Prueba Exitosa')
else:
   print('Prueba Fallida')
