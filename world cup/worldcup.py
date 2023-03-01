options = input("A: Total number of goals scored by a given country\nB: Total number of goals scored by a given player\nC: List the name of all the players who scored for a given country\nD: Total number of goals by all countries\nE: Total number of goals scored during the first half (45 minutes)\nF: Total number of goals scored during the second half (45 minutes to 90 minutes)\nG: Total number of goals scored during extra time (after 90 minutes of play)\nH: List the total number of goals scored for each country\nI: List the total number of goals scored for each player\nJ: Which country scored the most goals?\nK: Which player scored the most goals?\nX: Exit?\n")
file = open("goals.txt","r")
data = file.readlines()
new_data = [a.split(";") for a in data]
# Code of option A
def total_number_of_goals_scored_by_a_given_country():
    input_country = input("Enter a country: ")
    calculator_country = 0
    for i in new_data:
        if input_country == i[1]:
            calculator_country += 1
    if calculator_country == 0:
        print("\n{} did not score in the 2018 World Cup or {} did not participate in the 2018 World Cup.".format(input_country,input_country))
    elif calculator_country == 1:
        print("\n{} scored {} goal in the 2018 World Cup.".format(input_country,calculator_country))
    else:
        print("\n{} scored {} goals in the 2018 World Cup.".format(input_country,calculator_country))
# Code of option B
def total_number_of_goals_scored_by_a_given_player():
    input_player = input("Enter a player: ") 
    calculator_player = 0
    for i in new_data:
        if input_player == i[0]:
            calculator_player += 1
    if calculator_player == 0:
        print("\n{} did not score in the 2018 World Cup or {} did not participate in the 2018 World Cup.".format(input_player,input_player))
    elif calculator_player == 1:
        print("\n{} scored {} goal in the 2018 World Cup.".format(input_player,calculator_player))
    else:
        print("\n{} scored {} goals in the 2018 World Cup.".format(input_player,calculator_player))
# Code of option C
def list_the_name_of_all_the_players_who_scored_for_a_given_country():
    input_country = input("Enter a country: ")
    players = set()
    for i in new_data:
        if input_country == i[1]:
            players.add(i[0])
    print("\nGoal scorers for {} in the 2018 World Cup:\n".format(input_country))
    for j in sorted(players):
        print(j)
# Code of option D
def total_number_of_goals_by_all_countries():
    print("\nTotal number of goals by all countries is {} in the 2018 World Cup.".format(len(new_data)))
# Code of option E
def total_number_of_goals_scored_during_the_first_half():
    calculator_first_half = 0
    for i in new_data:
        if int(i[2]) <= 45:
            calculator_first_half += 1
    print("\nThe total number of goals scored in the first half is {} in the 2018 World Cup.".format(calculator_first_half))
# Code of option F
def total_number_of_goals_scored_during_the_second_half():
    calculator_second_half = 0
    for i in new_data:
        if 45 < int(i[2]) <= 90:
            calculator_second_half += 1
    print("\nThe total number of goals scored in the second half is {} in the 2018 World Cup.".format(calculator_second_half))
# Code of option G
def total_number_of_goals_scored_during_extra_time():
    calculator_extra_time = 0
    for i in new_data:
        if 90 < int(i[2]):
            calculator_extra_time += 1
    print("\nThe total number of goals scored in the extra time is {} in the 2018 World Cup.".format(calculator_extra_time))
# Code of option H
def list_the_total_number_of_goals_scored_for_each_country():
    new_data.sort(key=lambda x: x[1])
    variable = new_data[0][1]
    calculator_each_country = 0
    for i in new_data:
        if variable == i[1]:
            calculator_each_country += 1
        else:
            print("\n{} scored {} goals in the 2018 World Cup.".format(variable,calculator_each_country))
            variable = i[1]
            calculator_each_country = 1
def list_the_total_number_of_goals_scored_for_each_player():
    new_data.sort(key=lambda x: x[0])
    variable = new_data[0][0]
    calculator_each_player = 0
    for i in new_data:
        if variable == i[0]:
            calculator_each_player += 1
        else:
            print("\n{} scored {} goals in the 2018 World Cup.".format(variable,calculator_each_player))
            variable = i[0]
            calculator_each_player = 1
# Code of option J
def which_country_scored_the_most_goals():
    f = open("goals.txt","r")
    goals = {}
    for line in f:
        fields = line.strip().split(';')
        country = fields[1]
        if country in goals:
            goals[country] += 1
        else:
            goals[country] = 1
    most_goals_country = max(goals, key=goals.get)
    print("\n{} scored the most goals with {} goals in the 2018 World Cup.".format(most_goals_country,goals[most_goals_country]))
# Code of option K
def which_player_scored_the_most_goals():
    f = open("goals.txt","r")
    goals = {}
    for line in f:
        fields = line.strip().split(';')
        player = fields[0]
        if player in goals:
            goals[player] += 1
        else:
            goals[player] = 1
    most_goals_player = max(goals, key=goals.get)
    print("\n{} scored the most goals with {} goals in the 2018 World Cup.".format(most_goals_player,goals[most_goals_player]))
# Choose one of the options
while options != "X":
    if options == "A":
        total_number_of_goals_scored_by_a_given_country()
    elif options == "B":
        total_number_of_goals_scored_by_a_given_player()
    elif options == "C":
        list_the_name_of_all_the_players_who_scored_for_a_given_country()
    elif options == "D":
        total_number_of_goals_by_all_countries()
    elif options == "E":
        total_number_of_goals_scored_during_the_first_half()
    elif options == "F":
        total_number_of_goals_scored_during_the_second_half()
    elif options == "G":
        total_number_of_goals_scored_during_extra_time()
    elif options == "H":
        list_the_total_number_of_goals_scored_for_each_country()
    elif options == "I":
        list_the_total_number_of_goals_scored_for_each_player()
    elif options == "J":
        which_country_scored_the_most_goals()
    elif options == "K":
        which_player_scored_the_most_goals()
    options = input("\nA: Total number of goals scored by a given country\nB: Total number of goals scored by a given player\nC: List the name of all the players who scored for a given country\nD: Total number of goals by all countries\nE: Total number of goals scored during the first half (45 minutes)\nF: Total number of goals scored during the second half (45 minutes to 90 minutes)\nG: Total number of goals scored during extra time (after 90 minutes of play)\nH: List the total number of goals scored for each country\nI: List the total number of goals scored for each player\nJ: Which country scored the most goals?\nK: Which player scored the most goals?\nX: Exit?\n")