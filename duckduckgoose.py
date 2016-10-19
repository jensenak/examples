from random import randint
import time

class person():
    # This class property keeps track of how many person objects there are
    count = 0

    def __init__(self, name, age, fitness):
        # Wins and It will be used to keep track of stats
        self.wins = 0
        self.it = 0
        self.name = name
        # Speed is determined by age and fitness and ... weird adjustments
        self.speed = int(int(age)*(.8+int(fitness)/5))
        # Here we're incrementing the class property
        person.count += 1

    # The run method returns a random number, with a maximum of the person's speed
    # When two people run, the one with the faster return value wins
    def run(self):
       return randint(0, self.speed)

    # This is called every time someone either wins or becomes the goose
    def updateStats(self, winner):
        if winner:
            self.wins += 1
        else:
            self.it += 1

    # This just prints out the users statistics
    def getStats(self):
        return "{} was it {} times, and won {} times".format(self.name, self.it, self.wins)

#############################
# Get player info from user #
#############################
players = []
while True:
    name = input("Enter player name (empty to continue): ")
    if name == "":
        if len(players) < 3:
            print("You can't play duck duck goose with fewer than 3 people...")
            continue
        print("All players registered, moving to game play!")
        break
    age = input("What is this player's age: ")
    fit = input("1 = Active, 2 = Average, 3 = Sedentary; What is this player's fitness level? ")
    try:
        players.append(person(name, age, fit))
        print("Next!\n\n")
    except ValueError:
        if len(players) < 3:
            print("You can't play duck duck goose with fewer than 3 people...")
            continue
        print("All players registered, moving to game play!")
        break

rounds = int(input("How many rounds do you want to play? "))

###################
# Actual Gameplay #
###################

# Choose a random person to be the first goose
goose = randint(0, person.count-1)
# Calling updateStats with False is the way we say someone was "it"
players[goose].updateStats(False)

for r in range(rounds):
    print("\n==== {} is the goose ====".format(players[goose].name))
    # No one has been chosen
    newGoose = -1
    # Go around the circle until someone is chosen
    while newGoose < 0:
        # Touch each person on the head...
        for head in range(person.count):
            if head == goose:
                # Goose can't pick himself...
                continue
            # 10% chance the player will choose this person as goose
            if randint(1, 10) == 1:
                newGoose = head
                print("{}: GOOSE!".format(players[head].name))
                break
            print("{}: duck... ".format(players[head].name))

    # Find out how fast each person ran
    g = players[goose].run()
    n = players[newGoose].run()
    print("{} ran the circle in {} second(s); {} ran the circle in {} second(s)".format(players[goose].name, g, players[newGoose].name, n))
    # Whoever had a smaller run number wins
    if g > n:
        print(" --> {} wins".format(players[newGoose].name))
        players[newGoose].updateStats(True)
        players[goose].updateStats(False)
    else:
        print(" --> {} wins".format(players[goose].name))
        players[newGoose].updateStats(False)
        players[goose].updateStats(True)
        goose = newGoose

print("Final stats: ")
for p in players:
    print(p.getStats())
