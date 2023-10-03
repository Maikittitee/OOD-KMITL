
class Monkey:
	def __init__(self, name, strength, intelligence, agility, id):
		self.name = name
		self.str = strength
		self.int = intelligence
		self.agi = agility
		self.id = id
		self.data = {"name":name, "str":strength, "int":intelligence, "agi":agility, "id":id}
		
	def __repr__(self) -> str:
		return (self.name)


def merge_sort(my_list, pior):

	if len(my_list) <= 1:
		return my_list
   
	list_1 = my_list[0:len(my_list) // 2]
	list_2 = my_list[len(my_list) // 2:]
	
	return (sort_two_list(merge_sort(list_1, pior), merge_sort(list_2, pior), pior))



# Separate Function to sort and merge 2 sorted lists
def sort_two_list(list_1, list_2, piority):
	final_list = []
	i = 0
	j = 0
	s = 0
	n_pior = len(piority)
	while i < len(list_1) and j < len(list_2):
		if list_1[i].data[piority[s]] < list_2[j].data[piority[s]]:
			final_list.append(list_1[i])
			i += 1
			continue
		elif (s < n_pior and list_1[i].data[piority[s]] == list_2[j].data[piority[s]]):
			s += 1
			if (s < n_pior and list_1[i].data[piority[s]] < list_2[j].data[piority[s]]):
				final_list.append(list_1[i])
				i += 1
				continue	
			elif (s < n_pior and list_1[i].data[piority[s]] == list_2[j].data[piority[s]]):
				s += 1
				if (s < n_pior and list_1[i].data[piority[s]] < list_2[j].data[piority[s]]):
					final_list.append(list_1[i])
					i += 1
					continue	
		else:
			final_list.append(list_2[j])
			j += 1

	while i < len(list_1):
		final_list.append(list_1[i])
		i = i + 1
		
	while j < len(list_2):
		final_list.append(list_2[j])
		j = j + 1
		
	return final_list

l = []
l.append(Monkey("mai",5,1,1,1))
l.append(Monkey("dick",4,3,1,1))
l.append(Monkey("jack",4,2,1,1))
pior = ["str", "int"]
print(merge_sort(l, pior))


