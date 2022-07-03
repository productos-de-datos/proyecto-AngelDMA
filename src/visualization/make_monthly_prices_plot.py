def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    import pandas as pd

    df = pd.read_csv('data_lake/business/precios-mensuales.csv')
    fig = df.plot(x='fecha', y='precio')

    fig2 = fig.get_figure()
    fig2.savefig('data_lake/business/reports/figures/monthly_prices.png')


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_monthly_prices_plot()
