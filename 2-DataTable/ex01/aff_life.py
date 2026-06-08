from load_csv import load
from matplotlib import pyplot as plt


def display_graph(dataset):
    '''
    Displays a graph of the life expectancy in years for all the countries
    in the dataset.
    '''
    try:
        spain_data = dataset[dataset['country'] == 'Spain']
        years = spain_data.columns[1:]
        life_expectancy = spain_data.values[0][1:]

        plt.title("Spain Life Expectancy Projections")
        plt.plot(years, life_expectancy)
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.xticks(years[::40])
        plt.yticks(range(30, 100, 10))
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


def main():
    '''Main function to load the dataset and display the graph.'''
    dataset = load("life_expectancy_years.csv")
    if dataset is not None:
        display_graph(dataset)
        return 0
    return 1


if __name__ == "__main__":
    main()
