## Tic-tac-toe

- Tic-tac-toe (or noughts and crosses) is a simple strategy game in which two players take turns placing a mark on a 3x3 board, attempting to make a row, column, or diagonal of three with their mark.

- create a board, place markers on the board, evaluate if either player has won, and use this to simulate two basic strategies.

- Players 1 and 2 will take turns changing values of this array from a 0 to a 1 or 2, indicating the number of the player who places there.

- determine which positions are available to either player for placing their marker.
- select an available board position at random and place a marker there.
- place three pieces each on board for players 1 and 2.
- verify if either player has won the game. (row/column/diagonal)
- simulate an entire game.

- play 1,000 random games, and visualize how often either player wins, or how often the game is a draw.
- we see that when guessing at random, it's better to go first, as expected.
-  improve strategy. Player 1 always starts with the middle square.

### Library

- matplotlib.pyplot / time / random / numpy
