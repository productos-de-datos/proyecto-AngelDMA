import os


def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    if not os.path.exists('./data_lake/'):
        os.mkdir('./data_lake/')
    if not os.path.exists('./data_lake/landing/'):
        os.mkdir('./data_lake/landing/')
    if not os.path.exists('./data_lake/raw/'):
        os.mkdir('./data_lake/raw/')
    if not os.path.exists('./data_lake/cleansed/'):
        os.mkdir('./data_lake/cleansed/')
    if not os.path.exists('./data_lake/business/'):
        os.mkdir('./data_lake/business/')
    if not os.path.exists('./data_lake/business/reports/'):
        os.mkdir('./data_lake/business/reports/')
    if not os.path.exists('./data_lake/business/reports/figures/'):
        os.mkdir('./data_lake/business/reports/figures/')
    if not os.path.exists('./data_lake/business/features/'):
        os.mkdir('./data_lake/business/features/')
    if not os.path.exists('./data_lake/business/forecasts/'):
        os.mkdir('./data_lake/business/forecasts/')


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    create_data_lake()
