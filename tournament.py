 
# tournament.py -- implementation of a Swiss-system tournament

import bleach
import psycopg2


def connect():
    """Connects to the postgreSQL database and returns the connection object"""
    return psycopg2.connect("dbname=tournament")


def db_simple_operation(query, param=False):  
    """Performs the query against the database.

    Args:
      query: the query to perform agains the database
      param: the cleaned input to insert into the database
    """
    conn = connect()
    c = conn.cursor()
    c.execute(query, param)
    conn.commit()
    conn.close()


def db_return_operation(query, param=False):
    """Performs the query against the database and returns the result.

    Args:
      query: the query to perform agains the database
      param: the cleaned input to insert into the database

    Returns:
      Returns the list resulting from running the query
    """
    conn = connect()
    c = conn.cursor()
    c.execute(query, param)
    resultset = c.fetchall()
    conn.commit()
    conn.close()
    return resultset


def deleteMatches():
    """Removes all the match records from the database."""
    db_simple_operation("DELETE FROM matches;")


def deletePlayers():
    """Removes all the player records from the database."""
    db_simple_operation("DELETE FROM players;")


def countPlayers():
    """Returns the number of players currently registered."""
    [(num_of_players, )] = db_return_operation("SELECT count(*) FROM players;")
    return num_of_players


def registerPlayer(name_of_player):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.
  
    Args:
      name: the player's full name (need not be unique).
    """
    clean_name = bleach.clean(name_of_player)
    query = "INSERT INTO players (name) VALUES (%s);"
    db_simple_operation(query, (clean_name, ))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list is the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    playerStandings = db_return_operation("SELECT * FROM standings")
    return playerStandings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db_simple_operation("INSERT INTO matches (winner, loser) \
                          VALUES (%d, %d)" % (winner, loser))
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
   
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings. Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """