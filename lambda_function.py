import json
from preguntas import lista

import random
import time

random.seed(time.time()) 

lista_preguntas = lista.preguntas['preguntas']
largo = len(lista_preguntas)

random_sample_index = random.sample(range(0, largo), 8)

preguntas_seleccionadas = [lista_preguntas[i] for i in random_sample_index]



def lambda_handler(event, context):
    import random
    import time
    
    random.seed(time.time())  # Inicializa la semilla en cada ejecución
    
    random_sample_index = random.sample(range(0, largo), 8)
    preguntas_seleccionadas = [lista_preguntas[i] for i in random_sample_index]
    
    return {
        'statusCode': 200,
        'body': {
            'preguntas': preguntas_seleccionadas,
            'n': random_sample_index
        }
    }

