import sys

def main():
    if(len(sys.argv) < 2 ):
        sys.stderr.write("Must pass arguments")
    operation = sys.argv[1][1:]

    if(operation == 'a'):
        addTodo()
    elif(operation == 'l'):
        listTodos()
    elif(operation == 'r'):
        listTodos(rev=True)
    elif(operation == 'd'):
        interactiveMode()

def addTodo():
    pass

def listTodos(*, rev=False):
    pass

def interactiveMode():
    pass

if __name__ == "__main__":
    main()
