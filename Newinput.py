# name = input('what is your name')
# age = input('your age')
# print('welcome '+ name+' and your age is '+ age)


# num1 = input('enter the first no: ')
# num2 = input('enter the second no: ')
# result = int(num1)+int(num2)
# print(result)


# to solve decimal numbers
#
# num1 = input('enter the first no: ')
# num2 = input('enter the second no: ')
# result = float(num1)+float(num2)
# print(result)

# color = input('enter your color: ')
# noun_plural = input('enter your plural noun: ')
# adjective = input('enter your adjective: ')
#
# print('tree are '+color)
# print(noun_plural+' are mean')
# print('please keep it '+adjective)


# name = input('enter new name')
# prounun = input('enter new prnoun')
# adjective = input('enter new adjective')
#
# print('while '+name+' was reading '+prounun+' book')
# print(prounun+' mom told her to clean '+prounun+' room')
# print(name+' was '+adjective+' guy and '+adjective)
# print(name+' want to be football player but '+prounun+' dad did not want')
# print(name+' was sad cuz '+prounun+' dad did not helped '+prounun)


#many types of info in one place

#[] this squaers tells python that im list

# friends = [1, 'ahmed ali', 2.2 , True, False]
# print(friends)
# print(friends[1])
# print(friends[2])

# friends = ['saad', 'ahmed', 'hasan', 'hosni']

# print(friends)
# print(friends[-1])
# print(friends[-2])
# print(friends[1:3]) # here the programme say no add factor 3 hosni
#
# print(friends[0:2])
# # to start count from specif unit until the end
# print(friends[1:])
# friends[1] = 'coco' # to change value inside the list
# print(friends[1])
# print(friends)



# codezilla = ['programming', 'python', 'tutorial', 'html', 'css']
# tutorial = ['extend', 'list1', 'codezilla']
# print(codezilla, tutorial)

# to print them together add list to another list
# codezilla += tutorial
# print(codezilla)
# codezilla = codezilla + tutorial
# print(codezilla)

# to add agent to the list
# codezilla.append('ali')
# print(codezilla)
# codezilla.append([1, 2, 'ahmed'])
# print(codezilla)



# to detect exactly where you would like to add new agent to the list

# codezilla.insert(0, 'hasan')
# print(codezilla)
# codezilla.remove('python')
# print(codezilla)
# codezilla.clear() # to remove everything inside the list
# print(codezilla)
# codezilla.pop()
# print(codezilla)
# codezilla.pop()
# print(codezilla)
# what_was_popped = codezilla.pop()
# print(what_was_popped)
# # to remove just last agent in the list we use codezilla.pop()
#
# print(codezilla.index('python')) # to detect if the agent that we want in the list or not


# data = codezilla.index('tutorial')
# print(data)

# to check about one agent if is it in the list or not and how many time repeated we use
# print(codezilla.count('python'))

# to sort and rearrange the words in the list depening on alphabet
# we use
# codezilla.sort()
# print(codezilla)



# arrage the number from smallest to  the biggest
# ahmed = [1, 455, 86, 45, 10]
# ahmed.sort()
# print(ahmed)

# if you want to make copy for our list
# list_new = ahmed.copy()
# print(list_new)
#the new list will not change with any addtion to the original list

#this way to add changes the new list and old list together
# list_new1 = ahmed
# ahmed.append(1)
# print(list_new1)
# print(ahmed)


#tuples
#() for using tuples
# we put two values or more  inside the tuples
# in tuples we can not change anything in it
#after we made it we can not add or remove anthing
#from it
coordinate = (23, 25)
print(coordinate)
print(coordinate[1])

# we use tuples for information which do not accpet
#any changes after doing it like coordinates
# and the positions of the places

# we can make list of tuples and it will be
# the same like nomral tuples we can change or add anthing on it
# let us see example
#[()] like this list and inside the list tuples
list_of_tuples = [(2,3), (5, 6), (85, 47)]
print(list_of_tuples)

# list_of_tuples [0] [0] mean change value
#in 0 as arragne to 0 value and it will appear
#that we can not change or add anything











