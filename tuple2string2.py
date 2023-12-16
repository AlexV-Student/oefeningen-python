def tuple_to_string(t, sep =' '):
	s = ''
	for i in range(len(t)):
		s+=str(t[i])
		if i < len(t) -1:
			s+=sep
	return s

if __name__ == '__main__':
	t = ('appel', 'peer', 22, 5.0)
	print(tuple_to_string(t))
	print(tuple_to_string(t, ' - '))