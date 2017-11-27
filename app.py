# -*- coding: UTF-8 -*-

def select(names):
	print '> These are the names on the list: '
	for name in names:
		print '>> ' + name

def check(names):
	print '> Type the name you want to check if it is on the list: '
	name = raw_input()
	if name in names:
		print '>> Name is on the list'
	else:
		print '>> Name was not found on the list'

def insert(names):
	print '> Type the name you want to insert on the list: '
	name = raw_input()
	names.append(name)
	print '>> Name inserted'

def update(names):
	print '> Type the name you want to update on the list: '
	name = raw_input()
	if name in names:
		print '> Now, type the new name you want to insert on the list: '
		new_name = raw_input()
		position = names.index(name)
		names[position] = new_name
		print '>> Name updated'
	else:
		print '>> Name was not found on the list'

def delete(names):
	print '> Type the name you want to delete from the list: '
	name = raw_input()
	if name in names:
		names.remove(name)
		print '>> Name deleted'
	else:
		print '>> Name was not found on the list'

def menu():
	names = []
	option = ''
	while option != 'Q':
		print '> Press "S" to SELECT, "C" to CHECK, "I" to INSERT, "U" to UPDATE, "D" to DELETE and "Q" to QUIT'
		option = raw_input()
		if option == 'S':
			select(names)
		if option == 'C':
			check(names)
		if option == 'I':
			insert(names)
		if option == 'U':
			update(names)
		if option == 'D':
			delete(names)

menu()
