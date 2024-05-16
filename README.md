# Model Metadata Uploader

The Model Metadata Uploader is a Python package that simplifies the process of uploading metadata (metrics, parameters and monitoring args) to Athena for machine learning models. It provides a convenient interface for creating and managing metadata records associated with model runs, such as team name, project name, unique run ID, metrics, and timestamps.

## Features
- Easy Integration: Quickly integrate metadata uploading into your machine learning pipelines.
- Flexible Configuration: Customize metadata records with team name, project name, unique run ID, and additional metrics.
- Athena Integration: Seamlessly store metadata in Amazon Athena for easy querying and analysis.
- Automatic Timestamping: Automatically record timestamps for each metadata entry.

## Installation

You can install the Model Metadata Uploader from our GitHub repository:

``` bash
pip install git+https://https://github.com/moj-analytical-services/model_metadata.git
```

## Simple Usage

Results are saved in the `model_metadata` database on Athena under either:
- table `metrics` for `upload_metric()`
- table `params` for `upload_params()`
- table `monitoring` for `upload_monitoring()`

Here's how you can use the Model Metadata Uploader in your Python code:

```python
from model_metadata import MetricsUploader

# Initialize MetricsUploader with team name, project name, and optional unique run ID
uploader = MetricsUploader(team='TeamA', project='ProjectX')

# Upload a metric with name 'accuracy' and value 0.95
uploader.upload_metric('accuracy', 0.95)

# Upload a param with name 'test_train_split' and value 0.4
uploader.upload_metric('test_train_split', 0.4)

# Upload a metric with name 'accuracy' and value 0.95
uploader.upload_monitoring('load_time', 0.1)

```
You can customize the metadata by providing additional metrics and a unique run ID. If left blank the package will assign a random hex to your run id which will be the same across your metrics, parameters and monitoring args:

```python
# Initialize MetricsUploader with custom unique run ID
uploader = MetricsUploader(team='TeamA', project='ProjectX', unique_run_id='12345')

# Upload multiple metrics
uploader.upload_metric('accuracy', 0.95)
uploader.upload_metric('loss', 0.1)
```

## Usage with sklearn (sci-kit learn)

You can use it alongside sklearn for example to save model metrics:

``` python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from model_metadata import MetricsUploader

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
uploader = MetricsUploader(team='TeamA', project='ProjectX')

# Upload evaluation metrics to Athena
uploader.upload_metric('mean_squared_error', mse)
uploader.upload_metric('mean_absolute_error', mae)

```

## Documentation
For detailed documentation and API reference, please refer to the `/docs` folder (coming soon).

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.