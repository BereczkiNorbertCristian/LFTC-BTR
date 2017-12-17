from service.CanonicalItems import CanonicalItems
from service.CheckingService import CheckingService
from service.FirstFollow import FirstFollow
from util.FileReader import get_file_content

container = get_file_content("dummy.in")
# print(container)
# print(container.getDict())
firstFollow = FirstFollow(container, "S")
print(firstFollow)
canonicalItems = CanonicalItems(container, firstFollow)
print(canonicalItems)
checkingService = CheckingService(canonicalItems, container)
print()
if checkingService.checkSequence(["a", "c", "a"]):
    print("Accepted")
else:
    print("Not accepted")