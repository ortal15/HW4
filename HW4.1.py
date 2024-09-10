# START
pizza_triangles: int = int(input("How much pizza did Danny's mother bring ?"))
amount: int = pizza_triangles // 4
leftovers: int = pizza_triangles % 4
if leftovers > 0:
    print(f'4 friends got {amount} pizza triangles , and stayed {leftovers} leftovers ')
else:
    print(f'Each member received an equal number of {amount} pizzas')
# END

# START
friends: int = int(input('How many friends came?'))
pizza: int = int(input("How many pizza triangles were ordered? ?"))
amountt: int = pizza // friends
leftoverss: int = pizza % friends
if leftovers > 0:
    print(f'{friends} friends got {amountt} pizza triangles , and stayed {leftoverss} leftovers ')
else:
    print(f'Each member received an equal number of {amountt} pizzas')
# END
