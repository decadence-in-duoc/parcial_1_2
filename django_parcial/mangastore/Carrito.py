class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get["carrito"]
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self, producto):
        
        if str(producto.id) not in self.carrito.keys():
            self.carrito[producto.id] = {
                "producto_id":producto.id,
                "nombre": producto.nombre,
                "acumulado": str(producto.precio),
                "cantidad": 1,
                "image": producto.image.url,
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] +1
                    
                    break
        self.save()
    
    def save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
        
    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.save()
            
    def decrement(self, producto):
        for key, value in self.carrito.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 1:
                    self.remove(producto)
                else:
                    self.save()
                break
            else:
                print("el producto no existe en el carrito")
            
    def clear(self):
        self.session["carrito"] = {}
        self.session.modified = True