import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)
print("hello")
def get_big_mac_price_by_year(year,country_code):
    query = f"year == {year} and iso_a3 == '{country_code}'"
    result = df.query(query)[['name', 'iso_a3', 'dollar_price']]
    mean_price = result['dollar_price'].mean()
    return round(mean_price, 2)
    

def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    pass # Remove this line and code your user interface