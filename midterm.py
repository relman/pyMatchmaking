def matchmaking(players, teams=3, min_team=1, max_team=None):
    """
    Dynamically builds teams of players for online multiplayer.
    Filter out players with bad connections and produce the lists of players,
    segregated into appropriate teams.

    :param players: a list of tuples of usernames and connection strengths
    :param teams: the number of teams to build
    :param min_team: the minimum number of players per team
    :param max_team: the maximum number of players per team
    """
    filtered = [x for x in players if x[1]]
    if len(filtered) < min_team * teams:
        return False

    total = calc_total(filtered, teams, max_team)

    game = [[] for i in xrange(teams)]
    for i in xrange(total):
        game[i % teams].append(filtered[i][0])
    return game


def calc_total(players, teams, max_team):
    """
    Calculates total amount of players.

    :param players: a list of tuples of usernames and connection strengths
    :param teams: the number of teams to build
    :param max_team: the maximum number of players per team
    :return:
    """
    total = min(len(players)/teams * teams, teams * max_team) \
        if max_team is not None \
        else len(players)/teams * teams
    return total


if __name__ == '__main__':
    print 'dynamically builds teams of players for online multiplayer'
