import interface
import data_manager
import data_scraper
import email_sender

# Print the interface and get what the user wrote to search and the url
interfaces = interface.user_interface()
if interfaces[0] == "new_search":
    urls = interfaces[2]
    user_input = interfaces[1]

    # Get all the data from the search
    all_data = data_scraper.scrape_website(urls)

    # Write all the data that has been found into a csv file
    data_manager.write_data(user_input, all_data)

# Check if the user searched for it before, if the data already exist checks if there is a new product to alert
if interfaces[0] == "update":
    urls = interfaces[2]
    user_input = interfaces[1]

    for num in range(len(urls)):
        if data_manager.data_exists(user_input[num]):

            print(f"Searching new items for {user_input[num]}")
            all_data = data_scraper.scrape_website(urls[num])
            brand_new_item = data_manager.compare_data(user_input[num], all_data)

            if brand_new_item[0]:
                email_sender.send_email(brand_new_item[1])

            data_manager.write_data(user_input[num], all_data)









