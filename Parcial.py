class Paciente:
    def __init__(self,documento,nombre,sexo,fecha):
        self.documento=documento
        self.nombre=nombre
        self.sexo=sexo
        self.fecha_nacimiento=fecha

class HistoriaClinica:
    def __init__(self,signos_vitales,notas_evolucion,imagenes_diagnosticas,examenes_laboratorio):
        self.signos_vitales = signos_vitales
        self.notas_evolucion = notas_evolucion
        self.imagenes_diagnosticas = imagenes_diagnosticas
        self.examenes_laboratorio = examenes_laboratorio
        
    def mostrarhistoria(self):
        print("Signos vitales: ",self.signos_vitales)
        print("notas de evolucion: ",self.notas_evolucion)
        print("imagenes diagnosticas: ", self.imagenes_diagnosticas)
        print("examenes del laboratorio: ",self.examenes_laboratorio)
        
class Cama:
    def __init__(self):
        self.numero = 0
        self.servicio = ""
        self.paciente_actual = None
    def camilla(self):
        self.numero=input("numero de camilla: ")
        self.servicio=input("Servicio: ")

class Medicamento:
    def __init__(self, nombre, dosis):
        self.nombre = nombre
        self.dosis = dosis
        
    def mostrarmed(self):
        print("Medicamento: ",self.nombre)
        print("dosis: ", self.dosis)
      
pacientes=[]
historias_clinicas=[]
c=0
camillas=[]
op=0
while op!=4:
    print("BIENVENIDO\n Ingrese una opcion:\n 1:Ingresar paciente\n 2: mostrar historia clinica\n 3: consultar medicamento \n 4: terminar ")       
    
    op = int(input("Opción: "))
    if op == 1:
        documento=input("Documento de identidad: ")
        nombre=input("Nombre: ")
        sexo=input("Sexo [M] o [F]: ")
        fecha=input("Fecha de nacimiento: ")
        signos_vitales=input("Signos vitales: ")
        notas_evolucion=input("notas de evolucion: ")
        imagenes_diagnosticas=input("imagenes diagnosticas: ")
        examenes_laboratorio=input("examenes del laboratorio: ")
        nombremed=input("Medicamento recetado: ")
        dosis=input("dosis del medicamento: ")
        medicamentos_formulados=Medicamento(nombremed,dosis)
        pacientes.append(Paciente(documento,nombre,sexo,fecha))
        historias_clinicas.append(HistoriaClinica(signos_vitales,notas_evolucion,imagenes_diagnosticas,examenes_laboratorio))
    elif op == 2:
            for HistoriaClinica in historias_clinicas:
                HistoriaClinica.mostrarhistoria
          
    elif op == 3:
        medicamentos_formulados.mostrarmed
        
        
    elif op == 4:
        print("\nTenga un buen día\n")
        break  
    else:
        print("Opción invalida, intente de nuevo ")
        

