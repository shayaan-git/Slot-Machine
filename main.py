import random # creating a module

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}    # symbol are letters and the symbol_count are numbers

symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}    # at 38:00 

def check_winnings(columns, lines, bet, values):    # at 40:00 
    winnings = 0
    winning_lines = []
    for line in range(lines):   # looping through every rows
        symbol = columns[0][line]   # symbol check i.e. whatever the symbol is in the first column of the current row, because all of the symbols need to be the same.
        for column in columns:  # now we loop through every single column and check for that symbol
            symbol_to_check = column[line]  # so we go to each column and we say the symbol to check is = to the column at the current row that we are looking at
            if symbol != symbol_to_check: # if symbols are not the same then we break out then we now check the next line coz we didn't win
                break
        else:   #if the symbols are same then we won and next code executes
            winnigs += values[symbol] * bet #this bet is 'bet on each line' not the' total bet'
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []    #creating a symbol named list
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):   # The _ symbol at 25 minute
            all_symbols.append(symbol)

    columns = []    #Defining our column list
    for _ in range(cols): #generating a column for every single column, So if we have 3 columns then we need verything inside is 3 times
        column = []
        current_symbols = all_symbols[:]    # this ':' represents slice means current symbols are copy of all symbols
        for _ in range(rows): #looping through no. of values which is equal to no. of rows we have in our slot machine
            value = random.choice(current_symbols) #picks a value which is random choice from the current symbol
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):    # at 32:00
    for row in range(len(columns[0])): 
        for i, column in enumerate (columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")   # at 36:00
            else:
                print(column[row], end="")
            
        print()

def deposit ():    #creating a function
    while True:
        amount = input("What amount would You like to Deposit?\n$: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

#Collecting the bet from the user
#How much they wanna bet
#How many lines they wanna bet on
#Then multiply the bet amount with no. of lines

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?\n: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please Enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What would You like to bet on each line?\n$: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}...") #2nd way of putting variables in our string
# This is a way to embed values inside of strings. The 'f' is written before string and inside curly braces variables are written.
# Then it will automatically be converted to a string by Python if, it can be
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
                print(f"You do not have enough to bet that amount.\nYour current balance is: ${balance}")
        else:
            break
        
        print(f"You are betting ${bet} on {lines} lines.\nTotal bet amount is equal to: ${total_bet}")

    # print(balance, lines)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count) #slots here are actually column #
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main(): # Our program now is into this main function
    print ("\n")
    print("      *** HALAL SLOT MACHINE ***     ")
    print ("\n")
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press Enter to Spin (q to Quit).")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")

# calling the main function so that we start running main and do everything inside of it if wanted to try again.

main()