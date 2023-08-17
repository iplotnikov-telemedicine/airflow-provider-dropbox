__version__ = "1.0.0"


def get_provider_info():
    return {
        "package-name": "airflow-provider-dropbox",  # Required
        "name": "dropbox",  # Required
        "description": "This package provides the ability to communicate with the Dropbox API in Apache Airflow.",  # Required
        "connection-types": [
            {"connection-type": "dropbox", "hook-class-name": "airflow_provider_dropbox.hooks.dropbox.DropboxBaseHook"}
        ],
        "versions": [__version__],  # Required
    }