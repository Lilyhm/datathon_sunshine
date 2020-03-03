"""
Exploring different clustering methods
Starting with one I already know- knn
"""
import CLUSTERING.lilys_clustering.utils as ut

import pandas as pd

CONFIG_FILE_PATH = 'CLUSTERING/lilys_clustering/config.json'


def main():
    # Step 1: Connect to the data (only select the columns that you need)
    params = ut.read_params(CONFIG_FILE_PATH)
    df = pd.read_csv(params.RAW_FILE_PATH,
                     usecols=params.COLS_TO_USE,
                     parse_dates=params.DATETIME_COLS)

    # Step 2: clean the data
    """ Potential Cleaning:
        * one-hot encoding
    """

    # Step 3: perform clustering (ensure collection of metadata)

    return df.info()


if __name__ == "__main__":
    main()
