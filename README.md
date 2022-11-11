# Battleships
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Battleships is a termina based application allowing the user to play Battleships game against one computer opponent,

Live version is available at this link [https://ci-igor-battleships.herokuapp.com/](https://ci-igor-battleships.herokuapp.com/)

## Instructions how to play

When you start the game the applications first asks you for a setup information: the size of the board and the number of ships for each board.

![Game Setup](/assets/images/game-setup.png "Game setup")

After that a first round of game starts and repeats untill there are no ships left on one of the boards. Instructions how to play and current score are displayed at the begining of each round and at the end of it the user is aked to either continue to play or quit the game.

![Game Round](/assets/images/game_progress.png "Game round")
![Round Outcome](/assets/images/game_round_outcome.png "Round outcome")

This continues until there are no ships left on one or both boards. At this stage a game result is displayed and user may decide to continue with a new game or quit.

![Game Result](/assets/images/game_outcome.png "Game result")

## Features

### Implemented
The following features wer eimplemented:
* Game setup to set game settings: game board size and number of ships
* Random placement of ships on boards
* Opponents move
* Dsiplaying score and game instructions at the begining of every round
* Input of coordinates in form of 2 numbers separated by comma and in more natural range starting at 1 instead of 0
* Validation of user input against numbers out of range or not numbers
* Checking if the new user coordinates were already targeted
* In case of wrong data input instructions are given what was wrong


![Coordinates Validation](/assets/images/game_coordinates_validation.png "Input validation")

### To Do

* Change display mode from line input / terminal mode to ncurses

## Coding

The game is designed around a Board class which handles playing board data and fucntctionality. Both instance and class data is employed depending on needs.

The methods implemented deliver following functions:
* initialization of a instance board and filling it with empty cells
* returning a single line of a board as a string
* checking if a cell on a board is free/empty
* filling a board with randomly positioned ships

The playing board itself is implemented as a 2-dimensional list holding Unicode numbers representing objects on the board

## Testing

1. I used pylint to validate the code and achieved score of 10.0

![plint output](/assets/images/pylint_result.png "pylint output")

2. I checked if input validation functions react properly on user mistakes:
* entering number out of range
* entering a input which is not a number
* entering different input than two numbers separated by comma
3. I verified that the application output is readable and displays properly in gitpod terminal, the Heroku's one and in terminal of the local machine.

## Bugs
In early stage I noticed that users were asked to enter a number in a range 1 to *board size* while the index of a list starts at 0 to *board size*. I decided to keep this range (starting 1) as I find it more natural and modify the code instead of enforcing 0 as a starting number.

## Deployment

1. Log in to Heroku and proceed to dashboard
2. Select to create new app and give it a name and select region, press **Create app** button
3. In the Settings tab in the Config vars click **Reveal Config vars** and add a key *PORT* and value *8000*
4. In the buildpacks section add the following packs: *heroku/python* and *heroku/nodejs* in this order
5. Go to the **Deployment** tab go to **Deployment method** section and select **Github**. Connect to you github account if asked
6. Search for the repository containing this app and connect to it
7. Either using **Automatic deploys** or **Manual deploy** select the branch (main) and press **Deploy Branch** button


## Credits

C.I. gitpod template for Heroku app deployments