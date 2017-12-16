from service.FirstFollow import FirstFollow
from util.FileReader import get_file_content

container = get_file_content("dummy.in")
print(container)
# print(container.getDict())
# firstFollow = FirstFollow(container, "S")
# print(firstFollow)