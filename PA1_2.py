import csv
# Open and read a file
file_read = "assignment1.csv"
fin = open(file_read, "r")
nba_data = []
for line in fin:
    nba_data.append(line)
fin.close()


############################################################
# Print what types of data dimensions are there
############################################################
for index, line in enumerate(nba_data):
    if index == 0:
        print(line.split(","))

print(nba_data[0:3])

############################################################
# Modification #1. Change weight that is 'N/A' to 100 
############################################################
nba_data_corrected = []
for index, line in enumerate(nba_data):
    player = line.split(",")
    player_weight = player[27]
    if player_weight == 'N/A':
        player[27] = 100
    nba_data_corrected.append(player)



############################################################
# Modification #2. Remove columns weight_kg 
############################################################

for player in nba_data_corrected:
    del player[28]


############################################################
# Modification #3. Modify column nationality to remove \n 
############################################################

for player in nba_data_corrected:
    player[28] = player[28].strip()

############################################################
# Modification #4. Modify column birth_month to numerical equivalent \n 
############################################################

d = {'Jan' : 1, 'Feb' : 2 , 'Mar' : 3, 'Apr' : 4, 'May': 5 , 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
#remove rows with unkonwn birth month
nba_data_corrected1 = []
nba_data_corrected1.append(nba_data_corrected[0])
for index,player in enumerate(nba_data_corrected):
    if index != 0:
        if player[23] != '':
            nba_data_corrected1.append(player)

#map to dictionary value 
for index,player in enumerate(nba_data_corrected1):
    if index != 0:
        player[23] = d[player[23]]
    
############################################################
# Modification #5. Add a column for league year extracted from column Season \n 
############################################################
for index, player in enumerate(nba_data_corrected1):
    year = player[1][0:4]
    if index == 0:
        player.append('year')
    else:
        player.append(int(year))
############################################################
# write a file
############################################################
with open("nba_corrected.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(nba_data_corrected1)
print("writing complete")

