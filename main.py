import interface
import data_manager
import data_scraper
import email_sender

interfaces = interface.user_interface()
urls = interfaces[1]

all_data = data_scraper.scrape_website(urls)

brand_new_item = data_manager.compare_data(interfaces[0], all_data)

if brand_new_item[0]:
    email_sender.send_email(brand_new_item[1])

data_manager.write_data(interfaces[0], all_data)


# TODO: Melhorar a interface e experiência do usuário








