"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    import pandas as pd

    for year in range(1995, 2022):
        url = ''
        if year in range(2016, 2018):
            url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true'.format(
                year)
            archivo = pd.read_excel(url)
            archivo.to_excel('data_lake/landing/{}.xlsx'.format(year),
                             index=None, header=True)
        else:
            url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xlsx?raw=true'.format(
                year)
            archivo = pd.read_excel(url)
            archivo.to_excel('data_lake/landing/{}.xlsx'.format(year),
                             index=None, header=True)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ingest_data()
