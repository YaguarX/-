#import math


#class teams:
#    def __init__(self,points:int) -> None:
#        self.points = points
#        self.beg_poin = 0
#        self.current_points = current_points 


# как подставить ID в sql?
# как откатить назад,в случае чего?

ID = ['Yaroslav_0','Vital_1','Vasil_2','Ivan_3']

#for i in ID:
#    print(i)
sol = int(input('Введите свой ID:'))
los = int(input('Введите свой ID:'))
player_1 = ID[sol]
player_2 = ID[los]

score_1 = int(input('Счет_1_игрока:'))
score_2 = int(input('Счет_2_игрока:'))   
if score_1 > score_2:
    print('player_1 won')
elif score_1 == score_2:
    print('draw')
else:
    print('player_2 won')

team_1_stars = float(input('stars_1:'))
team_2_stars = float(input('stars_2:'))

points_1 = 0  
points_2 = 0

if team_1_stars == 5:
    points_1 += score_1 * 1
elif team_1_stars == 4.5:
    points_1 += score_1 * 1.2
elif team_1_stars == 4:
    points_1 += score_1 * 1.5
elif team_1_stars == 3.5:
    points_1 += score_1 * 1.8
elif team_1_stars == 3:
    points_1 += score_1 * 2
elif team_1_stars == 2.5:
    points_1 += score_1 * 2.5
elif team_1_stars == 2:
    points_1 += score_1 * 3
elif team_1_stars == 1.5:
    points_1 += score_1 * 3.5
elif team_1_stars == 1:
    points_1 += score_1 * 4
else:
    print('Что-то где-то ты ввел не так,проверь!')

if team_2_stars == 5:
    points_2 += score_2 * 1
elif team_2_stars == 4.5:
    points_2 += score_2 * 1.2
elif team_2_stars == 4:
    points_2 += score_2 * 1.4
elif team_2_stars == 3.5:
    points_2 += score_2 * 1.8
elif team_2_stars == 3:
    points_2 += score_2 * 2
elif team_2_stars == 2.5:
    points_2 += score_2 * 2.5
elif team_2_stars == 2:
    points_2 += score_2 * 3
elif team_2_stars == 1.5:
    points_2 += score_2 * 3.5
elif team_2_stars == 1:
    points_2 += score_2 * 4
else:
    print('Что-то где-то ты ввел не так,проверь!')
print(f'Игрок {player_1} получает:' ,points_1, 'очков')
print(f'Игрок {player_2} получает:' ,points_2, 'очков')


#points_1 += #ссылка на sql второго, где проставлено число за номер в таблице
#points_2 += #ссылка на sql первого, где проставлено число за номер в таблице


#def stars(player_1:float, player_2:float):
#    if player_1 == 5 and game_result == 'player_1 won':
#        self.current_points.add(3)
#    elif player_1 == 4.5 and game_result == 'player_1 won':
#        self.current_points.add(3)
#    elif player_1 == 4 and game_result == 'player_1 won':
#        self.current_points.add(3)


        

