DIRECTIONS = {
	'N' : {'L':'W', 'R':'E'},
	'W' : {'L':'S', 'R':'N'},
	'S' : {'L':'E', 'R':'W'},
	'E' : {'L':'N', 'R':'S'}
}

MOVE_COORDINATES = {
	'N' : [0, 1],
	'S' : [0,-1],
	'W' : [-1,0],
	'E' : [1, 0]	
}

def move(rover, moves):
	for move in moves:
		if (move=='L') or (move=='R'):
			rover['direction'] = DIRECTIONS[rover['direction']][move]
		elif(move=='M'):
			rover['start_point'][0] = int(rover['start_point'][0]) + int(MOVE_COORDINATES[rover['direction']][0]) 
			rover['start_point'][1] = int(rover['start_point'][1]) + int(MOVE_COORDINATES[rover['direction']][1]) 
		
def toString(rover):
	return ' '.join(map(str, rover['start_point']))+ " "+ rover['direction']


end_coordinates = raw_input().split()
first_rovers_points = raw_input().split()
first_rovers_start_point = first_rovers_points[:2]

first_rover =  { 
				'start_point' : first_rovers_start_point,
				'direction' : first_rovers_points[2],
				}
first_rovers_moves = raw_input()
move(first_rover, first_rovers_moves)


second_rovers_point = raw_input().split()
second_rovers_start_point = second_rovers_point[:2]
second_rover =  { 
				'start_point' : second_rovers_start_point,
				'direction' : second_rovers_point[2],
				}

second_rovers_moves = raw_input()
move(second_rover, second_rovers_moves)

print('\n')
print(toString(first_rover))
print(toString(second_rover))
