HISTORY_FILE = "History.txt"
def show_history():
    file = open(HISTORY_FILE,'r')
    lines= file.readlines()
    if len(lines)==0:
        print("no history found")
    else:
        for line in reversed(lines):
            print(line.sprip())
    file.close()
def clear_history():
    file = open(HISTORY_FILE , 'w') 
    file.close()
    print('history is cleared')

def save_to_history(equation , result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + '=' +str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalis input , Use format : number operation number (e.g - 8 + 8)")
        return 

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+" :
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2 
    elif op == "/":
        if num2 == 0:
            print("cannot divide by zero ,0 ")
            return
        result = num1 / num2
    else:
        print ("invalid operation , use only '+" , '-' , '*' , '/')
        return

    if int(result)==result:
        result = int(result)
    print ("result : " ,result)
    
    save_to_history(user_input , result)

def main ():
    print ("Simple calculator -- type history , clear or exist ")
    while True:
        user_input = input("Enter calculation , + - * /  or command (history , clear_history  , exist) ")
        if user_input == exit:
            print ("good-byy")
            break 
        elif user_input ==' history' : 
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()
