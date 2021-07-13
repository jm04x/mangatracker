import os.path
import json

print('\nWelcome to Manga Tracker by jm.')

def save(loaded_dict):
    with open('manga.json', 'w') as manga_file:
        json.dump(loaded_dict, manga_file, indent=4)
        print('\nSaving and exiting...')
        

def load():
    if os.path.isfile('manga.json'):
        with open('manga.json') as manga_file:
            return json.load(manga_file)


def manga_show_all(loaded_dict):
    print("\nAll Manga Entries:")
    for title, amount in loaded_dict.items():
        print("{}: Chapter {}.".format(title, amount))



def manga_remove(title):
    if title in loaded_dict:
        confirm = input('\nAre you sure you would like to delete {} from your manga entries? (y/n): '.format(title))
        if confirm.upper() == 'Y':
            print('\nDELETED {}.'.format(title))
            del loaded_dict[title]
            return
        elif confirm.upper() == 'N':
            print('\nRetruning to main menu...')
            return
        else:
            print("\nERROR Invalid Input.")
            return
    else:
        print("\nERROR {} does not exist.".format(title))
        return

def manga_update(title, chapter):
    # User will input "<Manga Titile> <Chapter>" and this would update or create an entry within the json file.
    if title in loaded_dict:
        loaded_dict[title] = chapter
        print("\nUPDATED {}: Chapter {}".format(title, chapter))
    elif title not in loaded_dict:
        loaded_dict[title] = int(chapter)
        print('\nADDED {}: Chapter {}'.format(title, chapter))
    else:
        return
        
def manga_lookup(title):
    # User will input "<Manga Title>" and this will return the current chapter or porgress of the manga.
    print('\nSearching for {}...'.format(title))
    if title in loaded_dict:
        chapter = loaded_dict[title]
        print('\n{}: Chapter {}'.format(title, chapter))
    else:
        print('\nError: Manga not found.')
    # if the title of manga is found in the json file - return the chapter.
    # else print that its not found and return to menu.
    

def user_input():
    # Main menu basically will ask user what they want to do: lookup or update/add.
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
            manga_show_all(loaded_dict)
        elif i == '5':
            save(loaded_dict)
            break # Exits while loop and closes.
            
        else:
            print('\nError: Invalid input.')
        
# Checks for storage file. If not created, creates a new one.

file_exists = os.path.isfile('manga.json')
if file_exists:
    print('\nStorage File Verified.')
    loaded_dict = load()
    user_input()
else:
    manga_file = open('manga.json', 'w')
    manga_file.write('{ }')
    manga_file.close()
    print('\nNew Storage File Created.')
    loaded_dict = load()
    user_input()

# Add ability for different users.
