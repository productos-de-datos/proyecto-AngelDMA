def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    import pandas as pd

    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    df = df.dropna()
    df['fecha'] = pd.to_datetime(df.fecha)
    df['fecha'] = df['fecha'] + pd.offsets.MonthBegin(-1)
    df = df.groupby(df.fecha).mean()
    df = df.iloc[:, 1:2]
    df.to_csv('data_lake/business/precios-mensuales.csv')


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_monthly_prices()
