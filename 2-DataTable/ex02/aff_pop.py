import pandas as pd
from matplotlib import pyplot as plt


def parse_population_data(dataset, country):
    '''
    Converts population values to floatsfrom strings with suffixes \
        (e.g., "M" for million, "k" for thousand)
    '''
    try:
        country_data = dataset[dataset['country'] == country]
        pop_per_year = country_data.values[0][1:-50]
        for i, data in enumerate(pop_per_year):
            if data.endswith("B"):
                pop_per_year[i] = float(data[:-1]) * 1_000_000_000
            elif data.endswith("M"):
                pop_per_year[i] = float(data[:-1]) * 1_000_000
            elif data.endswith("k"):
                pop_per_year[i] = float(data[:-1]) * 1_000
            else:
                pop_per_year[i] = float(data)
        return pop_per_year

    except Exception as e:
        print(f"Error parsing population data for {country}: {e}")
        return None


def population_vs(dataset, country):
    '''
    Displays a graph of the population for Spain vs the specified \
    country in the dataset.
    '''
    try:
        years = range(1800, 2051)
        spain_population = parse_population_data(dataset, 'Spain')
        country_population = parse_population_data(dataset, country)
        max_y = max(max(spain_population), max(country_population))


        plt.title("Population Projections")
        plt.plot(years, spain_population, label="Spain")
        plt.plot(years, country_population, label=country)
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.xticks(range(1800, 2050, 40))
        plt.ylim(0, max_y + 10_000_000)
        plt.yticks([20_000_000, 40_000_000, 60_000_000], labels=["20M", "40M", "60M"])
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


def main():
    '''Main function to load the dataset and display the graph.'''
    dataset = pd.read_csv("population_total.csv")
    if dataset is not None:
        population_vs(dataset, "France")
        return 0
    return 1


if __name__ == "__main__":
    main()
