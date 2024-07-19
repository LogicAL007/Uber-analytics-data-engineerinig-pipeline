import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api():
    """
    this function loads data from google cloud storage into a dataframe

    :return: A dataframe of the uber data
    """
    url = 'https://storage.googleapis.com/uber_dataset1/uber_data.csv'
    response = requests.get(url)

    return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output) -> None:
    """
    This function is the code for testing the output of the block.
    """
    assert output is not None
