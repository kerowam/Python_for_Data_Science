import pandas as pd
import matplotlib.pyplot as plt


def projection_life(gdp_dataset, life_dataset, year):
    '''
    Displays a graph of the GDP per capita vs life expectancy for the \
    specified year.
    '''
    try:
        gdp_year = gdp_dataset[["country", str(year)]]
        life_year = life_dataset[["country", str(year)]]
        plt.title(f"{year}")
        plt.scatter(gdp_year[str(year)], life_year[str(year)])
        plt.xscale("log")
        plt.xticks([300, 1000, 10000], labels=["300", "1k", "10k"])
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


def main():
    '''Main function to load the dataset and display the graph.'''
    gdp_file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    gdp_dataset = pd.read_csv(gdp_file)
    life_dataset = pd.read_csv("life_expectancy_years.csv")
    if gdp_dataset is None or life_dataset is None:
        return 0
    projection_life(gdp_dataset, life_dataset, 1900)
    return 1


if __name__ == "__main__":
    main()
