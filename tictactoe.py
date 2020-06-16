import math

board = ["-","-","-",
         "-","-","-",
         "-","-","-"] # Lista -> plansza

st_board = ['1','2','3',
            '4','5','6',
            '7','8','9'] # Pierwsza wyświetlana plansza w celu pokazania metody numerowania

checker = True # mówi czyja jest tura, True - tura X, False - tura O

is_over = False # mówi o tym, czy gra dalej trwa

winner = None # mówi kto wygrał

def dsp_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def placing(pos):
    global checker
    if board[pos] == "-":
        if checker == True:
            board[pos] = "X"
        else:
            board[pos] = "O"
        checker = not checker
    else:
        print("Pole zajęte, wybierz inne")

def tie():
    global is_over
    if '-' not in board:
        is_over = True
        return True
    else:
        return False

def win():
    global is_over
    global winner
    # Sprawdzam, czy wygrana jest w rzędach
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    # Jeżeli jest wygrana zmieniam flagę is_over
    if row1 or row2 or row3:
        is_over = True
        if row1:
            winner = board[0]
        elif row2:
            winner = board[3]
        elif row3:
            winner = board[6]
        else:
            winner = None

    # Sprawdzam, czy wygrana jest w kolumnach
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'

    if col1 or col2 or col3:
        is_over = True
        if col1:
            winner = board[0]
        elif col2:
            winner = board[1]
        elif col3:
            winner = board[2]
        else:
            winner = None

    # Sprawdzam, czy wygrana jest po przekątnej (tylko dwie opcje)

    cross1 = board[2] == board[4] == board[6] != '-'
    cross2 = board[0] == board[4] == board[8] != '-'

    if cross1 or cross2:
        is_over = True
        if cross1:
            winner = board[2]
        elif cross2:
            winner = board[0]
        else:
            winner = None



def game_state():
    win()
    tie()

def turn():
        if checker == True:
            print("Tura X")
        else:
            print("Tura O")
        pos = input("Wybierz pozycję od 1-9: ")
        pos = float(pos)
        if math.floor(pos) - pos != 0:
            print("Wprowadziłeś liczbę, która nie jest nautralna - wprowadź liczbę naturalną.")
            return None
        else:
            pos = int(pos) - 1
            if pos >= 0 and pos <= 8:
                placing(pos)
                dsp_board(board)
            else:
                print("Wprowadziłeś liczbę wiekszą niż 9 lub mniejszą niż 1")

def run_game():

    # Wyświetlenie planszy
    dsp_board(st_board)
    while not is_over:
        # obsługa tury
        turn()

        # Sprawdzanie stanu gry

        game_state()
    # Game Over - sprawdzam kto wygrał lub czy jest remis
    if winner != None:
        print("Wygrywa " + winner)
    elif winner == None:
        print("Remis!")

# Uruchamiam grę

run_game()


