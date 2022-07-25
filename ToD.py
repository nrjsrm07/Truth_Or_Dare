import random
truth_items = [['Truth Level_1 Question 1',
                'Truth Level_1 Question 2',
                'Truth Level_1 Question 3',
                'Truth Level_1 Question 4',
               'Truth Level_1 Question 5'],
               
               ['Truth Level_2 Question 1',
               'Truth Level_2 Question 2',
               'Truth Level_2 Question 3',
               'Truth Level_2 Question 4',
               'Truth Level_2 Question 5'],
               
               ['Truth Level_3 Question 1',
               'Truth Level_3 Question 2',
               'Truth Level_3 Question 3',
               'Truth Level_3 Question 4',
               'Truth Level_3 Question 5']]
                
dare_items  = [['Dare Level_1 Question 1',
               'Dare Level_1 Question 2',
               'Dare Level_1 Question 3',
               'Dare Level_1 Question 4',
               'Dare Level_1 Question 5'],
               
               ['Dare Level_2 Question 1',
               'Dare Level_2 Question 2',
               'Dare Level_2 Question 3',
               'Dare Level_2 Question 4',
               'Dare Level_2 Question 5'],
               
               ['Dare Level_3 Question 1',
               'Dare Level_3 Question 2',
               'Dare Level_3 Question 3',
               'Dare Level_3 Question 4',
               'Dare Level_3 Question 5']]

number_of_players = int(input('How many people wants to play?'))
list_of_players = []

for i in range(number_of_players) :
    player_name = input("Please enter player's name : ")
    list_of_players.append(player_name)

answer = "yes"
current_level=0                         
while answer == "yes" or answer == "y" :
    for i in range(number_of_players):
        print(f'Its {list_of_players[i]}\'s  turn')

        truth_dare = input('Please choose "Truth" or "Dare" [T/D] : ')

        if truth_dare.lower() == 'truth' or truth_dare.lower() == 't':
            print(random.choice(truth_items[current_level]))
        else:
            print(random.choice(dare_items[current_level]))

    answer=input("Do you wanna continue the game?[Yes/No]: ")
    if answer.lower()=="no" or answer.lower()=='n':
        pass
    else:
        level_up =input("Do you wanna level Up the game?[Yes/No]: ")
        if level_up.lower()=="yes" or level_up.lower() == "y":
            current_level+=1
        else:
            pass
else:
    print("Thanks for playing beautiful game")