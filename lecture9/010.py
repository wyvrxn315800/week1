phoenbook = {'suphakeat':'777-55555','mickey':'8889-9999','donal':'333-7777'}
print(phoenbook)
print(phoenbook['mickey'])
print(phoenbook.get('donal'))
key = 'Pluto'
if key in phoenbook:
    print(phoenbook['Pluto'])
else:
    print(key + 'not in phone book')
phoenbook['Simpson'] = '777-4567'
phoenbook['Pluto'] = '777-4444'
phoenbook['mickey'] = '777-2122'
print(phoenbook)
del phoenbook['Simpson']
print(phoenbook)