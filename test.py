
import re

match = re.fullmatch(r'\b\w\w.{1,2}\s.{2,3}', r're1 asd')
print(match[0] if match else 'Not found')

match = re.search(r'\b\w\w.{2}\s\b..]', r'!!!001 обрезано свечение в анимации')
print(match[0] if match else 'Not found')