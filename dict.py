wether = {'city': 'Москва', 'temperature': '20'}
print(wether['city'])
wether['temperature'] = int(wether['temperature']) - 5
print(wether)

#print(wether.get('country', 'Россия'))
wether.setdefault('country', 'Россия')
wether['date'] = '27.05.2019'
print(wether)
print(len(wether))