

class Tarea:
    def __init__(self, id_tarea, descripccion, prioridad, completada=False):
        self.id_tarea = id_tarea
        self.descripccion = descripccion
        self.prioridad = prioridad
        self.completada = completada

    def __str__(self):
        return f'ID Tarea: {self.id_tarea} - Descripccion: {self.descripccion} - Prioridad: {self.prioridad} - Completada: {self.completada}'

    def to_dict(self):
        return {
            'id_area': self.id_tarea,
            'descripccion': self.descripccion,
            'prioridad': self.prioridad,
            'completada': self.completada

        }

