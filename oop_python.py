class player:

    def __init__(self,name,team):
        self.name = name
        self.team = team

                
    def getPlayerName(self):
        return self.name

    def getTeam(self):
        return self.team



def main():
    name = input("name : ")
    team = input("team : ")
    p1 = player(name,team)

    name = input("name : ")
    team = input("team : ")
    p2 = player(name,team)

    name1 = p1.getPlayerName()
    team1 = p1.getTeam()
    print(f"{name1} is from {team1}")

    name2 = p2.getPlayerName()
    team3 = p2.getTeam()
    print(f"{name2} is from {team3}")


if __name__ == '__main__':
    main()

