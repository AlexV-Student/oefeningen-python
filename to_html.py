try:
	with open('devops_copy.txt', 'r') as python_file:
		python_string = python_file.read()

	html_string = python_string.replace('\n', '<br>')

	with open('devops_copy.html', 'w') as html_file:
		html_file.write(html_string)
	print(0)
except:
	print(-1)

