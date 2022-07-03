from operator import index


def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    import pickle

    def load_Data():
        df = pd.read_csv(
            'data_lake/business/features/precios_diarios.csv')
        df['fecha'] = pd.to_datetime(df.fecha)
        return df

    def separar_datos(datos):
        df = datos
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1:]
        return X, y

    def train_model(X, y):
        regressor = RandomForestRegressor(n_estimators=100, random_state=0)
        regressor.fit(X, y.values.ravel())
        return regressor

    def save_Estimator(regressor):
        with open("src/models/precios-diarios.pkl", "wb") as file:
            pickle.dump(regressor, file)

    df = load_Data()
    X, y = separar_datos(df)
    regressor = train_model(X, y)
    save_Estimator(regressor)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()
