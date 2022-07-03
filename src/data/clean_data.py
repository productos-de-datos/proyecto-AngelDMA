def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    import pandas as pd

    column_names = ['fecha', 'hora', 'precio']
    valores = []

    for year in range(1995, 2022):
        df = pd.read_csv('data_lake/raw/{}.csv'.format(year),
                         sep=',', header=0, index_col=None)

        for i in df.values:
            fecha = i[0]
            for z in range(1, 25):
                valores.append([fecha, z-1, i[z]])

    df2 = pd.DataFrame(valores, columns=column_names, index=None)

    df2.to_csv('data_lake/cleansed/precios-horarios.csv', index=None, sep=',')


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    clean_data()
