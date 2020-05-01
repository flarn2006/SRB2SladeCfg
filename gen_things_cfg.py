colors = ['{0, 0, 0}', '{0, 0, 170}', '{0, 170, 0}', '{0, 170, 170}', '{170, 0, 0}', '{170, 0, 170}', '{170, 85, 0}', '{170, 170, 170}',
	'{85, 85, 85}', '{85, 85, 255}', '{85, 255, 85}', '{85, 255, 255}', '{255, 85, 85}', '{255, 85, 255}', '{255, 255, 85}', '{255, 255, 255}',
	'{255, 170, 255}', '{255, 160, 0}', '{255, 210, 0}', '{255, 253, 208}']

def resetThing():
	global thingnum, title, sprite, width, height
	thingnum = None
	title = None
	sprite = None
	width = None
	height = None

def resetGroup():
	global color
	color = None
	resetThing()

resetGroup()

with open('things22.txt', 'r') as f:
	for line in f:
		tabs = 0
		for ch in line:
			if ch == '\t':
				tabs += 1
			else:
				break

		equals = line.find('=')
		if equals == -1:
			key = None
			value = line.strip('\t\n ;')
		else:
			key = line[:equals].strip()
			value = line[equals+1:].strip()

		if tabs == 1:
			if key is None and value == '}':
				print('\t}\n')
				resetGroup()
		elif tabs == 2:
			if key == 'title':
				print('\tgroup {}\n\t{{'.format(value.rstrip(';')), end='')
				if color is not None:
					print('\n\t\tcolour = ' + color)
			elif key == 'color':
				try:
					color = colors[int(value[:value.index(';')])]
				except (ValueError, IndexError):
					color = '{255, 0, 0}  // WARNING: Invalid color line encountered: ' + line
			elif key is None:
				if value.isnumeric():
					thingnum = int(value)
				elif value == '}' and thingnum is not None:
					print('\n\t\tthing {}\n\t\t{{'.format(thingnum))
					print('\t\t\tname = '+title)
					if sprite is not None:
						print('\t\t\tsprite = '+sprite)
					#if width is not None:
					#	print('\t\t\tradius = '+width)
					#if height is not None:
					#	print('\t\t\theight = '+height)
					print('\t\t}')
					resetThing()
		elif tabs == 3:
			if key == 'title':
				title = value
			elif key == 'sprite':
				sprite = '"{}?";'.format(value.strip('";').replace('internal:', '')[:5])
			elif key == 'width':
				width = value
			elif key == 'height':
				height = value

