from service.CanonicalItems import CanonicalItems
from service.CheckingService import CheckingService
from service.FirstFollow import FirstFollow
from util.FileReader import get_file_content

def read_pif(filename):
	ret = []
	with open(filename) as f:
		for line in f:
			for elem in line.split(","):
				ret.append(elem)
	return ret

container = get_file_content("dummy.in")
# print(container)
# print(container.getDict())
firstFollow = FirstFollow(container, "input")
# print(firstFollow)
canonicalItems = CanonicalItems(container, firstFollow)
# print(canonicalItems)
checkingService = CheckingService(canonicalItems, container)

pifList = read_pif("program.in")

if checkingService.checkSequence(pifList):
    print("Accepted")
else:
    print("Not accepted")