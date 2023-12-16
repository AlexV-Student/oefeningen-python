import os
from os import path
import shutil

try:
	file = shutil.copy('devops.txt', 'devops_copy.txt')
	print(0)
except:
	print(-1)