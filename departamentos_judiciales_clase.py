from dependencia_judicial import DependenciaJudicial #importamos la clase creada

def extraer_valores(valores): #recorremos la línea y extraemos los valores
    index = valores[0]
    fuero = valores[1]
    nombre = valores[2]
    tipo = valores[3]
    direccion = valores[4]
    localidad = valores[5]
    departamento = valores[6]
    telefono = valores[7]
    latitud = float(valores[8].replace(",", "."))
    longitud = float(valores[9].replace(",", "."))
    return index, fuero, nombre, tipo, direccion, localidad, departamento, telefono, latitud, longitud

class departamentosJudiciales: #creamos una nueva clase para los departamentos
    
    def __init__(self):
        self._departamentos = {} #creo un diccionario donde los voy a almacenar.
                
    def existe_departamento(self,departamento): #vemos si efectivamente tienen cargado un departamento
        return departamento in self._departamentos.keys()
    
    def agregar_departamento(self,departamento,dependencia, valores):
        index, fuero, nombre, tipo, direccion, localidad, departamento, telefono, latitud, longitud = extraer_valores(valores)
        self._departamentos[departamento] = [DependenciaJudicial(index, fuero, nombre, tipo, direccion, localidad,\
                                      departamento, telefono, latitud, longitud)]
        return None
    
    def agregar_dependencia(self,departamento,dependencia, valores):
        index, fuero, nombre, tipo, direccion, localidad, departamento, telefono, latitud, longitud = extraer_valores(valores)
        self._departamentos[departamento].append(DependenciaJudicial(index, fuero, nombre, tipo, direccion, localidad,\
                                      departamento, telefono, latitud, longitud))
        return None
    
    def ordenar(self): #ordenamos los elementos
        for departamento in self._departamentos.keys():
            self._departamentos[departamento] = sorted(self._departamentos[departamento])
        return None
    
    def guardar_en_archivo(self,file): #le indicamos como queremos que nos cree el txt
        f = open(file,"w")
        for dep in sorted(self._departamentos): 
            f.write(dep + ":" + "".join([str(x) for x in self._departamentos[dep]]) + "\n")
        f.close()
        return None
    
    def __repr__(self): #le indicamo como queremos que los represente
        text = ""
        for dep in sorted(self._departamentos):
            text += dep + ":" + "".join([str(x) for x in self._departamentos[dep]]) + "\n"
        return text
            
            