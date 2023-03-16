import pandas as pd


def write_data(name, all_data):
    file_name = name.lower().replace(' ', '_')

    data = pd.DataFrame(all_data)
    print(data)
    data.to_csv(f'data/{file_name}.csv')


def compare_data(name, all_data):
    file_name = name.lower().replace(' ', '_')
    data = pd.read_csv(f'data/{file_name}.csv')

    brand_new_data = []

    old_data_titles = []
    for index, row in data.iterrows():
        old_data_titles.append(row['title'].lower())

    for item in all_data:
        if item['title'].lower() not in old_data_titles:
            brand_new_data.append(item)

    if brand_new_data:
        print(brand_new_data)
        return [True, brand_new_data]
    else:
        print(f"\n Unfortunately we didn't find new products for {name}\n")
        return [False]
