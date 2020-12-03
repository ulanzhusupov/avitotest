import json


def load_data(filename, encoding='utf-8'):
    with open(filename, encoding=encoding) as json_file:
        return json.load(json_file)


values = load_data('Values.json')
testStructure = load_data('TestCaseStructure.json')

valuesArr = values['values']
testStructure = testStructure['params']

valuesId = {} # Для удобной работы с данными из Values.json

def simplifyValues(): # Метод который делает словарь с данных из Value.json для удобства
    for item in valuesArr:
        valuesId[item['id']] = item['value']

simplifyValues() # Вызов метода


data = { # Для экспорта json результата
    "params": [] 
} 

errors = {}# Для экспорта json ошибок


def getParams(arr): # Метод для работы с массивами params
    params = []
    for i in arr:
        if 'values' in i: # Если  в элементе есть массив values
            temp = getValues(i['values'], i['id']) # Вызываем метод для работы с массивом values и сохраняем полученные данные
            params.append({
                'id': i['id'],
                'title': i['title'],
                'value': temp['asValueTemp'] if 'asValueTemp' in temp else '', # Если временный asValueTemp не пустой
                'values': temp['arr'] # Присваиваем обработанный массив params
            })
        else: # Эта часть не будет работать, т.к. в нашем примере внутри всех массивов params есть values (P.S. на всякий случай)  
            params.append({
                'id': i['id'],
                'title': i['title'],
                'value': valuesId[i['id']],
            })
    return params


def getValues(arr, valId): # Метод для работы с массивами values
    valus = {
        'asValueTemp': '', # Здесь мы храним value, если id в Values.json имеется
        'arr': [] # Здесь мы храним обработанный массив
    }
    for i in arr:

        if valId in valuesId and valuesId[valId] == i['id']: # Проверяем на наличие id и совпадает ли он со значениями в values
            valus['asValueTemp'] = i['title'] 
        else:
            errors['error'] = {
                'message': 'Входные файлы некорректны'
            }

        if 'params' in i: # Если  в элементе есть массив params
            temp = getParams(i['params']) # Вызываем метод для работы с массивом params и сохраняем полученные данные
            valus['arr'].append({
                'id': i['id'],
                'title': i['title'],
                'params': temp, # Присваиваем обработанный массив params
            })
            
        else:
            valus['arr'].append({
                'id': i['id'],
                'title': i['title'],
            })
            

        
        
    return valus


for item in testStructure: # Основной цикл
    if 'values' in item: # Если  в элементе есть массив values
        temp = getValues(item['values'], item['id']) # Вызываем метод для работы с массивом values и сохраняем полученные данные
        data['params'].append({
            'id': item['id'],
            'title': item['title'],
            'value': temp['asValueTemp'], # Присваиваем value из совпавших с id элемента из массива values
            'values': temp['arr'] # Присваиваем обработанный массив values
        })
    else:
        data['params'].append({
            'id': item['id'],
            'title': item['title'],
            'value': valuesId[item['id']] # Присваиваем value из Values.json если в элементе нет массива values
        })


with open('StructureWithValues.json', 'w', encoding='utf-8') as outfile: # Сохранение файла
    json.dump(data, outfile, ensure_ascii=False)

with open('error.json', 'w', encoding='utf-8') as errFile: # Сохранение файла
    json.dump(errors, errFile, ensure_ascii=False)
