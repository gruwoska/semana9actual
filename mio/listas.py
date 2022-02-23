class Lista:
    def __init__(self):
        self.lista=[]
    def push(self,dato):
        self.lista.append(dato)   
    def pop(self):
        dato = self.lista.pop()
        return dato
    def eleminarElemento(self,pos):
        if pos < 0 or pos >= len(self.lista):
           return None
        else:    
           listaAux = []
           for ind in range(0,pos): 
                listaAux+= [self.lista[ind]]
           for ind in range(pos+1,len(self.lista)): 
               listaAux += [self.lista[ind]]
           self.lista = listaAux    
           return self.lista
    def InsertarElemento(self,pos,dato):
        self.lista.insert(pos,dato)
    def buscar(self,buscado):
        return(self.lista.index(buscado))
    def mostrar(self):
        print(self.lista)

