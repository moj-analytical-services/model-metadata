import uuid
import datetime
import awswrangler as wr
import pandas as pd


class MetadataUploader:
    def __init__(self, team: str, project: str, unique_run_id: str=None, database: str='model_metadata', s3_path: str='s3://alpha-model-metadata/'):
        """
        Initialize the MetricsUploader instance.

        Parameters:
        team (str): The name of the team responsible for the project.
        project (str): The name of the project.
        unique_run_id (str, optional): A unique identifier for the run. If not provided, a random hex ID will be generated. Default is None.
        database (str, optional): The name of the Athena database to store metrics. Default is 'model_metadata'.
        s3_path (str, optional): The S3 path where the metrics data will be stored. Default is 's3://alpha-model-metadata/'.

        Attributes:
        team (str): The name of the team responsible for the project.
        project (str): The name of the project.
        unique_run_id (str): A unique identifier for the run.
        database (str): The name of the Athena database to store metrics.
        s3_path (str): The S3 path where the metrics data will be stored.
        timestamp (datetime): The timestamp when the MetricsUploader instance was created.
        """
        self.team = team
        self.project = project
        self.unique_run_id = unique_run_id or uuid.uuid4().hex
        self.database = database
        self.s3_path = s3_path
        self.timestamp = datetime.datetime.now()

    def upload_metric(self, metric: str, value: float, table: str='metrics'):
        """
        Upload a metric to the specified Athena table.

        Parameters:
        table (str): The name of the Athena table where the metric will be stored.
        metric (str): The name of the metric.
        value (float): The value of the metric.

        Creates a dictionary with the specified metric information, converts it to a Pandas DataFrame, 
        and writes it to the specified S3 path in Parquet format using awswrangler.

        The dictionary keys are:
        - 'team': The name of the team responsible for the project.
        - 'project': The name of the project.
        - 'unique_run_id': A unique identifier for the run.
        - 'table': The name of the Athena table.
        - 'metric': The name of the metric.
        - 'value': The value of the metric.
        - 'timestamp': The timestamp when the metric was uploaded.

        The DataFrame is then written to S3 in Parquet format and registered in the specified Athena database and table.

        Example usage:
            uploader = MetricsUploader(team='TeamA', project='ProjectX')
            uploader.upload_metric('accuracy', 0.95)
        """
        data = {
            'team': [self.team],
            'project': [self.project],
            'unique_run_id': [self.unique_run_id],
            'table': [table],
            'metric': [metric],
            'value': [value],
            'timestamp': [self.timestamp]
        }
        df = pd.DataFrame(data)
        wr.s3.to_parquet(
            df=df,
            path=f"{self.s3_path}",
            dataset=True,
            database=self.database,
            table=table
        )

    def upload_param(self, param: str, value: float, table: str='params'):
        """
        Upload a param to the specified Athena table.

        Parameters:
        table (str): The name of the Athena table where the param will be stored.
        param (str): The name of the param.
        value (float): The value of the param.

        Creates a dictionary with the specified param information, converts it to a Pandas DataFrame, 
        and writes it to the specified S3 path in Parquet format using awswrangler.

        The dictionary keys are:
        - 'team': The name of the team responsible for the project.
        - 'project': The name of the project.
        - 'unique_run_id': A unique identifier for the run.
        - 'table': The name of the Athena table.
        - 'param': The name of the param.
        - 'value': The value of the param.
        - 'timestamp': The timestamp when the param was uploaded.

        The DataFrame is then written to S3 in Parquet format and registered in the specified Athena database and table.

        Example usage:
            uploader = MetricsUploader(team='TeamA', project='ProjectX')
            uploader.upload_param('test_train_split', 0.4)
        """
        data = {
            'team': [self.team],
            'project': [self.project],
            'unique_run_id': [self.unique_run_id],
            'table': [table],
            'param': [param],
            'value': [value],
            'timestamp': [self.timestamp]
        }
        df = pd.DataFrame(data)
        wr.s3.to_parquet(
            df=df,
            path=f"{self.s3_path}",
            dataset=True,
            database=self.database,
            table=table
        )

    def upload_monitoring(self, monitoring_arg: str, value: float, table: str='monitoring'):
        """
        Upload a monitoring arg to the specified Athena table.

        Parameters:
        table (str): The name of the Athena table where the monitoring arg will be stored.
        param (str): The name of the monitoring arg.
        value (float): The value of the monitoring arg.

        Creates a dictionary with the specified monitoring arg information, converts it to a Pandas DataFrame, 
        and writes it to the specified S3 path in Parquet format using awswrangler.

        The dictionary keys are:
        - 'team': The name of the team responsible for the project.
        - 'project': The name of the project.
        - 'unique_run_id': A unique identifier for the run.
        - 'table': The name of the Athena table.
        - 'monitoring_arg': The name of the monitoring arg.
        - 'value': The value of the monitoring arg.
        - 'timestamp': The timestamp when the monitoring arg was uploaded.

        The DataFrame is then written to S3 in Parquet format and registered in the specified Athena database and table.

        Example usage:
            uploader = MetricsUploader(team='TeamA', project='ProjectX')
            uploader.upload_monitoring('load_time', 0.1)
        """
        data = {
            'team': [self.team],
            'project': [self.project],
            'unique_run_id': [self.unique_run_id],
            'table': [table],
            'monitoring_arg': [monitoring_arg],
            'value': [value],
            'timestamp': [self.timestamp]
        }
        df = pd.DataFrame(data)
        wr.s3.to_parquet(
            df=df,
            path=f"{self.s3_path}",
            dataset=True,
            database=self.database,
            table=table
        )

    def __str__(self):
        return f"MetricsUploader(team={self.team}, project={self.project}, unique_run_id={self.unique_run_id})"

# Example usage
if __name__ == "__main__":
    uploader = MetadataUploader(team='TeamA', project='ProjectX')
    uploader.upload_metric('accuracy', 0.95)
    uploader.upload_param('test_train_split', 0.4)
    uploader.upload_monitoring('load_time', 0.1)
    print(uploader)