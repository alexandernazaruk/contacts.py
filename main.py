import pickle
import os
'''This program is designed for storing, creating, editing, deleting, searhcing contacts.'''

#Basic pickling of data
def get_data(file):
  '''Get addresses from file'''
  #Opening file for reading in binary mode, and handling possible issues
  try:
    f = open(file, 'rb')
    addresses = pickle.load(f)
  except IOError:
    print('No such file!')
  finally:
    if f:
      f.close()
  return addresses
def write_data(file, addresses):
  '''Write addresses to file'''
  #Opening file for writing in binary mode, and handling possible issues
  try:
    f = open(file, 'wb')
    addresses = pickle.dump(addresses, f)
  except IOError:
    print('No such file!')
  finally:
    if f:
      f.close()

#Manipulating existing data
def edit_contact(file, addresses):
  '''Edit contact from file'''
  select = input('Contact name (q-back): ')
  if select == 'q':
    return
  elif select in addresses:
    #Editing contact. Using OR set default values
    print(f'Editing \'{select}\'. Details: {addresses[select]}')
    email = input('Email: ') or addresses[select][0]
    phone = input('Phone: ') or addresses[select][1]
    addresses[select] = [email, phone]
    write_data(file, addresses)
  else:
    print('Unknown contact')
def delete_contact(file, addresses):
  '''Delete contact from file'''
  select = input('Contact name (q-back): ')
  if select == 'q':
    return
  elif select in addresses:
    print(f'Delete \'{select}\'. Details: {addresses[select]}')
    del addresses[select]
    write_data(file, addresses)
  else:
    print('Unknown contact')
def search_contacts(addresses):
  '''Search for contacts in addresses'''
  select = input('Search (q-back): ')
  for item, value in addresses.items():
    if item == select:
      print(f'{item} \t {value[0]} \t {value[1]}')
  if select == 'q':
    return

#Main functions
def browse_contacts():
  addresses = get_data('addressbook.txt')
  print()
  for item, value in addresses.items():
    print(f'{item} \t {value[0]} \t {value[1]}')
  while True:
    print()
    select = input('e-edit, d-delete, s-search, q-main: ')
    if select == 'e':
      edit_contact('addressbook.txt', addresses)
    elif select == 'd':
      delete_contact('addressbook.txt', addresses)
    elif select == 's':
      search_contacts(addresses)
    elif select == 'q':
      break
    else:
      print('Unknown menu item')
def add_contact():
  addresses = get_data('addressbook.txt')
  name = input('Enter name: ')
  email = input('Enter email: ')
  phone = input('Enter phone: ')
  addresses[name] = [email, phone]
  write_data('addressbook.txt', addresses)

print('Hello! This is your contact book app.')
while True:
  print('\nMain menu:\n0 - Browse contacts\n1 - Add contact\ne - Exit')
  select = input('Select action: ')
  if select == '0':
    browse_contacts()
  elif select == '1':
    add_contact()
  elif select == 'e':
    os._exit(1)
  else:
    print('Unknown menu item')