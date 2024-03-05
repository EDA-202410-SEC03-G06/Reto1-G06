"""
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


def new_data_structs(tipo):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    title;street;city;country_code;address_text;marker_icon;workplace_type;
    company_name;company_url;company_size;experience_level;published_at;remote_interview;
    open_to_hire_ukrainians;id;display_offer

    """ 
    if tipo == None:
        tipo = 'ARRAY_LIST'
        
    catalog = {'skills':None,
               'multi-locations': None,
               'jobs': None,
               'employment-types':None
              }
    
    
    catalog['skills'] = lt.newList(tipo)
    catalog['multi-locations'] = lt.newList(tipo)
    catalog['jobs'] = lt.newList(tipo)
    catalog['employment-types'] = lt.newList(tipo)
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
    
    pass


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
                break
            
    filtro_2 = lt.newList('ARRAY_LIST')
    for o in lt.iterator(filtro):
        datos = {'title':o['title'],'company_name':o['company_name'],'experience_level':o['experience_level'],
                 'country_code':o['country_code'],'city':o['city'],'company_size':o['company_size'],
                 'workplace_type':o['workplace_type'], 'open_to_hire_ukrainians':o['open_to_hire_ukrainians']}
        lt.addLast(filtro_2,datos)
    return filtro_2 
    
    


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
                break
            
    filtro_2 = lt.newList('ARRAY_LIST')
    for o in lt.iterator(filtro):
        datos = {'published_at':o['published_at'],'country_code':o['country_code'],'city':o['city'],
                 'company_name':o['company_name'],'title':o['title'], 'experience_level':o['experience_level'],
                 'remote_interview':o['remote_interview'],'workplace_type':o['workplace_type']}
        lt.addLast(filtro_2,datos)    
    
    return filtro_2
    



def req_3(catalog, empresa, fecha_in, fecha_fin):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    ofertas = catalog['jobs']
    final  = lt.newList('ARRAY_LIST')
   

    for oferta in lt.iterator(ofertas):
        if empresa == oferta['company_name']:
            date = oferta['published_at']
            fecha = datetime.strftime(date,'%Y-%m-%d')
            if fecha<=fecha_fin and fecha>=fecha_in:
                lt.addLast(final,oferta)
            elif fecha<fecha_in:
                break
            
    filtro_2 = lt.newList('ARRAY_LIST')
    for o in lt.iterator(final):
        datos = {'published_at':o['published_at'],'title':o['title'],'experience_level':o['experience_level'],
                 'city':o['city'],'country_code':o['country_code'],'company_size':o['company_size'], 
                 'workplace_type':o['workplace_type'],'open_to_hire_ukrainians':o['open_to_hire_ukrainians']}
        lt.addLast(filtro_2,datos)    
    
    ins.sort(filtro_2, sort_criteria_req3)
    print(filtro_2)
            
    return filtro_2 


def req_4(catalog, pais, fecha_in, fecha_fin):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    ofertas = catalog['jobs']
    final  = lt.newList('ARRAY_LIST')
    

    for oferta in lt.iterator(ofertas):
        if pais == oferta['country_code']:
            date = oferta['published_at']
            fecha = datetime.strftime(date,'%Y-%m-%d')
            if fecha<=fecha_fin and fecha>=fecha_in:
                lt.addLast(final,oferta)
    return final 


