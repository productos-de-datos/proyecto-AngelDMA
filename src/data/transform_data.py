def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    # 95 a 99 3
    # 20 a 2017 en adelante 2
    # else
    import pandas as pd

    for year in range(1995, 2022):
        if year in range(1995, 2000):
            df = pd.read_excel(
                'data_lake/landing/{}.xlsx'.format(year), header=3, index_col=None)
        elif year in range(2000, 2016):
            df = pd.read_excel(
                'data_lake/landing/{}.xlsx'.format(year), header=2, index_col=None)
        elif year in range(2016, 2018):
            df = pd.read_excel(
                'data_lake/landing/{}.xls'.format(year), header=2, index_col=None)
        else:
            df = pd.read_excel(
                'data_lake/landing/{}.xlsx'.format(year), header=0, index_col=None)

        df = df.iloc[:, 0:25]
        df.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                      '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
        df.to_csv('data_lake/raw/{}.csv'.format(year), sep=',', index=None)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()
