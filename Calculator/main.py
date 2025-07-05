history_file = "history.txt"

def show_history():
    file = open(history_file, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No such History")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(history_file, 'w')
    file.close()
    print("History has been clear")

def save_to_history(equation, result):
    file = open(history_file, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close() 

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print('Invalid Input. Use format: number operator number(e.g 5 + 5 )')
        return
    
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result =  num1 * num2
    elif operator == "/":
        if num2 == 0:
            print('Cannot devide by zero')
            return
        result =  num1 / num2
    else:
        print('Invalid operator. Use only + - * / ')
        return 
    if int(result) == result:
        result = int(result)
    
    print("Result: ", result)
    save_to_history(user_input, result)

def main():
    print('----CALCULATOR----')
    while True:
        user_input = input("Enter calculation (+ - * /) or command prompt (history, clear, exit)")
        if user_input == 'exit':
            print('Thank You for using this Calculator❤️')
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()


