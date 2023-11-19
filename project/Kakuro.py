#### ------------------------------------------------------------------------------------
#                            Introduction : Monte-Carlo Kakuro
#
#    A rendre 15/04/2018
#    Pas de rapport, just description et code
#    Nested Monte-Carlo Search, Recherche Monte-Corlo impriquee
#    On resout un KAKURO suivant
#          24 25 20 26 24
#       18 .  .  .  .  .
#       26 .  .  .  .  .
#       28 .  .  .  .  .
#       26 .  .  .  .  .
#       21 .  .  .  .  .
#   Les chiffres sont compris entre 1 et 9, remplir les cases aleatoirement une par une
#   Tous les nombres sont differents sur chaque ligne et chaque colonne
#### ------------------------------------------------------------------------------------

import time
import random

# Init:  Affectation de la table Kakuro
Kakuro = [[0 for x in range(6)] for x in range(6)]
Kakuro = [[0, 24, 25, 20, 26, 24], # the sum of the integers of the last column has to be 24.
          [18, 0, 0, 0, 0, 0], # The sum of the integers of the first row has to be 18
          [26, 0, 0, 0, 0, 0],
          [28, 0, 0, 0, 0, 0],
          [26, 0, 0, 0, 0, 0],
          [21, 0, 0, 0, 0, 0]]

# Init: Affectation de la table Domains des Free Variables
domainTableSize = [[0 for x in range(9)] for x in range(25)]
for i in range(0,25):
    for j in range(0,9):
        domainTableSize[i][j] = j + 1

# This fonction shows all the values in the table
def ShowTable(table):
    k = 0
    while k < len(table):
        print(table[k])
        k = k + 1

# This fonction check there is not a free variable in the table
def CheckFreeVariable(table):
    for i in range(1,6):
        for j in range(1,6):
            if table[i][j] == 0:
                return False
    return True

# This fonction check a domain is Empty
def CheckADomainEmpty(domainTable):
    for i in range(0, 25):
        isEmpty = True
        for j in range(0, 9):
            if domainTable[i][j] != 0:
                isEmpty = False
        if isEmpty:
            return True
    return False

# ---------------------------------------------------------------------------- OK
# These fonctions check the inconsistent of the table Kakuro :
# If all the variables of the row have been assigned the sum is compared to the target sum and if it is different, the assignment is declared inconsistent.

def NotEmptyRow(i, table):
    notEmpty = True
    for j in range(1, 6):
        if table[i][j] == 0:
            notEmpty = False
    return notEmpty

def NotEmptyColumn(j, table):
    notEmpty = True
    for i in range(1, 6):
        if table[i][j] == 0:
            notEmpty = False
    return notEmpty

def CheckInConsistent(table):
    sumRows = 0
    for i in range(1, 6):
        if NotEmptyRow(i, table):
            for k in range(1, 6):
                sumRows = sumRows + table[i][k]
            if table[i][0] != sumRows:
                return True
            sumRows = 0

    sumColumns = 0
    for j in range(1, 6):
        if NotEmptyColumn(j, table):
            for k in range(1, 6):
                sumColumns = sumColumns + table[k][j]
            if table[0][j] != sumColumns:
                return True
            sumColumns = 0
    return False

# ---------------------------------------------------------------------------- OK
# These fonctions choose a variable from the table Kakuro
# Choose the variable that has the smallest domain size ! If not, choose the first free variable !

def VariableDomainSize(i, j, domainTable):
    size = 0
    for k in range(0, 9):
        if domainTable[(i - 1) * 5 + j - 1][k] != 0:
            size = size + 1
    return size

def firstFreeVariable(table):
    place = []
    for i in range(1,6):
        for j in range(1,6):
            if table[i][j] == 0:
                place.append(i)
                place.append(j)
                return place

def ChooseVariable(table, domainTable):
    place = []
    row = firstFreeVariable(table)[0]
    col = firstFreeVariable(table)[1]
    place.append(row)
    place.append(col)
    size = VariableDomainSize(row, col, domainTable)
    for i in range(1,6):
        for j in range(1,6):
            if table[i][j] == 0:
                if VariableDomainSize(i, j, domainTable) < size and VariableDomainSize(i, j, domainTable) != 0:
                    size = VariableDomainSize(i, j, domainTable)
                    place.pop(0)
                    place.pop(0)
                    place.append(i)
                    place.append(j)
    if size == VariableDomainSize(row, col, domainTable):
        place.pop(0)
        place.pop(0)
        place.append(row)
        place.append(col)
    return place

# ---------------------------------------------------------------------------- OK
# This fonction update domains of all the free variables in the table Kakuro
# 1. Each time a value is assigned to a variable, the value is removed from the domain of the free variables that are either in the same row or in the same column as the assigned variable.
# 2. All values that are greater than Maxval are removed from the domains of the free variables

