#producto.py

class Producto:
    def __init__ (self, id: str, nombre:str, precio: float, stock: int):
        self.id = None
        self.nombre = None
        self.precio = None
        self.stock = None

        self.set_id(id)
        self.set_nombre( nombre )
        self.set_precio( precio )
        self.set_stock( stock )
        

    #GETTERS
    def get_id(self): return self.id
    def get_nombre(self): return self.nombre
    def get_precio(self): return self.precio
    def get_stock(self): return self.stock

    #SETTERS con validaciones simples
    def set_id(self, new_id:str):
        if not new_id or not new_id.strip():
            raise ValueError("El id no puede estar vacio")
        self.id = new_id.strip()
    
    def set_nombre(self, new_nombre:str):
        if not new_nombre or not new_nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        self.nombre = new_nombre.strip()   

    def set_precio(self, new_precio:float ):
        try:
            precio = float(new_precio)
        except:
            raise ValueError("El precio debe ser numero")
        
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        self.precio = precio
    
    def set_stock(self, new_stock:float ):
        try:
            cant = int(new_stock)
        except:
            raise ValueError("El stock debe ser numero")
        
        if cant <= 0:
            raise ValueError("El stock debe ser mayor que cero")
        self.stock = cant
    
    #funciones extras de la clase 
    
    





