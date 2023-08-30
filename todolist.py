import os

runProgram = True
todolist = []

#Funcion para mostrar las opciones del menu
def showMenuOptions():
    print("")
    print("")
    print("Por favor seleccione una opción:")
    print("")
    print("")
    print("1. Crear una tarea")
    print("2. Marcar como realizada una tarea")
    print("3. Borrar una tarea")
    print("4. Salir")

#Funcion para mostrar todas las tareas
def showTodoList():
    global todolist
    print()
    print()
    print("****************************************")
    for todo in todolist:
        print(f"{todolist.index(todo) + 1}. {todo}")
    print("****************************************")
    print()
    print()

#Funcion para guardar las tareas en la variable "todolist"
def createTodo():
    os.system("clear")
    global todolist
    print("Crear una nueva tarea")
    todo = input("Por favor ingrese el nombre de la tarea: ")
    todolist.append(todo)
    #Mostrar la lista de tareas
    showTodoList()

#Funcion para marcar una tarea como realizada
def updateTodo():
    global todolist
    print("Actualizar una tarea")
    todoId = int(input("Ingrese el número de la tarea que quiere marcar como hecha: "))
    todolist[todoId - 1] = todolist[todoId - 1] + "✅"
    showTodoList()

#Funcion que nos permite borrar una tarea
def deleteTodo():
    global todolist
    print("Borrar una tarea")
    todoId = int(input("Ingrese el número de la tarea que quiere borrar: "))
    del todolist[todoId - 1]
    showTodoList()

def main():
    global runProgram
    print(".: WELCOME TO A PYTHON TO DO LIST :.")
    flag = True

    while runProgram:
        while flag:
            showMenuOptions()
            option = int(input("Ingrese el número de la opción: "))

            match option:
                case 1:
                    createTodo()
                case 2:
                    updateTodo()
                case 3:
                    deleteTodo()
                case 4:
                    print("Hasta Luego!!!")
                    runProgram = False
                    flag = False
                case _:
                    print("Opción no reconocida. Ingrese una opción válida.")

if __name__ == "__main__":
    main()
