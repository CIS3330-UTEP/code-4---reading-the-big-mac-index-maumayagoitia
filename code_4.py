import pandas as pd

big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    country_code = country_code.upper()
    query = f"date.str.startswith('{year}') and iso_a3 == '{country_code}'"
    result = df.query(query)
    mean_price = result['dollar_price'].mean()
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    query = f"iso_a3 == '{country_code}'"
    result = df.query(query)
    mean_price = result['dollar_price'].mean()
    return round(mean_price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    cheapest = df.query(f'date.str.startswith("{year}")')['dollar_price'].idxmin()
    cheapestmac = df.loc[cheapest]
    return f"{cheapestmac['name']}({cheapestmac['iso_a3']}): ${round(cheapestmac['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    expensive = df.query(f'date.str.startswith("{year}")')['dollar_price'].idxmax()
    expensivemac = df.loc[expensive]
    return f"{expensivemac['name']}({expensivemac['iso_a3']}): ${round(expensivemac['dollar_price'], 2) }"

if __name__ == "__main__":
    while True:
        print("\n1. Get Big Mac price by year and country code")
        print("2. Get Big Mac price by country code")
        print("3. Get the cheapest Big Mac price by year")
        print("4. Get the most expensive Big Mac price by year")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            year = input("Enter year: ")
            country_code = input("Enter country code: ").upper()
            price = get_big_mac_price_by_year(year, country_code)
            print(f"The mean Big Mac price in {country_code} for the year {year} is {country_code}.")
        elif choice == '2':
            country_code = input("Enter country code: ").upper()
            price = get_big_mac_price_by_country(country_code)
            print(f"The mean Big Mac price in {country_code} is ${price}.")
        elif choice == '3':
            year = input("Enter year: ")
            print(get_the_cheapest_big_mac_price_by_year(year))
        elif choice == '4':
            year = input("Enter year: ")
            print(get_the_most_expensive_big_mac_price_by_year(year))
        elif choice == '5':
            break
        else:
            print("Invalid choice")