def UpadteDomainsTable(table, domainTable):
    for i in range(1,6):
        for j in range(1,6):
            if table[i][j] != 0:
                row = (i - 1) * 5 + j - 1
                column = table[i][j]
                # Update every row and column
                if 0 <= row <= 4:
                    for k in range(0, 5):
                        domainTable[k][column - 1] = 0
                    for n in range(0, 5):
                        domainTable[row%5 + 5*n][column - 1] = 0
                if 5 <= row <= 9:
                    for k in range(0, 5):
                        domainTable[k + 5][column - 1] = 0
                    for n in range(0, 5):
                        domainTable[row%5 + 5*n][column - 1] = 0
                if 10 <= row <= 14:
                    for k in range(0, 5):
                        domainTable[k + 10][column - 1] = 0
                    for n in range(0, 5):
                        domainTable[row%5 + 5*n][column - 1] = 0
                if 15 <= row <= 19:
                    for k in range(0, 5):
                        domainTable[k + 15][column - 1] = 0
                    for n in range(0, 5):
                        domainTable[row%5 + 5*n][column - 1] = 0
                if 20 <= row <= 24:
                    for k in range(0, 5):
                        domainTable[k + 20][column - 1] = 0
                    for n in range(0, 5):
                        domainTable[row%5 + 5*n][column - 1] = 0
    # All value that are greater than M axval are removed from the domains of the free variables of the row.
    sumRows = 0
    Srow = 0
    for i in range(1, 6): # Update every row in the table
        for k in range(1, 6):
            sumRows = sumRows + table[i][k]
        Srow = table[i][0] - sumRows
        sumRows = 0
        for k in range(1, 6):
            for l in range(0, 9):
                if domainTable[(i - 1) * 5 + k - 1][l] > Srow:
                    domainTable[(i - 1) * 5 + k - 1][l] = 0
    sumColumns = 0
    Scolumns = 0
    for j in range(1, 6): # Update every column in the table
        for k in range(1, 6):
            sumColumns = sumColumns + table[k][j]
        Scolumns = table[0][j] - sumColumns
        sumColumns = 0
        for k in range(1, 6):
            for l in range(0, 9):
                if domainTable[(k - 1) * 5 + j - 1][l] > Scolumns:
                    domainTable[(k - 1) * 5 + j - 1][l] = 0


#### ------------------------------------------------------------------------------------ OK
#### Search Algorithms 1 : Forward Checking
#### Forward Checking search is a depth first search that chooses a variable at each node, tries all the values in the domain of this variable and recursively
#### calls itself until a domain is empty or a solution is found.
#### ------------------------------------------------------------------------------------

def ForwardChecking(table, domainTable):
    if CheckFreeVariable(table):
        return True
    row = ChooseVariable(table, domainTable)[0]
    column = ChooseVariable(table, domainTable)[1]
    for j in range(0, 9):
        value = domainTable[(row - 1) * 5 + column - 1][j]
        if value != 0:
            table[row][column] = value
            UpadteDomainsTable(table, domainTable)
            if not CheckADomainEmpty(domainTable) or CheckInConsistent(table):
                if ForwardChecking(table, domainTable):
                    return True
    return False


#### ------------------------------------------------------------------------------------ OK
###  Search Algorithms 2 : Iterative Sampling
###  A sample consists in choosing a variable, assigning a possible value to it, updating the domains of the other free variables and looping until a solution
###  is found or a variable with an empty domain is found.
#### ------------------------------------------------------------------------------------

def FindNumberVaribale(table):
    num = 0
    for i in range(1,6):
        for j in range(1,6):
            if table[i][j] == 0:
                num = num + 1
    return num

# This fonction check a variable with an empty domain
def FindDomainEmpty(table, domainTable):
    for i in range(1, 6):
        for j in range(1, 6):
            if table[i][j] == 0:
                isEmpty = True
                for k in range(0, 9):
                    if domainTable[(i - 1) * 5 + j - 1][k] != 0:
                        isEmpty = False
                if isEmpty:
                    return True
    return False

def Sample(table, domainTable):
    while True:
        row = ChooseVariable(table, domainTable)[0]
        column = ChooseVariable(table, domainTable)[1]
        # Choose a random value and assign it to a free variable
        listRandomNumber = []
        for j in range(0, 9):
            if domainTable[(row - 1) * 5 + column - 1][j] != 0:
                listRandomNumber.append(domainTable[(row - 1) * 5 + column - 1][j])
        if len(listRandomNumber) != 0:
            table[row][column] = random.choice(listRandomNumber)
        UpadteDomainsTable(table, domainTable)
        if FindDomainEmpty(table, domainTable) or CheckInConsistent(table):
            return 1 + FindNumberVaribale(table)
        if FindNumberVaribale(table) == 0:
            return 0

