from setuptools import setup, find_packages

setup(
    name='model_metadata',
    version='0.1',
    packages=find_packages(include=['model_metadata', 'model_metadata.*']),
    install_requires=[
        'awswrangler',
        'pandas',
        'boto3'
    ],
    author='Michael Hodge',
    author_email='michael.hodge1@justice.gov.uk',
    description='A package for uploading model metadata to Athena',
    url='https://github.com/moj-analytical-services/model_metadata',
)