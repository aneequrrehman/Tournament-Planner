# Tournament-Planner
This project is created to host a non-elimination Swiss-style tournament 
where players are only matched against the players with almost the same
number of wins. The database schema to store the game matches between players,
and the code to query this data, plan the matches between players and determine
the rankings of the players is presented here.

# Tournament Planner Database Project for Udacity Full Stack Nano Degree Program


FILES INCLUDED
--------------

	- tournament.py
	- tournament.sql
	- tournament_test.py
	- pg_config.sh
	- Vagrantfile


REQUIREMENTS
------------

	This program is developed in Python 2.7, psycopg2 v2.6.1, and PostgreSQL
	database v9.3.10 is used. Virtual machines should be setup to run the 
	project files. For development and testing purposes, Git Bash v1.9.5 Shell,
	vagrant v1.7.4, Oracle VM VirtualBox v5.0.0 were used.


SPECIFICATIONS
--------------
	
	- Players can be registered in or deleted from the database.
	- The matches played by the players can be stored or deleted.
	- The rankings of the players can be viewed based on their wins and losses.
	- The swiss-style pairings of the players can be generated to plan matches
	between players so that each player goes agains the player with almost the
	same number of wins


HOW TO USE
----------

	- Git Bash the project files directly and type this command to run the 
	virtual machine
		vagrant up

	- Then type the following command to log into your virtual machine
		vagrant ssh

	- The shared directry will be located at /vagrant. Use the following 
	command to change directry to the shared folder
		cd /vagrant

	- Run this command to run PostgreSQL database
		psql

	- To create the database with the schema defined in tournament.sql, type
	the following command
		\i tournament.sql

	- If you run the above steps for the second time, it may generate an error
	stating that database named "tournament" already exists. In that case, you
	may want to drop the previous database using this SQL statement:
		DROP DATABASE IF EXISTS tournament;

	- The database is now created with the schema defined. It can now be used.


TOOLS USED
----------

	- Official Python editor IDLE was used for the development.
	- Sublime Text Editor was extensively used for the "tournament.sql"
	- Oracle VM VirtualBox v5.0.0 was installed for virtual machines.
	- vagrant v1.7.4 software was used to create or remove VMs.
	- Git Bash v1.9.5 was used as shell to run vagrant and configure VMs.


DEVELOPER's NOTES
-----------------

	"Vagrantfile" contains the configuration of VM. The ports or other 
	VM settings can be changed in this file.

	"pg_config.sh" contains all the necessary python modules for the 
	remaining .py files. Additional modules can be installed, if needed.

	"tournament.sql" contains the database schema of the tournament planner.
	It can be changed to add more features e.g. support multiple tournaments.

	"tournament.py" contains the python code to interact with the database. 
	All the functions are implemented in this file. No front-end of the project
	is created. The functions defined in this project can be used if fornt-end
	of the project is created.

	"tournament_test.py" contains all the unit tests for the "tournament.py" file.
	If new features are added then the tests for those features can be written in
	this file.

	If you want to improve, feel free to go ahead.


CREDITS
-------

	Credits are given to:

	- "Udacity" for teaching the core concepts
	- "python.org" community for the concise documentation they have provided
	- "StackOverflow.com" community for their continuous support
	- Official postgreSQL documentation has helped a lot


CONTACT
-------

	If you have any suggestions, the contact description is given below:

	Name:		ANEEQ-UR-REHMAN
	Email:		aneeqnazir@gmail.com
	Country:	Pakistan

