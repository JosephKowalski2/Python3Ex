def greet(name):
    """
    :param name: name
    :return: prints Hello followed by name parameter
    """
    print("Hello " + name)

def name_input():
    """
    :return: name input from user
    """
    return input("Please enter your name \n")

def language_input():
    print("1. English")
    print("2. Spanish")
    print("3. French")
    chosen_language = input('Please choose a number for a language\n')
    if chosen_language == '1':
        print("You have chosen English")
        greet(name_input())
    elif chosen_language == '2':
        print("Has elegido español\n")
        spanish_input = input("por favor, escriba su nombre\n")
        print(f'Hola {spanish_input}')
    elif chosen_language == '3':
        print('Vous avez choisi le français\n')
        french_input = input('S`il vous plaît entrez votre nom\n')
        print(f'Bonjour {french_input}')

language_input()