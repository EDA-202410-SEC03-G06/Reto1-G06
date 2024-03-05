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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
from datetime import datetime
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    title;street;city;country_code;address_text;marker_icon;workplace_type;
    company_name;company_url;company_size;experience_level;published_at;remote_interview;
    open_to_hire_ukrainians;id;display_offer

    """ 
    catalog = {'skills':None,
               'multi-locations': None,
               'jobs': None,
               'employment-types':None
              }
    
    
    catalog['skills'] = lt.newList('ARRAY_LIST')
    catalog['multi-locations'] = lt.newList('ARRAY_LIST')
    catalog['jobs'] = lt.newList('ARRAY_LIST')
    catalog['employment-types'] = lt.newList('ARRAY_LIST')
    #TODO: Inicializar las estructuras de datos
    return catalog


# Funciones para agregar informacion al modelo

def add_skills(catalog, skills):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(catalog['skills'], skills)
    
    
def add_jobs(catalog, job):
    
    date = job['published_at']
    job['published_at'] = datetime.strptime(date,'%Y-%m-%dT%H:%M:%S.%fZ')
    lt.addLast(catalog['jobs'], job)
    
def add_locations(catalog, location):
    lt.addLast(catalog['multi-locations'],location)
    
def add_employment_types(catalog,emptype): 
    lt.addLast(catalog['employment-types'], emptype)
# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(lst):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(lst)


def req_1(catalog, n, pais, expert):
    # TODO: Realizar el requerimiento 1
    """
    Función que soluciona el requerimiento 1
    """
    ofertas = catalog['jobs']
    filtro = lt.newList('ARRAY_LIST')
    total_ofertas=0
    for oferta in lt.iterator(ofertas):
        if oferta['country_code'] ==pais and oferta['experience_level']==expert:
            lt.addLast(filtro, oferta)
            total_ofertas+=1
            if total_ofertas>=n:
                return filtro
    return filtro 
    
    


def req_2(catalog, n, empresa, ciudad):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    ofertas = catalog['jobs']
    filtro = lt.newList('ARRAY_LIST')
    total_ofertas=0
    for oferta in lt.iterator(ofertas):
        if oferta['city'] ==ciudad and oferta['company_name']==empresa:
            lt.addLast(filtro, oferta)
            total_ofertas+=1
            if total_ofertas>=n:
                return filtro
    return filtro
    



def req_3(catalog, empresa, f_inicio, f_fin):
    """
    Función que soluciona el requerimiento 3
    """
    ofertas = catalog['jobs']
    ofertas_rango = lt.newList('ARRAY_LIST')
    of_junior = 0
    of_mid = 0
    of_senior = 0
    f_inicio = datetime.strptime(f_inicio, "%Y-%m-%d")
    f_fin = datetime.strptime(f_fin, "%Y-%m-%d")
    for oferta in lt.iterator(ofertas):
        if oferta["company_name"] == empresa:
            fecha = oferta['published_at']
            fecha = datetime.strftime(fecha,'%Y-%m-%d')
            fecha = datetime.strptime(fecha,'%Y-%m-%d')
            if (f_inicio <= fecha) and (fecha <= f_fin):
                lt.addLast(ofertas_rango, oferta)
                experiencia = oferta["experience_level"]
                if experiencia.lower() == "junior":
                    of_junior +=1
                elif experiencia.lower() == "mid":
                    of_mid +=1
                elif experiencia.lower()== "senior":
                    of_senior +=1
    of_total = of_junior + of_mid + of_senior
    return of_total, of_junior, of_mid, of_senior, ofertas_rango
                
            
    
    
    


def req_4(catalog, pais, f_inicio, f_fin):
    """
    Función que soluciona el requerimiento 4
    """
    ofertas = catalog['jobs']
    ofertas_rango = lt.newList('ARRAY_LIST')
    empresas = lt.newList('ARRAY_LIST')
    f_inicio = datetime.strptime(f_inicio,'%Y-%m-%d')
    f_fin = datetime.strptime(f_fin,'%Y-%m-%d')
    ciudades = {}
    for oferta in lt.iterator(ofertas):
        if pais == oferta['country_code']:
            empresa = oferta["company_name"]
            
            fecha_oferta = oferta['published_at']
            fecha_string = datetime.strftime(fecha_oferta,'%Y-%m-%d')
            fecha = datetime.strptime(fecha_string,'%Y-%m-%d')
            if (f_inicio <= fecha) and (fecha <= f_fin):
                remote = oferta['workplace_type']
                if 'remote' in remote:
                    oferta['remote'] = remote
                else:
                    oferta['remote'] = False
                lt.addLast(ofertas_rango, oferta)
                empresa = oferta["company_name"]

                if lt.ispresent(empresas, empresa) == 0:
                    lt.addLast(empresas, empresa)
                
                if oferta['city'] not in ciudades:
                    ciudades[oferta['city']] = 1
                else:
                    ciudades[oferta['city']] +=1
    ciudades_ordenadas = lt.newList('ARRAY_LIST')
    for city in ciudades.keys():
        lt.addLast(ciudades_ordenadas, {'ciudad': city,'cuenta': ciudades[city]})
    merg.sort(ciudades_ordenadas, sort_criteria_req6)
    numero_ciudades = lt.size(ciudades_ordenadas)
    mayor = lt.firstElement(ciudades_ordenadas)
    ciudad_mayor = mayor["ciudad"]
    cuenta_ciudad_mayor = mayor['cuenta']
    menor = lt.lastElement(ciudades_ordenadas)
    ciudad_menor = menor['ciudad']
    cuenta_ciudad_menor = menor['cuenta']
    
    
                
                    
    return lt.size(ofertas_rango), lt.size(empresas), lt.size(ciudades_ordenadas), (ciudad_mayor, cuenta_ciudad_mayor),(ciudad_menor,cuenta_ciudad_menor),ofertas_rango
    


def req_5():
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(catalog, n, f_inicial, f_final):
    """
    Función que soluciona el requerimiento 7
    """

    ofertas_jobs = catalog["jobs"]
    ofertas_skills = catalog["skills"]
    

    f_inicio = datetime.strptime(f_inicial,'%Y-%m-%d')
    f_fin = datetime.strptime(f_final,'%Y-%m-%d')

    ofertas_rango = lt.newList('ARRAY_LIST')
    ofertas_paises = {}
    for oferta in lt.iterator(ofertas_jobs):
        if ((ofertas_jobs['published_at'] >= f_inicio) and (ofertas_jobs['published_at'] <= f_fin)):
            lt.addLast(ofertas_rango, oferta)
            pais_oferta = oferta['country_code']
            if pais_oferta not in ofertas_paises:
               ofertas_paises[pais_oferta] = 1
            else:
                ofertas_paises[pais_oferta] += 1
    paises_organizados = lt.newList('ARRAY_LIST')  
    for pais in paises.keys():
        lt.addLast(paises_organizados, {'pais': pais,'cuenta': ciudades[pais]})
    merg.sort(paises_organizados, sort_criteria_req6)
    top_n = lt.newList('ARRAY_LIST')
    i= 0 
    while lt.size(top_n) < n:
        lt.addLast(top_n, paises_organizados[i]['pais'])
        i+=1

    pais_mayor = top_n[0]['pais']
    cuenta_pais_mayor = pais_oferta[pais_mayor]
    
    ofertas_n_paises = lt.newList()
    for oferta in lt.iterator(ofertas_rango):
        if lt.ispresent(top_n, oferta['country_code']) == 0:
            lt.addLast(ofertas_n_paises, oferta)
    
    total_ofertas = lt.size(ofertas_n_paises)
# Criterios para retornar en ciudades
    ciudades = {}
    for oferta in ofertas_n_paises:
        if oferta['city'] not in ciudades:
            ciudades[oferta['city']] = 1
        else:
            ciudades[oferta['city']] +=1
    
    ciudades_ordenadas = lt.newList('ARRAY_LIST')
    for city in ciudades.keys():
        lt.addLast(ciudades_ordenadas, {'ciudad': city,'cuenta': ciudades[city]})
    merg.sort(ciudades_ordenadas, sort_criteria_req6)
    numero_ciudades = lt.size(ciudades_ordenadas)
    ciudad_mayor= ciudades_ordenadas[0]['ciudad']
    cuenta_ciudad_mayor = ciudades_ordenadas[0]['cuenta']
#Encontrar los skills y organizarlos
    skills_junior = lt.newList('ARRAY_LIST')
    skills_mid = lt.newList('ARRAY_LIST')
    skills_senior = lt.newList('ARRAY_LIST')
    for oferta in lt.iterator(ofertas_n_paises):
        position = lt.isPresent(ofertas_skills, oferta['id'])
        elemento = lt.getElement(ofertas_skills, position)
        lt.addLast(skills, elemento)
    
            
            
    
    return total_ofertas, numero_ciudades, (pais_mayor, cuenta_pais_mayor), (ciudad_mayor, cuenta_ciudad_mayor),


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    return data_1["published_at"] > data_2["published_at"]


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    return merg.sort(data_structs["jobs"], sort_criteria)

def sort_criteria_req6(data_1,data_2):
    return data_1['count']>data_2['count']