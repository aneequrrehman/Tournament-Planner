-- Table definitions for the tournament project.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Connect to the tournament database
\c tournament

-- Create table 'players'
CREATE TABLE players ( id SERIAL PRIMARY KEY,
					   name TEXT );

-- Create table 'matches'
CREATE TABLE matches ( id SERIAL PRIMARY KEY,
					   winner INTEGER REFERENCES players (id),
					   loser INTEGER REFERENCES players (id) );


-- View to calculate number of wins of each player
CREATE VIEW win_total AS 
	SELECT id, name, (SELECT count(*) FROM matches
		WHERE players.id=matches.winner) AS wins
	FROM players;

-- View to calculate number of losses of each player
CREATE VIEW loss_total AS
	SELECT id, name, (SELECT count(*) FROM matches
		WHERE players.id=matches.loser) AS losses
	FROM players;

-- View to calculate total number of matches played by each player
CREATE VIEW match_total AS
	SELECT id, name, (SELECT count(*) FROM matches
		WHERE players.id IN (matches.winner, matches.loser)) AS matches
	FROM players;

-- View to show standings of the players
CREATE VIEW standings AS
	SELECT match_total.id, match_total.name, wins, matches
	FROM match_total JOIN win_total ON match_total.id=win_total.id
	ORDER BY wins DESC;