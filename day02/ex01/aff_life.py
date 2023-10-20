from load_csv import load
import matplotlib.pyplot as plt


def main():
    df = load("data/life_expectancy_years.csv")
    years = df.columns[1:].tolist()
    expectancies = df[df['country'] == 'France'].iloc[0, 1:].values
    plt.plot(years, expectancies)
    plt.title('France Life expectay Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectacy')
    plt.xticks(years[::40])
    plt.show()


if __name__ == "__main__":
    main()
