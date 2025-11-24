import json
import os
from tarea import Tarea

class Gestor_tareas:
    def __init__(self, ruta_archivo="C:/Users/espos/Documents/Fer/gitrepos/gestor-tareas/data/tareas.json"):
        self.ruta_archivo = ruta_archivo
        self.tareas = []
        self.cargar_tareas()

    def cargar_tareas(self):
        if not os.path.exists(self.ruta_archivo):
            self.guardar_tareas()
            return

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.tareas = [Tarea(**t) for t in datos]
        except (json.JSONDecodeError, ValueError):
            print("⚠️ Archivo JSON vacío o corrupto. Se reiniciará.")
            self.tareas = []
            self.guardar_tareas()

    def guardar_tareas(self):
        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tareas], f, indent=4) 
    
    def agregar_tarea(self):
        id_tarea = input('Ingrese el nombre de la tarea: ')
        descripccion = input('Ingrese descripccion de la tarea: ')
        prioridad = int(input('Ingrese la prioridad de la tarea: '))

        tarea_nueva = Tarea(id_tarea,descripccion,prioridad)
        self.tareas.append(tarea_nueva)
        self.guardar_tareas()
        print('Tarea agregada con exito')


    def listar_tareas(self):
        if not self.tareas:
            print('No hay tareas')
            return
        for tarea in self.tareas:
            print(tarea)


    def completar_tarea(self):
        id_tarea = input('Ingrese el id de la tarea: ')

        for tarea in self.tareas:
            if tarea.id_tarea == id_tarea:
                tarea.completada = True
                self.guardar_tareas()
                print(f'Tarea {id_tarea} esta completada')
                return
            
        else:
            print(f'No se encontro la tarea {id_tarea}')
        


    def eliminar_tarea(self):
        id_tarea = input('Ingrese el ID de la tarea')
        for tarea in self.tareas:
            if tarea.id_tarea == id_tarea:
                self.tareas.remove(tarea)
                self.guardar_tareas()
                print(f'Tarea {id_tarea} fue eliminada con exito')
                return
        else:
            print(f'No se encontro la tarea {id_tarea}')
        



    def ordenar_por_prioridad(self):
        n = len(self.tareas)

        if n < 2:
            print("No hay suficientes tareas para ordenar.")
            return

        # Bubble sort
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.tareas[j].prioridad > self.tareas[j + 1].prioridad:
                    self.tareas[j], self.tareas[j + 1] = self.tareas[j + 1], self.tareas[j]

        self.guardar_tareas()
        print("Tareas ordenadas por prioridad:")

        for tarea in self.tareas:
            print(tarea.to_dict())
        

