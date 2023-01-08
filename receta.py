from datetime import date
from clinica import Clinica
from persona import mostrar_doctor, mostrar_paciente

class medicamento:
    _secuencia=0
    def __init__(self,des,pre,sto):
        medicamento._secuencia += 1
        self.__codigo = medicamento._secuencia
        self.descripcion = des
        self.precio = pre
        self.stock = sto
    
    @property
    def codigo(self):
        return self.__codigo
        
    def mostrar_medicamento(self):
        print(self.codigo,self.descripcion)
        

class DetalleVenta:
    _linea=0
    def __init__(self,medicina,cantidad):
        DetalleVenta._linea += 1
        self.linea = DetalleVenta._linea
        self.medicina = medicina
        self.precio = medicina.precio
        self.cantidad = cantidad
        
class Venta:
    _factura=0
    _iva=0.12
    def __init__(self,paciente):
        Venta._factura = Venta._factura + 1
        self.factura = "F"+str(Venta._factura)
        self.fecha = date.today()
        self.paciente = paciente
        self.subtotal = 0
        self.iva = 0 
        self.total = 0
        self.detalleVenta = []
        
    
    def agregarDetalle(self,medicina,cantidad):
        detalle = DetalleVenta(medicina,cantidad)
        self.subtotal += round(detalle.precio*detalle.cantidad,2)
        self.iva = round(self.subtotal*Venta._iva,2)
        self.total = round(self.subtotal+self.iva,2)
        self.detalleVenta.append(detalle)    
    
    def mostrarVenta(self,clinicanombre,clinicaruc):
        print("="*100)
        print("Clinica: {:17} Ruc:{}".format(clinicanombre,clinicaruc))    
        print("Factura#:{:13}Fecha:  {}".format(self.factura,self.fecha))
        self.paciente.mostrar_datos()
        print("="*100)
        print("Lista de Medicinas                  Precio Cantidad Subtotal")
        for det in self.detalleVenta:
            print("{} {:35} {}  {:6}  {:7}".format(det.linea,det.medicina.descripcion,det.precio,det.cantidad,det.precio*det.cantidad))
        print("="*100)    
        print( "Diagnostico: administrarse 1 Aspirina de 500 mg cada 8 horas")
        print( "Diagnostico: administrarse 1 Paracetamol cada 8 horas")
        print( "Diagnostico: administrarse 1 Desloratadina cada 24 horas")
        print("="*100)
        print("                                                                         ","Subtotal => ",f"    $ {self.subtotal}")    
        print( "                                                                         ","Iva =>", f"          $ {self.iva}")
        print( "                                                                         ","Total => ",  f"       $ {self.total} ")   

clinica = Clinica()
paciente = mostrar_paciente("Dary Pincay",20, 987463698, 899654793, "Sauses")
doctor = mostrar_doctor("Anderson Merchán",22, 984726066, 157794324, "Guayaquil")      
medi1 = medicamento("Aspirina",3,100)
medi2 = medicamento("Paracetamol",1,200)
medi3 = medicamento("Umbral",1,300)
medi4 = medicamento("Desloratadina",2,100)
venta = Venta(paciente)
venta.agregarDetalle(medi1,3)
venta.agregarDetalle(medi2,2)
venta.agregarDetalle(medi3,1)
venta.agregarDetalle(medi4,2)
venta.mostrarVenta(clinica.nombre,clinica.ruc)
