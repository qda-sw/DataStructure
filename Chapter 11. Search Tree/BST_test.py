from BST import BST
bst = BST()
while True:
    command = input().split()
    if command[0] == 'get':
        result = bst.get(int(command[1]))
        print(result.value) if result else print("None")
    elif command[0] == 'put':
        result = bst.put(*map(int, command[1:]))
    elif command[0] == 'delete':
        bst.delete(int(command[1]))
    elif command[0] == 'print':
        bst.print()
    elif command[0] == 'quit':
        exit()