# This is a password generator that allows the user to generate their own random password

import random
import string

print('''
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$                     
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o                   
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o             
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o                Welcome to Will's
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$           Custom Password Generator!
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""                
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                 oo             o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""  
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$       
                                """"$$$$$$$$$$$        
                                    $$$$$$$$$$$$       
                                     $$$$$$$$$$"      
                                      "$$$""""

''')










# Sets the acceptable range for the password length

MIN_LENGTH = 6
MAX_LENGTH = 20


# Asks the user for their desired password length and validates it
while True:
    try:
        length = int(input("How long should your password be? Choose between 6 and 20 characters: "))
        if length < MIN_LENGTH:
            print("Too Short! Let's try to keep the password at least 6 characters for security.")
        elif length > MAX_LENGTH:
            print("Woah there partner! Let's try not to exceed 20 characters to keep things reasonable.")
        else:
            break # break is if a valid length is entered
    except ValueError:
        print("Sorry, You have to enter a valid number, not words or symbols.")


# Helps to validate 'y' or 'n' input
def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ('y', 'n'):
            return answer == 'y' # Return True for 'y', False for 'n'
        else:
            print("Sorry, you have to enter either 'y' for yes or 'n' for no.")


# Asks the users what types of characters they would like to includeand validates it
uppercase = ask_yes_no("Would you like the password to include capital letters? (y/n): ")
print(""" """)
lowercase = ask_yes_no("Would you like the password to include lowercase letters? (y/n):")
print(""" """)
numbers = ask_yes_no("Should we add in some numbers? (y/n): ")
print(""" """)
specials = ask_yes_no("Should we add some special symbols? (y/n): ")
print(""" """)


## Builds the character pool based on user choices
characters = ''
if uppercase:
    characters += string.ascii_uppercase
if lowercase:
    characters += string.ascii_lowercase
if numbers:
    characters += string.digits
if specials:
    characters += string.punctuation

# Checks if at least one type was chosen
if not characters:
    print("Looks like you didn't choose any character types :/ I can't generate a password without any of the ingredients!")
else:
    # Generates password of requested length using allowed characters
    password = ''.join(random.choice(characters) for _ in range(length))
print("""

""")
      
print("Alright! Here's your brand new freshly generated password:")
print(password)
      




