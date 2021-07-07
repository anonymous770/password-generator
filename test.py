characters = list('abcdefghijklmnopqrstuvwxyz')

if request.GET.get('uppercase'):
	characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

if request.GET.get('special'):
	characters.extend(list('!@#$%^&*~()_+?'))

if request.GET.get('numbers'):
	characters.extend(list('0123456789'))

ength = int(request.GET.get('length'))
pas = ""
for x in range(length):
	pas += random.choice(characters)

