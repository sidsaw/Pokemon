import copy
import csv
aquaplayers = ['Joe', 'Sahil', 'Mayur', 'Kush', 'Quresh', 'Deepak', 'Alex', 'Niketh', 'Branden']
magmaplayers = ['Sid', 'Parth', 'Prakash', 'Samarth', 'Darshil', 'Julian', 'Samuel', 'Sumit', 'Alishah']

def rotate(arr):
	rotated = copy.deepcopy(arr)
	for i in range(len(arr) - 1):
		rotated[i + 1] = arr[i]

	rotated[0] = arr[len(arr) - 1]
	return rotated


writer = csv.writer(open('xgames.csv', 'wb'))

for i in range(9):
	print(magmaplayers)
	print(aquaplayers)
	for j in range(len(aquaplayers)):
		match = []
		match.append(i + 1)
		match.append(aquaplayers[j])
		match.append(magmaplayers[j])
		writer.writerow(match)
	aquaplayers = rotate(aquaplayers)

