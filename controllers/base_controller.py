class BaseController:
    def __init__(seft):
        seft.data=[]
        
    def guardar(self, entrada):
        self.data.append(entrada)
        
    def obtener_todos(self):
        return self.data    