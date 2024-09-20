class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def __str__(self):
        return f'Empleado: {self.nombre}, salario: {self.salario}'
    
    def __repr__(self):
        return f'Empleado({self.nombre}'
    