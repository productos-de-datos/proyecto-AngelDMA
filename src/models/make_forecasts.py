def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    import pandas as pd
    import pickle
    import numpy as np

    df = pd.read_csv('data_lake/business/features/precios_diarios.csv')
    df['fecha'] = pd.to_datetime(df.fecha)

    with open("src/models/precios-diarios.pkl", "rb") as file:
        estimator = pickle.load(file)

    X = df.iloc[:, :-1]

    pred = estimator.predict(X)

    df["pronostico"] = pred

    df.to_csv('data_lake/business/forecasts/precios-diarios.csv', index=None)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_forecasts()
