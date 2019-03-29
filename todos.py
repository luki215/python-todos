# Thanks for submitting the homework! I've found some minor issues (mostly
# Python-unrelated nitpicks). Fixing those would make the code better for others.
# (You don't need to fix it, it's just feedback for you to know what (not) to do).
#
# Overall, I like your solution for being simple and easy to follow. That's
# a very important, yet very underestimated quality in software these days.

# Always good to add the interpreter/hash-bang line: #!/usr/bin/env python3
import sys

dbFile = "db.dat"


def main():
    if(len(sys.argv) < 2 ):
        # Nitpick: a better error message would be a usage message in
        # the Unix tradition. Also, be careful with sys.stderr.write as
        # it does not append \n to the output by default (like printf does);
        # better to print(..., file=sys.stderr) IMO.
        sys.stderr.write("Must pass arguments")
        # You probably want to sys.exit here with a non-zero exit code.
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
        # Either usage message or a descriptive message should be given here.
        # Something like:
        #
        # me = os.path.basename(sys.argv[0])
        # f"{me}: unknown option: #{operation}"
        sys.stderr.write("Invalid argument")
        # And you want to exit here with a non-zero exit code, too.

def addTodo():
    # Nitpick: better to test for equality (as in len(sys.argv) == 4); this will
    # allow extra arguments to be passed and it can get confusing for the user.
    if(len(sys.argv) < 4):
        sys.stderr.write("Must specify priority and todo")
        # return (also everywhere below)

    # int(...) conversion would be cool! Otherwise, you risk writing something
    # that's not an int into the file, and you won't be able to ever load it
    # again. So the database will be corrupted from the user's POV.
    priority = sys.argv[2]
    todo = sys.argv[3]

    with open(dbFile, "a") as file:
        print(f"{priority};{todo}", file=file)


# Hmmm... Why the *?
def listTodos(*, rev=False):
    with open(dbFile, "r") as file:
        todos = [parseTodo(todo) for todo in file.readlines()] # Nice!
        todos.sort(key=lambda x: x[0], reverse=rev)
        for t in todos:
            # I would personally refrain from the interpolation operator;
            # feels like a P2 heritage. Much better to use f"strings" IMO.
            print("%3d %s"%t)

def parseTodo(todo): 
    priority, text = todo.split(";")
    # Stripping the new-line this way is a bad idea. If the last line of the
    # file does not end in \n, your app will break :(. Try with:
    #
    #   % echo -ne "1;a\n2;b" > db.dat
    #   % python3 todos.py -l
    #
    # Better to always use strip :).
    return int(priority), text[:-1]

def deleteInteractive():
    pass

if __name__ == "__main__":
    main()
