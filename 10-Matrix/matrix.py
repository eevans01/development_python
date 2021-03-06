w = 4 #Creates a variable named "w" with a value of 4. This represents the width of the matrix.
h = 11 #Creates a variable named "h" with a value of 11. This represents the height of the matrix.
teams = [[0 for x in range(w)] for y in range(h)] #Creates a matrix named "a" using a for loop that is w by h in size. The matrix at this point is filled with 0 in every index.
#Matrix Population - Part 1 (Team Numbers)
teams[0][0] = "127" #Enters the value "127" into index 0,0 of matrix "teams".
teams[1][0] = "5443" #Enters the value of "5443" into the index of 1,0 of matrix "teams".
teams[2][0] = "9402" #Enters the value "9402" into the index of 2,0 of matrix "teams".
teams[3][0] = "9403" #Enters the value "9403" into the index of 3,0 of matrix "teams".
teams[4][0] = "10143" #Enters the value "10143" into the index of 4,0 of matrix "teams".
teams[5][0] = "11085" #Enters the value "11085" into the index of 5,0 of matrix "teams".
teams[6][0] = "11242" #Enters the value "11242" into the index of 6,0 of matrix "teams".
teams[7][0] = "12645" #Enters the value "12645" into the index of 7,0 of matrix "teams".
teams[8][0] = "12650" #Enters the value "12650" into the index of 8,0 of matrix "teams".
teams[9][0] = "12992" #Enters the value "12992" into the index of 9,0 of matrix "teams".
teams[10][0] = "13905" #Enters the value "13905" into the index of 10,0 of matrix "teams".
#Matrix Population - Part 2 (Team Names)
teams[0][1] = "The Fighting Pickles" #Enters the value "The Fighting Pickles" into the index of 0,3 of matrix "teams".
teams[1][1] = "Synergy" #Enters the value "Synergy" into the index of 1,3 of matrix "teams".
teams[2][1] = "Hive of Steel" #Enters the value "Hive of Steel" into the index of 2,3 of matrix "teams".
teams[3][1] = "CyberSwarm" #Enters the value "CyberSwarm" into the index of 3,3 of matrix "teams".
teams[4][1] = "Bits and Bots" #Enters the value "Bits and Bots" into the index of 4,3 of matrix "teams".
teams[5][1] = "Mad Hackers" #Enters the value "Mad Hackers" into the index of 5,3 of matrix "teams".
teams[6][1] = "ERROR 451" #Enters the value "ERROR 451" into the index of 6,3 of matrix "teams".
teams[7][1] = "S.C.R.E.W. Ups" #Enters the value "S.C.R.E.W. Ups" into the index of 7,3 of matrix "teams".
teams[8][1] = "Cannot Compute" #Enters the value "Cannot Compute" into the index of 8,3 of matrix "teams".
teams[9][1] = "Vindicators" #Enters the value "Vindicators" into the index of 9,3 of matrix "teams".
teams[10][1] = "Eagles Robotics" #Enters the value "Eagles Robotics" into the index of 10,3 of matrix "teams".
#Matrix Population - Part 3 (Team Schools)
teams[0][2] = "Ben Barber Innovation Academy" #Enters the value "Ben Barber Innovation Academy" into the index of 0,1 of matrix "teams".
teams[1][2] = "Harmony School of Innovation" #Enters the value "Harmony School of Innovation" into the index of 1,1 of matrix "teams".
teams[2][2] = "Henderson Junior High School" #Enters the value "Henderson Junior High School" into the index of 2,1 of matrix "teams".
teams[3][2] = "Henderson Junior High School" #Enters the value "Henderson Junior High School" into the index of 3,1 of matrix "teams".
teams[4][2] = "Harmony School of Innovation" #Enters the value "Harmondy School of Innovation" into the index of 4,1 of matrix "teams".
teams[5][2] = "Mansfield High School" #Enters the value "Mansfield High School" into the index of 5,1 of matrix "teams".
teams[6][2] = "Ferris High School" #Enters the value "Ferris High School" into the index of 6,1 of matrix "teams".
teams[7][2] = "Ferris High School" #Enters the value "Ferris High School" into the index of 7,1 of matrix "teams".
teams[8][2] = "Ferris Junior High School" #Enters the value "Ferris Junior High School" into the index of 8,1 of matrix "teams".
teams[9][2] = "Italy High School" #Enters the value "Italy High School" into the index of 9,1 of matrix "teams".
teams[10][2] = "Faith Family Academy" #Enters the value "Faith Family Academy" into the index of 10,1 of matrix "teams".
#Matrix Population - Part 4 (Team Hometowns)
teams[0][3] = "Mansfield, TX" #Enters the value "Mansfield, TX" into the index of 0,2 of matrix "teams".
teams[1][3] = "Ft. Worth, TX" #Enters the value "Ft. Worth, TX" into the index of 1,2 of matrix "teams".
teams[2][3] = "Stephenville, TX" #Enters the value "Stephenville, TX" into the index of 2,2 of matrix "teams".
teams[3][3] = "Stephenville, TX" #Enters the value "Stephenville, TX" into the index of 3,2 of matrix "teams".
teams[4][3] = "Ft. Worth, TX" #Enters the value "Ft. Worth" into the index of 4,2 of matrix "teams".
teams[5][3] = "Mansfield, TX" #Enters the value "Mansfield, TX" into the index of 5,2 of matrix "teams".
teams[6][3] = "Ferris, TX" #Enters the value "Ferris, TX" into the index of 6,2 of matrix "teams".
teams[7][3] = "Ferris, TX" #Enters the value "Ferris, TX" into the index of 7,2 of matrix "teams".
teams[8][3] = "Ferris, TX" #Enters the value "Ferris, TX" into the index of 8,2 of matrix "teams".
teams[9][3] = "Italy, TX" #Enters the value "Italy, TX" into the index of 9,2 of matrix "teams".
teams[10][3] = "Waxahachie, TX" #Enters the value "Waxahacnie, TX" into the index of 10,2 of matrix "teams".
#Matrix Display
print(teams[0][0] + " - " + teams[0][1] + " - " + teams[0][2] + " - " + teams[0][3]) #Displays indices 0,0, 0,1, 0,2, and 0,3 concatenated with a hyphen between each index for formatting.
print(teams[1][0] + " - " + teams[1][1] + " - " + teams[1][2] + " - " + teams[1][3]) #Displays indices 1,0, 1,1, 1,2, and 1,3 concatenated with a hyphen between each index for formatting.
print(teams[2][0] + " - " + teams[2][1] + " - " + teams[2][2] + " - " + teams[2][3]) #Displays indices 2,0, 2,1, 2,2, and 2,3 concatenated with a hyphen between each index for formatting.
print(teams[3][0] + " - " + teams[3][1] + " - " + teams[3][2] + " - " + teams[3][3]) #Displays indices 3,0, 3,1, 3,2, and 3,3 concatenated with a hyphen between each index for formatting.
print(teams[4][0] + " - " + teams[4][1] + " - " + teams[4][2] + " - " + teams[4][3]) #Displays indices 4,0, 4,1, 4,2, and 4,3 concatenated with a hyphen between each index for formatting.
print(teams[5][0] + " - " + teams[5][1] + " - " + teams[5][2] + " - " + teams[5][3]) #Displays indices 5,0, 5,1, 5,2, and 5,3 concatenated with a hyphen between each index for formatting.
print(teams[6][0] + " - " + teams[6][1] + " - " + teams[6][2] + " - " + teams[6][3]) #Displays indices 6,0, 6,1, 6,2, and 6,3 concatenated with a hyphen between each index for formatting.
print(teams[7][0] + " - " + teams[7][1] + " - " + teams[7][2] + " - " + teams[7][3]) #Displays indices 7,0, 7,1, 7,2, and 7,3 concatenated with a hyphen between each index for formatting.
print(teams[8][0] + " - " + teams[8][1] + " - " + teams[8][2] + " - " + teams[8][3]) #Displays indices 8,0, 8,1, 8,2, and 8,3 concatenated with a hyphen between each index for formatting.
print(teams[9][0] + " - " + teams[9][1] + " - " + teams[9][2] + " - " + teams[9][3]) #Displays indices 9,0, 9,1, 9,2, and 9,3 concatenated with a hyphen between each index for formatting.
print(teams[10][0] + " - " + teams[10][1] + " - " + teams[10][2] + " - " + teams[10][3]) #Displays indices 10,0, 10,1, 10,2, and 10,3 concatenated with a hyphen between each index for formatting.