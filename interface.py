import os


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
    print("\nOptions: a. New Search, b. Search for updates, c. List all past searches, q. Quit")

    while True:
        user_choice = input("\nWhat do you want to do today? ").lower()

        if user_choice == "a":
            s_old = input("\nWhat do you want to search today? ").lower()
            l_ask = input("\nDo you want results from China? (Yes/No) ").lower()

            s_new = s_old.replace(" ", "%20")

            if l_ask == "yes":
                urls = f"https://shopee.com.br/search?keyword={s_new}&page"
            else:
                urls = f"https://shopee.com.br/search?keyword={s_new}&locations=Nacional&noCorrection=true&page"

            return ["new_search", s_old, urls]

        elif user_choice == "b":
            all_csv_names = [item.replace(".csv", "").replace("_", " ") for item in os.listdir("data/")]
            all_csv_names_dic = {num: all_csv_names[num] for num in range(len(all_csv_names))}
            user_update = []
            all_urls = []

            print("\nYour past searches")
            for key, value in all_csv_names_dic.items():
                print(f"\n{key}. {value}")

            update_choice = input("\nDo you want seek for updates for all your past searches? (Yes/No) ").lower()
            if update_choice == "yes":
                for name in all_csv_names:
                    new_name = name.replace(" ", "%20")
                    all_urls.append(f"https://shopee.com.br/search?keyword={new_name}&page")

                return ["update", all_csv_names, all_urls]

            else:
                user_update_select = input("Select the items you want to update separated by spaces: (ex: 0 1 3 5 7) ")
                all_update_select = [int(num) for num in user_update_select.split()]
                for index in all_update_select:
                    user_update.append(all_csv_names_dic[index])
                    new_name = all_csv_names_dic[index].replace(" ", "%20")
                    all_urls.append(f"https://shopee.com.br/search?keyword={new_name}&page")

                return ["update", user_update, all_urls]

        elif user_choice == "c":
            all_csv_names = [item.replace(".csv", "").replace("_", " ") for item in os.listdir("data/")]
            for name in all_csv_names:
                print(f"\n{name}")

        elif user_choice == "q":
            break

        else:
            print(f"\n{user_choice} is not a valid option type something else!")