# The Iterative Sampling algorithm simply consists in repeatedly calling Sample :
def IterativeSampling(table, domainTable):
    starttime = time.time()
    # Set the allocated time to 5 seconds
    while (5.0 - ((time.time() - starttime) % 60.0)) > 0:
        if Sample(table, domainTable) == 0:
            return True
    return False


#### ------------------------------------------------------------------------------------
#### Search Algorithms 3 : Meta Monte-Carlo search
#### A Meta Monte-Carlo Search tries all possible assignments of the variable, plays a sample after each assignment and choose the value that has the best sample score.
### ------------------------------------------------------------------------------------

def metaMonteCarlo(table, domainTable):
    bestScore = FindNumberVaribale(table)
    while True:
        row = ChooseVariable(table, domainTable)[0]
        column = ChooseVariable(table, domainTable)[1]
        bestSequence = [0]
        # for all values in the domain of var
        for j in range(0, 9):
            if domainTable[(row - 1) * 5 + column - 1][j] != 0:
                table[row][column] = domainTable[(row - 1) * 5 + column - 1][j]
                UpadteDomainsTable(table, domainTable)
                if FindDomainEmpty(table, domainTable) or CheckInConsistent(table):
                    score = FindNumberVaribale(table) + 1
                else:
                    score = Sample(table, domainTable)
                if score < bestScore:
                    bestScore = score
                    # Use a list to save the best sequence (variable, value)
                    bestSequence.append(j + 1)
        # assign the best value to variable
        table[row][column] = bestSequence.pop(len(bestSequence) - 1)
        UpadteDomainsTable(table, domainTable)
        if FindDomainEmpty(table, domainTable) or CheckInConsistent(table):
            return 1 + FindNumberVaribale(table)
        if FindNumberVaribale(table) == 0 or bestScore == 0:
            return 0

# The algorithm can be used with any maximum allocated time, repeatedly calling it until a solution is found or the time is elapsed
def iterativeMetaMonteCarlo(table, domainTable):
    starttime = time.time()
    # Set the allocated time to 5 seconds
    while (5.0 - ((time.time() - starttime) % 60.0)) > 0:
        if metaMonteCarlo(table, domainTable) == 0:
            return True
    return False


#### ------------------------------------------------------------------------------------
#### Search Algorithms 4 : Nested Monte-Carlo Search
#### Nested Monte-Carlo Search mainly consists in getting much information about the interestingness of all values before choosing one
#### ------------------------------------------------------------------------------------

def nested(level, table, domainTable):
    bestScore = FindNumberVaribale(table)
    while True:
        row = ChooseVariable(table, domainTable)[0]
        column = ChooseVariable(table, domainTable)[1]
        # for all values in the domain of var
        bestSequence = [0]
        for j in range(0, 9):
            if domainTable[(row - 1) * 5 + column - 1][j] != 0:
                table[row][column] = domainTable[(row - 1) * 5 + column - 1][j]
                UpadteDomainsTable(table, domainTable)
                if FindDomainEmpty(table, domainTable) or CheckInConsistent(table):
                    score = FindNumberVaribale(table) + 1
                elif level == 1:
                    score = Sample(table, domainTable)
                else:
                    score = nested(level - 1, table, domainTable)
                if score < bestScore:
                    bestScore = score
                    bestSequence.append(j + 1)
        # assign the best value to variable
        table[row][column] = bestSequence.pop(len(bestSequence) - 1)
        UpadteDomainsTable(table, domainTable)
        if FindDomainEmpty(table, domainTable) or CheckInConsistent(table):
            return 1 + FindNumberVaribale(table)
        if FindNumberVaribale(table) == 0 or bestScore == 0:
            return 0


# The algorithm can be used with any maximum allocated time, repeatedly calling it until a solution is found or the time is elapsed
def iterativeNestedMonteCarlo(level, table, domainTable):
    ShowTable(Kakuro)
    ShowTable(domainTable)
    print("Please wait for .......")
    starttime = time.time()
    # Set the allocated time to 5 seconds
    while (5.0 - ((time.time() - starttime) % 60.0)) > 0:
        if nested(level, table, domainTable) == 0:
            return True
    return False

# Test for the Nested Monte-Carlo Search
if iterativeNestedMonteCarlo(2, Kakuro, domainTableSize):
    print("Success : Nested Monte-Carlo search at level 2")
    ShowTable(Kakuro)
else:
    print("Failed : Nested Monte-Carlo search at level 2")
    ShowTable(Kakuro)



#### ---------------------------------------------------------------------------------------
####
#### In conclusion, we have compared Forward Checking, Iterative Sampling and Nested Monte-Carlo
#### Search on Kakuro problems.
#### Nested Monte-Carlo search at level 2 gives the best results.
####           24 25 20 26 24
####       18  1  7  5  3  2
####       26  4  5  3  8  6
####       28  5  6  7  2  8
####       26  8  4  1  6  7
####       21  6  3  4  7  1
####
#### ---------------------------------------------------------------------------------------