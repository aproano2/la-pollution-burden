import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score



def clean_data(file_loc, county_list=None, impute=None):
    """
    This function loads and cleans the CES3.0 enviromental data
    provided by the state of California that can be found at:
    https://oehha.ca.gov/calenviroscreen/maps-data
    Inputs:
    - file_loc - location of the csv file with the data
    - county_list - list of California counties to be used
    - impute - method is "delete" rows or use the zip code "mean"
               if something else is passed, rows are deleted
    Output:
    - cleaned dataframe
    """
    # Read data from file
    df = pd.read_csv(file_loc)

    # Get data from the list of counties if provided
    if county_list:
        counties = '|'.join(county_list)
        df = df[df['California County'].str.contains(counties)]
        df.reset_index(drop=True, inplace=True)

    # Rename columns with long names
    long_cols = {'Nearby City \n(to help approximate location only)':
                 'Nearby City'}
    df.rename(index=str, columns=long_cols, inplace=True)

    # Lower capitalize all column names and remove spaces and points
    df.columns = [x.strip().replace(' ', '_').replace('\n','').\
                 replace('.','').lower() for x in df.columns]

    # Remove percentile columns data from
    pctl_cols = df.columns[df.columns.str.contains('pctl|percentile')]
    df.drop(pctl_cols, axis=1, inplace=True)

    # Impute the data with the column mean or just delete the rows
    if impute:
        if impute == 'mean':
            for col in set(df.columns[df.isnull().mean() > 0]):
                df[col].fillna(df[col].mean(), inplace=True)
        else:
            df.dropna(inplace=True)

    return df


def handle_categorical(df, cat_columns):
    """
    Handle categorical values by creating dummy columns
    Input:
    - df - dataframe
    - cat_columms - list of categorical columns
    Output:
    Dataframe with dummy columns
    """
    return pd.get_dummies(df, columns=cat_columns)


def run_regression(df, response_col, var_cols, tsize=0.25, rndm=0):
    """
    Run regression
    Input:
    - df - dataframe
    - response_col - name of the response column
    - var_cols - name of the columns to be considered as variables
    - tsize - fraction of data to be used for testing
    - rndm - random number generator seed used to split data
    Output:
    - r2_train - r square score for the training set
    - r2_test - r square score for the test set
    """
    # Split the data
    X = df[var_cols].drop(response_col, axis=1)
    y = df[response_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=tsize,
                                                        random_state=rndm)

    #fit the model and obtain pred response
    lm_model = LinearRegression(normalize=True)
    lm_model.fit(X_train, y_train)
    y_test_preds = lm_model.predict(X_test)
    y_train_preds = lm_model.predict(X_train)

    return r2_score(y_train, y_train_preds), r2_score(y_test, y_test_preds)
