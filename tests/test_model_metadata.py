import pytest
from unittest.mock import patch, MagicMock
from model_metadata import MetadataUploader
import awswrangler as wr
import uuid
import datetime

@pytest.fixture
def mock_to_parquet():
    with patch('awswrangler.s3.to_parquet') as mock:
        yield mock

def test_upload_metric(mock_to_parquet):
    # Create an instance of MetricsUploader
    uploader = MetadataUploader(team='TeamA', project='ProjectX', unique_run_id='12345')
    
    # Call upload_metric method
    uploader.upload_metric('accuracy', 0.95)
    
    # Get the arguments that were passed to to_parquet
    args, kwargs = mock_to_parquet.call_args_list[0]
    
    # Check if the DataFrame contains correct data
    df = kwargs['df']

    assert df['team'].iloc[0] == 'TeamA'
    assert df['project'].iloc[0] == 'ProjectX'
    assert df['unique_run_id'].iloc[0] == '12345'
    assert df['metric'].iloc[0] == 'accuracy'
    assert df['value'].iloc[0] == 0.95
    assert df['table'].iloc[0] == 'metrics'

    # # Check if the S3 path, database, and table are correct
    assert uploader.s3_path == 's3://alpha-model-metadata/'
    assert uploader.database == 'model_metadata'
    assert uploader.timestamp.date() == datetime.datetime.now().date()

def test_upload_param(mock_to_parquet):
    # Create an instance of MetricsUploader
    uploader = MetadataUploader(team='TeamA', project='ProjectX', unique_run_id='12345')
    
    # Call upload_param method
    uploader.upload_param('test_train_spilt', 0.4)
    
    # Get the arguments that were passed to to_parquet
    args, kwargs = mock_to_parquet.call_args_list[0]
    
    # Check if the DataFrame contains correct data
    df = kwargs['df']

    assert df['team'].iloc[0] == 'TeamA'
    assert df['project'].iloc[0] == 'ProjectX'
    assert df['unique_run_id'].iloc[0] == '12345'
    assert df['param'].iloc[0] == 'test_train_spilt'
    assert df['value'].iloc[0] == 0.4
    assert df['table'].iloc[0] == 'params'

    # # Check if the S3 path, database, and table are correct
    assert uploader.s3_path == 's3://alpha-model-metadata/'
    assert uploader.database == 'model_metadata'
    assert uploader.timestamp.date() == datetime.datetime.now().date()

def test_upload_monitoring(mock_to_parquet):
    # Create an instance of MetricsUploader
    uploader = MetadataUploader(team='TeamA', project='ProjectX', unique_run_id='12345')
    
    # Call upload_monitoring method
    uploader.upload_monitoring('load_time', 0.01)
    
    # Get the arguments that were passed to to_parquet
    args, kwargs = mock_to_parquet.call_args_list[0]
    
    # Check if the DataFrame contains correct data
    df = kwargs['df']

    assert df['team'].iloc[0] == 'TeamA'
    assert df['project'].iloc[0] == 'ProjectX'
    assert df['unique_run_id'].iloc[0] == '12345'
    assert df['monitoring_arg'].iloc[0] == 'load_time'
    assert df['value'].iloc[0] == 0.01
    assert df['table'].iloc[0] == 'monitoring'

    # # Check if the S3 path, database, and table are correct
    assert uploader.s3_path == 's3://alpha-model-metadata/'
    assert uploader.database == 'model_metadata'
    assert uploader.timestamp.date() == datetime.datetime.now().date()


def test_unique_run_id_generation():
    # Create an instance without providing unique_run_id
    uploader = MetadataUploader(team='TeamA', project='ProjectX')
    
    # Check if unique_run_id is generated and is a valid hex
    assert uuid.UUID(uploader.unique_run_id).hex == uploader.unique_run_id

def test_str_representation():
    uploader = MetadataUploader(team='TeamA', project='ProjectX', unique_run_id='12345')
    expected_str = "MetricsUploader(team=TeamA, project=ProjectX, unique_run_id=12345)"
    assert str(uploader) == expected_str

