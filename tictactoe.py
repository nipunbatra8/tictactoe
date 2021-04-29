print('Welcome to Tic-Tac-Toe!')

l1 = list('     |     |     ')
l2 = list('     |     |     ')
l3 = list('_____|_____|_____')
l4 = list('     |     |     ')
l5 = list('     |     |     ')
l6 = list('_____|_____|_____')
l7 = list('     |     |     ')
l8 = list('     |     |     ')
l9 = list('     |     |     ')

# print(l1)

def draw_board():
    print(' %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s' %
          (''.join(l1), ''.join(l2), ''.join(l3), ''.join(l4), ''.join(l5), ''.join(l6), ''.join(l7), ''.join(l8), ''.join(l9)))

def which_quadrant(count):
    if count == 1:
        which_quadrant.player = 1
        which_quadrant.quad = input('Player 1 (X), Choose quadrant 1-9: ')
        while True:
            try:
                which_quadrant.quad = int(which_quadrant.quad)
                if (which_quadrant.quad >= 1 and which_quadrant.quad <= 9):
                    break
                else:
                    print('Not a number between 1-9')
            except ValueError:
                print('Not a number')
    else:
        while True:
            if which_quadrant.player == 1:
                which_quadrant.quad = input('Player 1 (X), Choose quadrant 1-9: ')
            if which_quadrant.player == 2:
                which_quadrant.quad = input('Player 2 (O), Choose quadrant 1-9: ')
            try:
                which_quadrant.quad = int(which_quadrant.quad)
                if (which_quadrant.quad >= 1 and which_quadrant.quad <= 9):
                    break
                else:
                    print('Not a number between 1-9')
            except ValueError:
                print('Not a number')

# intro
draw_board()
count = 1
which_quadrant(count)
count += 1
# print(which_quadrant.quad)

while True:
    if which_quadrant.player == 1:
        if which_quadrant.quad == 1:
            l2[2] = 'X'
            draw_board()
        elif which_quadrant.quad == 2:
            l2[8] = 'X'
            draw_board()
        elif which_quadrant.quad == 3:
            l2[14] = 'X'
            draw_board()
        elif which_quadrant.quad == 4:
            l5[2] = 'X'
            draw_board()
        elif which_quadrant.quad == 5:
            l5[8] = 'X'
            draw_board()
        elif which_quadrant.quad == 6:
            l5[14] = 'X'
            draw_board()
        elif which_quadrant.quad == 7:
            l8[2] = 'X'
            draw_board()
        elif which_quadrant.quad == 8:
            l8[8] = 'X'
            draw_board()
        elif which_quadrant.quad == 9:
            l8[14] = 'X'
            draw_board()
        which_quadrant.player = 2
        which_quadrant(count)
    elif which_quadrant.player == 2:
        if which_quadrant.quad == 1:
            l2[2] = 'O'
            draw_board()
        elif which_quadrant.quad == 2:
            l2[8] = 'O'
            draw_board()
        elif which_quadrant.quad == 3:
            l2[14] = 'O'
            draw_board()
        elif which_quadrant.quad == 4:
            l5[2] = 'O'
            draw_board()
        elif which_quadrant.quad == 5:
            l5[8] = 'O'
            draw_board()
        elif which_quadrant.quad == 6:
            l5[14] = 'O'
            draw_board()
        elif which_quadrant.quad == 7:
            l8[2] = 'O'
            draw_board()
        elif which_quadrant.quad == 8:
            l8[8] = 'O'
            draw_board()
        elif which_quadrant.quad == 9:
            l8[14] = 'O'
            draw_board()
        which_quadrant.player = 1
        which_quadrant(count)