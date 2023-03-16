ART ='''
   _____ __  ______  ____  ____________   ___________   ______  __________ 
  / ___// / / / __ \/ __ \/ ____/ ____/  / ____/  _/ | / / __ \/ ____/ __ 
  \__ \/ /_/ / / / / /_/ / __/ / __/    / /_   / //  |/ / / / / __/ / /_/ /
 ___/ / __  / /_/ / ____/ /___/ /___   / __/ _/ // /|  / /_/ / /___/ _, _/ 
/____/_/ /_/\____/_/   /_____/_____/  /_/   /___/_/ |_/_____/_____/_/ |_|  
        Mateus Oliveira© All Knights Reserved.                                                 
'''


def user_interface():

    '''
    Creates the user interface and returns the string the user typed, the string for search and the china status
    '''

    print(ART)
    print("\nWelcome to Shopee Finder, a nice robot to help you find your things out at shopee!")

    s_old = input("\nWhat do you want to search today? ").lower()
    l_ask = input("\nDo you want results from China? (Yes/No) ").lower()

    s_new = s_old.replace(" ", "%20")

    if l_ask == "yes":
        urls = f"https://shopee.com.br/search?keyword={s_new}&page"
    else:
        urls = f"https://shopee.com.br/search?keyword={s_new}&locations=Nacional&noCorrection=true&page"

    return [s_old, urls]
