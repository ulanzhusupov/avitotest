import json


def load_data(filename, encoding='utf-8'):
    with open(filename, encoding=encoding) as json_file:
        return json.load(json_file)


values = load_data('Values.json')
structure = load_data('TestCaseStructure.json')


data = {}
data["params"] = []

valuesArr = values['values']
testStructure = structure['params']


forParams = {
    'id': None,
    'title': None,
    'value': None
}

forValues = {
    'id': None,
    'title': None,
    'value': None
}
count = 0

def get_object_data(someValues, valueNum):
    obj = {}
    for item in someValues:
        if valueNum == item['id']: # Если id равен на value из Value.json
            forValues['value'] = item['title']
            count = count+1

        if 'params' not in item:
            obj['id'] = str(item['id'])
            obj['title'] = item['title']
        else:
            obj['id'] = str(item['id'])
            obj['title'] = item['title']
            obj['params'] = []
            for paramItems in item['params']: # Цикл для params
                obj['params'].append({
                    'id': str(paramItems['id']),
                    'title': paramItems['title'],
                    'value': None,
                    'values': []
                })
                for valuesItem in paramItems['values']: # Цикл для values внутри params
                    if valuesArr[count]['value'] == valuesItem['id']:
                        obj['params']['value'] = valuesItem['title']
                        count = count + 1

                    obj['params']['values'].append({
                        'id': str(valuesItem['id']),
                        'title': valuesItem['title']
                    })
        forValues['values'].append(obj) # Присваиваем объект в forValues
        count = count+1



for item in testStructure:
    if 'values' not in item:
        forParams['id'] = str(item['id'])
        forParams['title'] = str(item['title'])
        forParams['value'] = str(valuesArr[count]['value'])

        data['params'].append(forParams) # Добавляем объект к params
    else:
        forValues['id'] = str(item['id'])
        forValues['title'] = str(item['title'])
        get_object_data(item['values'], valuesArr[count]['value'])

        data['params'].append(forValues) # Добавляем объект к params
    count = count+1

print(data)


