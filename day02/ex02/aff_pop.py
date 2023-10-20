from load_csv import load
import matplotlib.pyplot as plt


def format(xs):
    for i in range(len(xs)):
        s = xs[i]
        if s.endswith('k'):
            xs[i] = int(float(s[:-1]) * 1000)
        elif s.endswith('M'):
            xs[i] = int(float(s[:-1]) * 1000000)
        elif s.endswith('B'):
            xs[i] = int(float(s[:-1]) * 1000000000)
    return xs


def main():

    # Read the CSV file into a pandas DataFrame
    df = load("data/population_total.csv")

    # Remove DataFrame columns from 2051 to 2100
    df = df.drop(columns=[str(year) for year in range(2051, 2101)])

    # Years on x axis
    years = list(map(int, df.columns[1:].tolist()))

    # Populations on y axis
    population_france = df[df['country'] == 'France'].iloc[0, 1:].values
    population_belgium = df[df['country'] == 'Belgium'].iloc[0, 1:].values

    # Convert 'k's and 'M's to decimals
    population_france = format(population_france)
    population_belgium = format(population_belgium)

    # Some convenient variables
    population_max = max(population_france + population_belgium)
    population_tick = 20000000
    population_range = range(0, population_max, population_tick)

    # Create line plots
    plt.plot(years, population_france, label='France')
    plt.plot(years, population_belgium, label='Belgium')

    # Add title, labels, legend and custom ticks
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(years[::40])
    plt.yticks(population_range, [f'{int(val/1000000)}M' for val in population_range])
    plt.legend(loc='lower right')

    # Display the plot
    plt.show()


if __name__ == "__main__":
    main()
