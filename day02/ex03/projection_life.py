from load_csv import load
import matplotlib.pyplot as plt


def main():

    # Read CSV files into pandas DataFrames
    df_life_expectancy = load("data/life_expectancy_years.csv")
    df_income_per_person = load("data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    # Keep only year 1900
    df_life_expectancy = df_life_expectancy[['country', '1900']]
    df_income_per_person = df_income_per_person[['country', '1900']]

    incomes = df_income_per_person.iloc[:, 1:].values.flatten()
    expectancies = df_life_expectancy.iloc[:, 1:].values.flatten()

    plt.scatter(incomes, expectancies)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.xscale('log', base=10)
    plt.xticks([300, 1000, 8000], ['300', '1k', '8k'])
    plt.show()


if __name__ == "__main__":
    main()
