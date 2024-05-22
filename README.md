# Model Metadata Uploader

https://github.com/moj-analytical-services/model-metadata/assets/15108577/4bd7a951-5860-40cc-bd00-de4bc93afa06

The Model Metadata Uploader is a Python package that simplifies the process of uploading metadata (metrics, parameters and monitoring args) to Athena for machine learning models. It provides a convenient interface for creating and managing metadata records associated with model runs, such as team name, project name, unique run ID, metrics, and timestamps. It follows the principles and logic of [MLFlow](https://mlflow.org/docs/latest/index.html) as we wish to move over to MLFlow in the near future.

There is a front-end application at: [https://model-metadata-uploader-dev.apps.live.cloud-platform.service.justice.gov.uk/](https://model-metadata-uploader-dev.apps.live.cloud-platform.service.justice.gov.uk/).

>[!Note]
>If you want to get access to this tool and front-end, [please submit a request here](https://github.com/moj-analytical-services/model-metadata/issues/new?assignees=&labels=&projects=&template=access.yml).

## Features
- Follows [MLFlow](https://mlflow.org/docs/latest/index.html) logic so you don't have to learn something different when we adopt MLFlow (Coming Soon).
- Easy Integration: Quickly integrate metadata uploading into your machine learning pipelines.
- Flexible Configuration: Customize metadata records with team name, project name, unique run ID, and additional metrics.
- Athena Integration: Seamlessly store metadata in Amazon Athena for easy querying and analysis.
- Automatic Timestamping: Automatically record timestamps for each metadata entry.

## Installation

You can install the Model Metadata Uploader from our GitHub repository:

``` bash
pip install model_metadata@git+https://github.com/moj-analytical-services/model_metadata
```

## Simple Usage

Results are saved in the `model_metadata` database on Athena under either:
- table `metrics` for `log_metric()`
- table `params` for `log_params()`
- table `measurements` for `log_measurement()`

Here's how you can use the Model Metadata Uploader in your Python code:

```python
from model_metadata.uploader import MetadataUploader

# Initialize MetadataUploader with team name, project name, and optional unique run ID
metup = MetadataUploader(team='TeamA', experiment='Exp1')

# Log a metric with name 'accuracy' and value 0.95
metup.log_metric('accuracy', 0.95)

# Log a param with name 'test_train_split' and value 0.4
metup.log_param('test_train_split', 0.4)

# Log a measurment with name 'load_name' and value0.1
metup.log_measurement('load_time', 0.1)

```
You can customize the metadata by providing additional metrics and a unique run ID. If left blank the package will assign a random hex to your run id which will be the same across your metrics, parameters and monitoring args:

```python
# Initialize MetadataUploader with custom unique run ID
metup = MetadataUploader(team='TeamA', experiment='Exp1', run_name='Run1')

# Upload multiple metrics
metup.log_metric('accuracy', 0.95)
metup.log_metric('loss', 0.1)
```

## Usage with sklearn (sci-kit learn)

See [/examples](/examples) folder for a demo of the below.

You can use it alongside sklearn for example to save model metrics:

``` python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from model_metadata.uploader import MetadataUploader

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

# Initialize MetricsUploader with team name and project name
metup = MetadataUploader(team='TeamA', experiment='Exp1')

# Upload evaluation metrics to Athena
metup.log_metric('mean_squared_error', mse)
metup.log_metric('mean_absolute_error', mae)

```

## Documentation
For detailed documentation and API reference, please refer to the `/docs` folder (coming soon).

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.