def req_5(catalog, city, fecha_in, fecha_fin):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    ofertas = catalog['jobs']
    ofertas_filtradas  = lt.newList('ARRAY_LIST')
    fecha_in = datetime.strptime(fecha_in, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    empresas= lt.newList("ARRAY_LIST")
    mayor_numero_empresas = {}
    numero_empresas_ordenadas = lt.newList("ARRAY_LIST")
 
    for oferta in lt.iterator(ofertas):
        if city == oferta['city']:
            empresa = oferta["company_name"]
            date = oferta['published_at']
            fecha = datetime.strftime(date,'%Y-%m-%d')
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            
            if fecha<=fecha_fin and fecha>=fecha_in:
                lt.addLast(ofertas_filtradas,oferta)
                cantidad_ofertas= lt.size(ofertas_filtradas)
                if lt.isPresent(empresas, empresa)==0:
                    lt.addLast(empresas, empresa)
                    cantidad_empresas= lt.size(empresas)
                
                if oferta["company_name"] not in mayor_numero_empresas:
                    mayor_numero_empresas[oferta["company_name"]] = 1
                else: 
                    mayor_numero_empresas[oferta["company_name"]] +=1
        
                    
                    
    for empresa in mayor_numero_empresas.keys():
        lt.addLast(numero_empresas_ordenadas, {"empresa":mayor_numero_empresas, "count":mayor_numero_empresas[empresa]})
    merg.sort(numero_empresas_ordenadas, sort_criteria_req6)
    mayor= lt.firstElement(numero_empresas_ordenadas)
    mayor_empresa= mayor["empresa"]
    menor= lt.lastElement(numero_empresas_ordenadas)
    menor_empresa= menor["empresa"]
    
    ultima_respuesta = lt.newList('ARRAY_LIST')
    for llave in lt.iterator(ultima_respuesta):
        datos = {'published_at':llave['published_at'],'title': llave['title'],'experience_level': llave['experience_level'],
                 'city': llave['city'],'country_code': llave['country_code'],'company_size': llave['company_size'], 
                 'workplace_type': llave['workplace_type'],'open_to_hire_ukrainians':llave['open_to_hire_ukrainians']}
        lt.addLast(ultima_respuesta,datos)    
    ins.sort(ultima_respuesta, sort_criteria_req3)
    
        
                    
    return (cantidad_ofertas, cantidad_empresas, (mayor, mayor_empresa), (menor, menor_empresa), ultima_respuesta)






def req_6(data_structs, n, pais, experience, fecha_in, fecha_fin):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 
    catalog = data_structs['jobs']
    emptypes = data_structs['employment-types']
    ciudades = lt.newList('ARRAY_LIST')
    ofertas = lt.newList('ARRAY_LIST')
    empresas = lt.newList('ARRAY_LIST')
    id_list = lt.newList('ARRAY_LIST')
    city = {}
    cant_empresas = 0
    sal_promedio = 0
    div_salario = 0
#filtrar con pais
    if pais != None: 
        for oferta in lt.iterator(catalog):
         
            if pais == oferta['country_code'] and experience == oferta['experience_level']:
                date = oferta['published_at']
                fecha = datetime.strftime(date,'%Y-%m-%d')
                if fecha<=fecha_fin and fecha>=fecha_in:
                 
                    if oferta['city'] not in city:
                        city[oferta['city']] = 1
                        lt.addLast(ofertas,oferta)     
                        
                    elif oferta['city']  in city:
                        lt.addLast(ofertas,oferta)
                        city[oferta['city']] += 1

#filtrar sin pais        
    else:
        for oferta in lt.iterator(catalog):
            date = oferta['published_at']
            fecha = datetime.strftime(date,'%Y-%m-%d')
            if  experience == oferta['experience_level'] and fecha<=fecha_fin and fecha>=fecha_in:
                    
                    if oferta['city'] not in city:
                        city[oferta['city']] = 1
                        lt.addLast(ofertas,oferta)     
                        
                    elif oferta['city']  in city:
                        lt.addLast(ofertas,oferta)
                        city[oferta['city']] += 1
    
      
       
# sort a ciudades
    for ciudad in city.keys():
        lt.addLast(ciudades,{'city':ciudad,'count':city[ciudad]})     
           
    merg.sort(ciudades,sort_criteria_req6)
    lista_de_n_cities = lt.newList('ARRAY_LIST')
    for ciudad in lt.iterator(ciudades):
        if lt.size(lista_de_n_cities)<n:
            lt.addLast(lista_de_n_cities,ciudad['city'])
        else:
            break
    cant_ciudades = lt.size(lista_de_n_cities)
    mayor = lt.firstElement(ciudades)
    sub = lt.subList(ciudades,0,n+1)
    menor = lt.lastElement(sub)
    
#lista filtrada con las ciudades
    filtro = lt.newList('ARRAY_LIST')
    for oferta in lt.iterator(ofertas):
        present = lt.isPresent(lista_de_n_cities,oferta['city'])
        if present>0:
            lt.addLast(filtro,oferta)
    total_ofertas = lt.size(filtro)

#contar empresas y sacar id  
    for oferta in lt.iterator(filtro):
        present_empresa = lt.isPresent(empresas,oferta['company_name'])
        if present_empresa==0:
            lt.addLast(empresas,oferta['company_name']) 
            cant_empresas +=1
        lt.addLast(id_list,oferta['id'])
          
    
    #promedio salario
    if pais!=None:
        for oferta in lt.iterator(emptypes):
            present_id = lt.isPresent(id_list,oferta['id'])
            if present_id>0 and oferta['salary_from']!='':
                sal_promedio+= int(oferta['salary_from'])
                div_salario +=1

    promedio = sal_promedio/div_salario
    
    print(promedio)
    return total_ofertas, cant_ciudades, cant_empresas, mayor, menor, promedio                                 
    

def req_7(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    
    pass

def req_8(catalog, nivel_experiencia, fecha_in, fecha_fin):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    
    #Empresas que publicaron por lo menos una oferte
    empresas_que_publicaron_algo=0
    ofertas = catalog["jobs"]
    
    for empresas in lt.iterator(ofertas):
        

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

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

def sort_criteria_req3(data_1,data_2):
    if data_1['published_at']==data_2['published_at']:
        return data_1['country_code'] < data_2['country_code']
    else:
        return data_1["published_at"] > data_2["published_at"]


def sort_criteria_req6(data_1,data_2):
    return data_1['count']>data_2['count']