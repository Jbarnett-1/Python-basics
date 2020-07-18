bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # list only first bicycle

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title()) # capitalize first bicycle 

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1]) # access the last item of a list

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# modifying elements 
colors = ['red', 'orange', 'yellow']
print (colors)

colors[0] = 'green'
print (colors)

# append to end of a list
colors.append('blue')
print(colors)

popped_colors = colors.pop() #removal of last entry and assigned poppd variable
print(colors)
print(popped_colors)

colors = ['red', 'orange', 'yellow']

last_colors = colors.pop()
print(f"The last color on the list is {last_colors.title()}.")

colors = ['red', 'orange', 'yellow']
print(colors)

colors.remove('yellow')
print(colors)

foods = ['pasta', 'burgers', 'fries'] # alphabetically sorts
foods.sort()
print(foods)
