class Empleado:
    def __init__(self, nombre, id_empleado, salario, fecha_inicio, impuesto):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario = salario
        self.fecha_inicio = fecha_inicio

    def obtener_datos(self):
        datos_empleado = {
            'nombre': self.nombre,
            'id_empleado': self.id_empleado,
            'salario': self.salario,
            'fecha_inicio': self.fecha_inicio,
            'impuesto' : self.impuesto
        }
        return datos_empleado
        pass
    
class CalculadoraImpuestos:
        
    def calcular_impuestos(self, empleado):
        salario = empleado.salario  
        impuestos = empleado.impuesto
        #Se calcula impuesto
        impuestos = salario * (impuestos / 100)
        return impuestos
        pass
    
class GeneradorReportes:
    def generar_reporte(self, empleado):
        reporte = f"Reporte del empleado {empleado.nombre}\n"
        reporte += f"Código de empleado: {empleado.id_empleado}\n"
        reporte += f"Salario: {empleado.salario}\n"
        reporte += f"Fecha de contratación: {empleado.fecha_inicio}\n"
        reporte += f"Impuesto del empleado: {empleado.impuesto}\n"
        return reporte