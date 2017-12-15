
from Terminal import Terminal
from NonTerminal import NonTerminal



class Container(object):

	def __init__(self):
		self.dict = {}
		self.lst = []

	def addTuple(self,left,right):
		if left.islower():
			raise Exception("Left side should not be small letter: " + left)
		rightLst = []
		for i in range(0,len(right)):
			toAppend = None
			if right[i].islower():
				toAppend = Terminal(right[i])
			else:
				toAppend = NonTerminal(right[i])
			rightLst.append(toAppend)
		if not left in self.dict.keys():
			self.dict[left] = []
		self.dict[left].append(rightLst)
		self.lst.append((left,rightLst))

	# expressionsForNonTerminal gives the list of expressions for a nonTermial
	# 	doesn't matter what you send as parameter either string or NonTermial
	def expressionsForNonTerminal(self,nonTerminal):

		key = None
		if isinstance(nonTerminal,str):
			key = nonTerminal
		if isinstance(nonTerminal,NonTerminal):
			key = nonTerminal.c
		return self.dict[key]

	# getDict returns a dict which has the following:
	# 	key (left non terminal) -> val (list of lists meaning a list of expressions)
	# 	for the given nonTerminal
	def getDict(self):
		return self.dict

	# getList returns a list of tuples of the form (nonTermial,expression) 
	# 	expression if formed from terminals and non termials	
	def getList(self):
		return self.lst

	@staticmethod
	def printList(lst):
		ret = "\nList:["
		for el in lst:
			ret += el.c + ","
		ret += "]\n"
		return ret

	def __str__(self):
		ret = ""
		for k,lst in self.lst:
			ret += k + "->" + Container.printList(lst)
		ret += "Dict:{"
		for k in self.dict.keys():
			ret += "\n"
			ret += k + "->"
			val = self.dict[k]
			for lst in val:
				ret += Container.printList(lst)

		ret += "}\n"
		return ret


