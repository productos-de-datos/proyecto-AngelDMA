from operator import index
from pandas import read_csv
import pandas as pd


def average_daily_price(file):
    '''
    Validar test
    >>> list(average_daily_price(pd.DataFrame({'fecha': ('2021-06-02', '2021-03-02', '2021-06-02', '2021-03-02'),'precio': (12, 40, 12, 80)})).precio)
    [60.0, 12.0]
    '''
    subset_file = file.copy()

    subset_file["fecha"] = pd.to_datetime(subset_file["fecha"])
    compute_daily_prices = subset_file.groupby(
        "fecha").mean({"precio": "precio"})
    compute_daily_prices.reset_index(inplace=True)
    subset_file = subset_file[["fecha", "precio"]]

    return compute_daily_prices


def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    import pandas as pd

    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    df = df.dropna()
    df = df.groupby(df.fecha).mean()
    df = df.iloc[:, 1:2]
    df.to_csv('data_lake/business/precios-diarios.csv')


def test_values_compute_daily_prices():
    df = pd.DataFrame({
        'fecha': ('2021-06-02', '2021-03-02', '2021-06-02', '2021-03-02'),
        'precio': (12, 40, 12, 80)
    })
    expect = [60.0, 12.0]
    assert list(average_daily_price(df).precio) == expect


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_daily_prices()
