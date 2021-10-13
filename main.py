import os.path
import json


def verify_user_file():
    user_file_exists = os.path.isfile('users.json')
    if user_file_exists:
        print('User database has been verified.')
    else:
        user_file = open('users.json', 'w')
        user_file.write('{"users": []}')
        user_file.close()
        print('User database has been created.')


def load_user_file():
    with open('users.json') as user_file:
        return json.load(user_file)


def login():
    username = input('Please enter usernname to login: ')
    return username


def verify_existance(username):
    if username in loaded_users_dict['users']:
        print('User found in user database.')
        return
    else:
        opt_create_user = input('User does not exists. Would you like to add {} as a new user? (y/n): '.format(username))
        if opt_create_user.upper() == 'Y':
            add_user(username)
        elif opt_create_user.upper() == 'N':
            print('Returning to login screen...')
            login()
        else:
            print('ERROR: Invalid input.')
            print('Returning to login screen...')
            login()
        

def add_user(username):
    loaded_users_dict['users'].append(username)
    print('{} added to users database.'.format(username))
    verify_manga_file(username)


def verify_manga_file(username):
    manga_file_exists = os.path.isfile('{}.json'.format(username))
    if manga_file_exists:
        print("{}'s manga file has been verified.".format(username))
    else:
        user_manga_file = open('{}.json'.format(username), 'w')
        user_manga_file.write('{ }')
        user_manga_file.close()
        print("{}'s manga file has been created.".format(username))
        

def load_manga_file(username):
    with open('{}.json'.format(username)) as manga_file:
        return json.load(manga_file)


def main_menu():
    while True:
        print('\nPlease select an option below:')
        print('1. Look-up Current Manga Progress.')
        print('2. Update / Add Manga Progress.')
        print('3. Remove Manga Progress.')
        print('4. List All Manga Entries.')
        print('5. Exit Program & Save Entries.')

        i = input(': ')
        if i == '1':
            manga_title = input("\nPlease enter the title of the manga (CASE SENSITIVE): ")
            manga_lookup(title=manga_title)
        elif i == '2':
            manga_title = input("\nPlease enter the title of the manga (CASE SENSITIVE): ")
            manga_chapter = input("\nPlease enter the chapter of the manga: ")
            manga_update(title=manga_title, chapter=manga_chapter)
        elif i == '3':
            manga_title = input("\nPlease enter the title of the manga you would like to delete (CASE SENSITIVE): ")
            manga_remove(title=manga_title)
        elif i == '4':
            manga_show_all(loaded_manga_dict)
        elif i == '5':
            save_manga_file(loaded_manga_dict)
            save_user_file(loaded_users_dict)
            break 
        else:
            print('\nError: Invalid input.')


def manga_show_all(loaded_manga_dict):
    print("\nAll Manga Entries:")
    for title, amount in loaded_manga_dict.items():
        print("{}: Chapter {}.".format(title, amount))



def manga_remove(title):
    if title in loaded_manga_dict:
        confirm = input('\nAre you sure you would like to delete {} from your manga entries? (y/n): '.format(title))
        if confirm.upper() == 'Y':
            print('\nDELETED {}.'.format(title))
            del loaded_manga_dict[title]
        elif confirm.upper() == 'N':
            print('\nRetruning to main menu...')
        else:
            print("\nERROR Invalid Input.")
    else:
        print("\nERROR {} does not exist.".format(title))

def manga_update(title, chapter):
    if title in loaded_manga_dict:
        loaded_manga_dict[title] = chapter
        print("\nUPDATED {}: Chapter {}".format(title, chapter))
    elif title not in loaded_manga_dict:
        loaded_manga_dict[title] = int(chapter)
        print('\nADDED {}: Chapter {}'.format(title, chapter))
    else:
        pass

def manga_lookup(title):
    print('\nSearching for {}...'.format(title))
    if title in loaded_manga_dict:
        chapter = loaded_manga_dict[title]
        print('\n{}: Chapter {}'.format(title, chapter))
    else:
        print('\nError: Manga not found.')

def save_manga_file(loaded_manga_dict):
    with open('{}.json'.format(username), 'w') as manga_file:
        json.dump(loaded_manga_dict, manga_file, indent=4)
        print('\nSaving and exiting...')


def save_user_file(loaded_users_dict):
    with open('users.json', 'w') as user_file:
        json.dump(loaded_users_dict, user_file, indent=4)


verify_user_file()
loaded_users_dict = load_user_file()
username = login() 
verify_existance(username) 
verify_manga_file(username)
loaded_manga_dict = load_manga_file(username)
main_menu()

#UPDATES TO COME: 

# ADD A WAY TO REMOVE USERS FROM USERS.JSON
# HANDLE ERRORS
