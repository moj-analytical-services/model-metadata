import pytest
from unittest.mock import patch, MagicMock
from model_metadata.model_metadata import MetadataUploader
import awswrangler as wr
import uuid
import datetime

@pytest.fixture
def mock_to_parquet():
    with patch('awswrangler.s3.to_parquet') as mock:
        yield mock

def test_log_metric(mock_to_parquet):
    # Create an instance of MetricsUploader
    metup = MetadataUploader(team='TeamA', experiment='Exp1', run_name='Run1')
    
    # Call log_metric method
    metup.log_metric('accuracy', 0.95)
    
    # Get the arguments that were passed to to_parquet
    args, kwargs = mock_to_parquet.call_args_list[0]
    
    # Check if the DataFrame contains correct data
    df = kwargs['df']

    assert df['team'].iloc[0] == 'TeamA'
    assert df['experiment'].iloc[0] == 'Exp1'
    assert df['run_name'].iloc[0] == 'Run1'
    assert df['metric'].iloc[0] == 'accuracy'
    assert df['value'].iloc[0] == 0.95
    assert df['table'].iloc[0] == 'metrics'

    # # Check if the S3 path, database, and table are correct
    assert metup.s3_path == 's3://alpha-model-metadata/'
    assert metup.database == 'model_metadata'
    assert metup.timestamp.date() == datetime.datetime.now().date()

def test_log_param(mock_to_parquet):
    # Create an instance of MetricsUploader
    metup = MetadataUploader(team='TeamB', experiment='Exp2', run_name='Run2')
    
    # Call log_param method
    metup.log_param('test_train_spilt', 0.4)
    
    # Get the arguments that were passed to to_parquet
    args, kwargs = mock_to_parquet.call_args_list[0]
    
    # Check if the DataFrame contains correct data
    df = kwargs['df']

    assert df['team'].iloc[0] == 'TeamB'
    assert df['experiment'].iloc[0] == 'Exp2'
    assert df['run_name'].iloc[0] == 'Run2'
    assert df['param'].iloc[0] == 'test_train_spilt'
    assert df['value'].iloc[0] == 0.4
    assert df['table'].iloc[0] == 'params'

    # # Check if the S3 path, database, and table are correct
    assert metup.s3_path == 's3://alpha-model-metadata/'
    assert metup.database == 'model_metadata'
    assert metup.timestamp.date() == datetime.datetime.now().date()

def test_log_measurement(mock_to_parquet):
    # Create an instance of MetricsUploader
    metup = MetadataUploader(team='TeamC', experiment='Exp3', run_name='Run3')
    
    # Call log_measurement method
    metup.log_measurement('load_time', 0.01)
    
    # Get the arguments that were passed to to_parquet
    args, kwargs = mock_to_parquet.call_args_list[0]
    
    # Check if the DataFrame contains correct data
    df = kwargs['df']

    assert df['team'].iloc[0] == 'TeamC'
    assert df['experiment'].iloc[0] == 'Exp3'
    assert df['run_name'].iloc[0] == 'Run3'
    assert df['measurement'].iloc[0] == 'load_time'
    assert df['value'].iloc[0] == 0.01
    assert df['table'].iloc[0] == 'measurements'

    # # Check if the S3 path, database, and table are correct
    assert metup.s3_path == 's3://alpha-model-metadata/'
    assert metup.database == 'model_metadata'
    assert metup.timestamp.date() == datetime.datetime.now().date()


def test_unique_run_name_generation():
    # Create an instance without providing unique_run_id
    metup = MetadataUploader(team='TeamA', experiment='Exp1')
    
    # Check if unique_run_id is generated and is a valid hex
    assert uuid.UUID(metup.run_name).hex == metup.run_name

