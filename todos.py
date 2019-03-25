import sys

dbFile = "db.dat"


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
        deleteInteractive()
    else:
        sys.stderr.write("Invalid argument")

def addTodo():
    if(len(sys.argv) < 4):
        sys.stderr.write("Must specify priority and todo")
    
    priority = sys.argv[2]
    todo = sys.argv[3]

    with open(dbFile, "a") as file:
        print(f"{priority};{todo}", file=file)


def listTodos(*, rev=False):
    with open(dbFile, "r") as file:
        todos = list(map(parseTodo, file.readlines()))
        todos.sort(key=lambda x: x[0], reverse=rev)
        for t in todos:
            print("%3d %s"%t)

def parseTodo(todo): 
    priority, text = todo.split(";")
    return int(priority), text[:-1]
    
def deleteInteractive():
    pass

if __name__ == "__main__":
    main()
