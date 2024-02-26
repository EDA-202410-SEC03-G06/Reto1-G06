﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control):
    """
    Carglos datos del reto
    """
    skills = load_skills(control['model'])
    jobs = load_jobs(control["model"])
    locations = load_locations(control['model'])
    employments = load_employment_type(control['model'])
    return (skills, jobs, locations, employments)

def load_skills(catalog):
    booksfile = cf.data_dir + "small-skills.csv"
    input_file = csv.DictReader(open(booksfile, encoding="utf-8"),delimiter=";")
    for skill in input_file:
        model.add_skills(catalog,skill)
   
    return model.data_size(catalog["skills"])
    
def load_jobs(catalog):
    booksfile = cf.data_dir + "small-jobs.csv"
    input_file = csv.DictReader(open(booksfile, encoding="utf-8"),delimiter=";")
    for job in input_file:
        model.add_jobs(catalog,job)
    
    model.sort(catalog)
    return model.data_size(catalog['jobs'])

def load_locations(catalog):
    booksfile = cf.data_dir + "small-multilocations.csv"
    input_file = csv.DictReader(open(booksfile, encoding="utf-8"),delimiter=";")
    for multilocation in input_file:
        model.add_locations(catalog, multilocation)
    return model.data_size(catalog['multi-locations'])

def load_employment_type(catalog):
    booksfile = cf.data_dir + "small-employments_types.csv"
    input_file = csv.DictReader(open(booksfile, encoding="utf-8"),delimiter=";")
    for employment in input_file:
        model.add_employment_types(catalog, employment)
    return model.data_size(catalog['employment-types'])
# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control,n,pais,exp):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    return model.req_1(control['model'],10,'PL','junior')


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    return model.req_2(control['model'],10,'IntelligINTS','Rijad')


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
