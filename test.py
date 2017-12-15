
from FileReader import get_file_content

container = get_file_content("dummy.in")

print(str(container))

print("_____________")
exprss = container.expressionsForNonTerminal("S")
for expr in exprss:
	print("Expression BEGIN:")
	for el in expr:
		print(el.isTerminal())
		print(el.c) #get the character for an object

	print("END")