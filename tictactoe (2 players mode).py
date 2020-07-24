#%%
# This is for 2 human players

class TicTacToe:
    def __init__(self, names):
        self.board = [[' ',' ',' '] for i in range(3)]

        player_name = names.split(',')
        self.name1 = player_name[0]
        self.name2 = player_name[1]
        self.player = 'X'

    def play(self):
        print(self.name1 + ' will play with \'X\' and ' + self.name2 + ' will play with \'O\'')
        while self.has_turn():
            pass
        regame = input('Would you like to play again? (press \'y\' if yes): ')
        if regame == 'y':
            self.board = [[' ',' ',' '] for i in range(3)]
            self.play()
        print('---------Game Over---------')

    def display(self):
        print('==========================')
        print('1 | 2 | 3       '+ ' | '.join(self.board[0]))
        print('----------      ----------')
        print('4 | 5 | 6  ==>  '+' | '.join(self.board[1]))
        print('----------      ----------')
        print('7 | 8 | 9       '+' | '.join(self.board[2]))
        print('==========================')

    def has_turn(self):
        self.display()
        coordinate = self.get_input()
        while coordinate == False:
            print("Please enter a valid number between 1 - 9, and choose an empty space.")
            coordinate = self.get_input()
        x, y = coordinate[0], coordinate[1]
        self.board[x][y] = self.player
        if self.has_winner() == 'WIN':
            self.win_message()
            return False
        elif self.has_winner() == 'DRAW':
            print('Draw!!')
            return False

        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
        return True

    def has_winner(self):
        win_combi = [
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
            
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],

            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
        ]
        if [self.player, self.player, self.player] in win_combi:
            return 'WIN'
        if self.is_blank():
            return ''
        else:
            return 'DRAW'
        
    def is_blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return True
        return False
    
    def win_message(self):
        if self.player == 'X':
            print("Congrats, " + self.name1 + ". You won!")
        else:
            print("Congrats, " + self.name2 + ". You won!")

    def get_input(self):
        try:
            if self.player == 'X':
                input_values = int(input(self.name1 + ', please choose a space between 1 - 9: '))
            else:
                input_values = int(input(self.name2 + ', please choose a space between 1 - 9: '))

            if input_values == 1:
                return [0, 0] if self.board[0][0] == ' ' else False
            elif input_values == 2:
                return [0, 1] if self.board[0][1] == ' ' else False
            elif input_values == 3:
                return [0, 2] if self.board[0][2] == ' ' else False
            elif input_values == 4:
                return [1, 0] if self.board[1][0] == ' ' else False
            elif input_values == 5:
                return [1, 1] if self.board[1][1] == ' ' else False
            elif input_values == 6:
                return [1, 2] if self.board[1][2] == ' ' else False
            elif input_values == 7:
                return [2, 0] if self.board[2][0] == ' ' else False
            elif input_values == 8:
                return [2, 1] if self.board[2][1] == ' ' else False
            elif input_values == 9:
                return [2, 2] if self.board[2][2] == ' ' else False
            else:
                return False
        except:
            return False

if __name__ == '__main__':
    names = input('Enter player names (e.g., Jino,Tom): ')
    game = TicTacToe(names)
    game.play()

# %%
