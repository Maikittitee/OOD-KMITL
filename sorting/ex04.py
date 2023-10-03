
class Monkey:
	def __init__(self, name, strength, intelligence, agility, id):
		self.name = name
		self.str = strength
		self.int = intelligence
		self.agi = agility
		self.id = id
		self.data = {"name":name, "str":strength, "int":intelligence, "agi":agility, "id":id}
		
	def __repr__(self) -> str:
		return (f"{self.id}-{self.name}")


def merge_sort(my_list, pior):

	if len(my_list) <= 1:
		return my_list

	if (len(pior) == 1 and pior[0] == ''):
		return (my_list)
   
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
		s = 0
		if s < n_pior and list_1[i].data[piority[s]] < list_2[j].data[piority[s]]:
			final_list.append(list_1[i])
			i += 1
			continue
		if (s < n_pior and list_1[i].data[piority[s]] == list_2[j].data[piority[s]]):
			s += 1
			if (s < n_pior and list_1[i].data[piority[s]] < list_2[j].data[piority[s]]):
				final_list.append(list_1[i])
				i += 1
				continue	
			if (s < n_pior and list_1[i].data[piority[s]] == list_2[j].data[piority[s]]):
				s += 1
				if (s < n_pior and list_1[i].data[piority[s]] < list_2[j].data[piority[s]]):
					final_list.append(list_1[i])
					i += 1
					continue
				if (s < n_pior and list_1[i].data[piority[s]] == list_2[j].data[piority[s]]):
					s += 1
					if (s < n_pior and list_1[i].data[piority[s]] < list_2[j].data[piority[s]]):
						final_list.append(list_1[i])
						i += 1
						continue
					if (s < n_pior and list_1[i].data[piority[s]] == list_2[j].data[piority[s]]):
						s += 1
						if (s < n_pior and list_1[i].data[piority[s]] < list_2[j].data[piority[s]]):
							final_list.append(list_1[i])
							i += 1
							continue
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

inp = input("Enter Input: ").split('/')
mode = inp[0]
if (mode == 'D'):
	reverse = True
else:
	reverse = False
pior = inp[1].split(',')
arg = inp[2].split(',')
for i in range(len(arg)):
	name,stre,intel,agi = arg[i].split()
	l.append(Monkey(name,int(stre),int(intel),int(agi),int(i)))

print(f"pior is {pior}")
sorted_list = merge_sort(l, pior)
if (reverse):
	sorted_list = list(reversed(sorted_list))
print(sorted_list)

