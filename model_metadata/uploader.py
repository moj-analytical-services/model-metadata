import uuid
import datetime
import awswrangler as wr
import pandas as pd


class MetadataUploader:
    def __init__(self, team: str, experiment: str, run_name: str=None, database: str='model_metadata', s3_path: str='s3://alpha-model-metadata-app/'):
        """
        Initialize the MetricsUploader instance.

        Parameters:
        team (str): The name of the team responsible for the experiment.
        experiment (str): The name of the experiment.
        unique_run_id (str, optional): A unique identifier for the run. If not provided, a random hex ID will be generated. Default is None.
        database (str, optional): The name of the Athena database to store metrics. Default is 'model_metadata'.
        s3_path (str, optional): The S3 path where the metrics data will be stored. Default is 's3://alpha-model-metadata-app/'.

        Attributes:
        team (str): The name of the team responsible for the experiment.
        experiment (str): The name of the experiment.
        unique_run_id (str): A unique identifier for the run.
        database (str): The name of the Athena database to store metrics.
        s3_path (str): The S3 path where the metrics data will be stored.
        timestamp (datetime): The timestamp when the MetricsUploader instance was created.
        """
        self.team = team
        self.experiment = experiment
        self.run_name = run_name or uuid.uuid4().hex
        self.database = database
        self.s3_path = s3_path
        self.timestamp = datetime.datetime.now()

    def log_metric(self, metric: str, value: float, table: str='metrics'):
        """
        Log a metric to the specified Athena table.

        Parameters:
        table (str): The name of the Athena table where the metric will be stored.
        metric (str): The name of the metric.
        value (float): The value of the metric.

        Creates a dictionary with the specified metric information, converts it to a Pandas DataFrame, 
        and writes it to the specified S3 path in Parquet format using awswrangler.

        The dictionary keys are:
        - 'team': The name of the team responsible for the experiment.
        - 'experiment': The name of the experiment.
        - 'unique_run_id': A unique identifier for the run.
        - 'table': The name of the Athena table.
        - 'metric': The name of the metric.
        - 'value': The value of the metric.
        - 'timestamp': The timestamp when the metric was uploaded.

        The DataFrame is then written to S3 in Parquet format and registered in the specified Athena database and table.

        Example usage:
            metup = MetricsUploader(team='TeamA', experiment='Exp1', run_name='Run1')
            metup.log_metric('accuracy', 0.95)
        """
        data = {
            'team': [self.team],
            'experiment': [self.experiment],
            'run_name': [self.run_name],
            'table': [table],
            'metric': [metric],
            'value': [value],
            'timestamp': [self.timestamp]
        }
        df = pd.DataFrame(data)
        wr.s3.to_parquet(
            df=df,
            path=f"{self.s3_path}metrics",
            dataset=True,
            database=self.database,
            table=table
        )

    def log_param(self, param: str, value: float, table: str='params'):
        """
        Log a param to the specified Athena table.

        Parameters:
        table (str): The name of the Athena table where the param will be stored.
        param (str): The name of the param.
        value (float): The value of the param.

        Creates a dictionary with the specified param information, converts it to a Pandas DataFrame, 
        and writes it to the specified S3 path in Parquet format using awswrangler.

        The dictionary keys are:
        - 'team': The name of the team responsible for the experiment.
        - 'experiment': The name of the experiment.
        - 'unique_run_id': A unique identifier for the run.
        - 'table': The name of the Athena table.
        - 'param': The name of the param.
        - 'value': The value of the param.
        - 'timestamp': The timestamp when the param was uploaded.

        The DataFrame is then written to S3 in Parquet format and registered in the specified Athena database and table.

        Example usage:
            metup = MetricsUploader(team='TeamA', experiment='Exp1', run_name='Run1')
            metup.log_param('test_train_split', 0.4)
        """
        data = {
            'team': [self.team],
            'experiment': [self.experiment],
            'run_name': [self.run_name],
            'table': [table],
            'param': [param],
            'value': [value],
            'timestamp': [self.timestamp]
        }
        df = pd.DataFrame(data)
        wr.s3.to_parquet(
            df=df,
            path=f"{self.s3_path}params",
            dataset=True,
            database=self.database,
            table=table
        )

    def log_measurement(self, measurement: str, value: float, table: str='measurements'):
        """
        Log a measurement to the specified Athena table.

        Parameters:
        table (str): The name of the Athena table where the monitoring arg will be stored.
        measurement (str): The name of the measurement.
        value (float): The value of the measurement.

        Creates a dictionary with the specified measurement information, converts it to a Pandas DataFrame, 
        and writes it to the specified S3 path in Parquet format using awswrangler.

        The dictionary keys are:
        - 'team': The name of the team responsible for the experiment.
        - 'experiment': The name of the experiment.
        - 'unique_run_id': A unique identifier for the run.
        - 'table': The name of the Athena table.
        - 'measurement': The name of the measurement.
        - 'measurement': The value of the measurement.
        - 'timestamp': The timestamp when the monitoring arg was uploaded.

        The DataFrame is then written to S3 in Parquet format and registered in the specified Athena database and table.

        Example usage:
            metup = MetricsUploader(team='TeamA', experiment='Exp1', run_name='Run1')
            metup.log_measurement('load_time', 0.1)
        """
        data = {
            'team': [self.team],
            'experiment': [self.experiment],
            'run_name': [self.run_name],
            'table': [table],
            'measurement': [measurement],
            'value': [value],
            'timestamp': [self.timestamp]
        }
        df = pd.DataFrame(data)
        wr.s3.to_parquet(
            df=df,
            path=f"{self.s3_path}measurements",
            dataset=True,
            database=self.database,
            table=table
        )

    def __str__(self):
        return f"MetricsUploader(team={self.team}, run_name={self.run_name}, run_name={self.run_name})"

# Example usage
if __name__ == "__main__":
    metup = MetadataUploader(team='TeamA', experiment='Exp1', run_name='Run1')
    metup.log_metric('accuracy', 0.95)
    metup.log_param('test_train_split', 0.4)
    metup.log_measurement('load_time', 0.1)
    print(metup)
