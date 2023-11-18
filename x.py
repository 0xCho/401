class Continent:
    def __init__(self, continent="North America"):
        self.continent = continent

    def __repr__(self):
        return f"Continent:{self.continent}"


class Location(Continent):
    def __init__(self, name="city, state"):
        super().__init__()
        try:
            self.city, self.state = name.split(", ")
        except ValueError:
            self.city = "unknown"
            self.state = "unknown"

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def __repr__(self):
        return f"Location: {self.city}, {self.state}"


class SportsTeam:
    def __init__(self, teamName, stadium, league, location):
        self.teamName = teamName
        self.stadium = stadium
        self.league = league
        self.location = location

    def getTeamName(self):
        return self.teamName

    def getStadium(self):
        return self.stadium

    def getLeague(self):
        return self.league

    def getLocation(self):
        return self.location

    def __repr__(self):
        return f"The {self.teamName} is a {self.league} team that plays at {self.stadium} in {self.location.getCity()}, {self.location.getState()}"


def queryList(team_list):
    while True:
        try:
            user_input = input("Enter a city or state (case sensitive): ")

            if user_input == 'quit' or user_input == 'exit':
                break

            found_teams = []
            for team in team_list:
                if user_input in team.getLocation().getCity() or user_input in team.getLocation().getState():
                    found_teams.append(team)

            if found_teams:
                print(f"{user_input} has these sports teams: ")
                for team in found_teams:
                    print(team)
            else:
                print(f"No sports teams were found in {user_input}")

        except Exception as e:
            print(f"Error: {e}")
            continue


def main():
    team_list = []
    try:
        aFile = open("sportsTeams.txt")
        lines = aFile.readlines()
        for line in lines:
            data = line.strip().split("\t")
            if len(data) >= 4:
                teamName = data[0]
                cityState = data[1].strip('"')
                stadium = data[2]
                league = data[3]

                location = Location(cityState)
                team = SportsTeam(teamName, stadium, league, location)
                team_list.append(team)

    except FileNotFoundError:
        print("File not found.")

    queryList(team_list)


main()
