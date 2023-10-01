class FootballTeam:
	def __init__(self, name, wins, loss, draws, scored, conceded):
		self.name = name
		self.wins = wins
		self.loss = loss
		self.draws = draws
		self.scored = scored
		self.conceded = conceded
	
	def get_total_point(self):
		return (self.wins * 3 + 0 * self.loss + 1 * self.draws)
	
	def get_goal_difference(self):
		return (self.scored - self.conceded)
	
teams = []
teams_input = input("Enter Input : ").split('/')
for team in teams_input:
	arg = team.split(',')
	team_instant = FootballTeam(arg[0], int(arg[1]), int(arg[2]), int(arg[3]), int(arg[4]), int(arg[5]))
	teams.append(team_instant)

n = len(teams)

i = 0
while (i < n):
	j = i + 1
	while (j < n):
		if (teams[i].get_total_point() < teams[j].get_total_point()):
			teams[i], teams[j] = teams[j], teams[i]
		elif (teams[i].get_total_point() == teams[j].get_total_point()):
			if (teams[i].get_goal_difference() < teams[j].get_goal_difference()):
				teams[i], teams[j] = teams[j], teams[i]
		j += 1
	i += 1

for team in teams:
	print(team.name)


