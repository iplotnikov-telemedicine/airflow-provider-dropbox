__version__ = "1.0.0"


def get_provider_info():
    return {
        "package-name": "airflow-provider-dropbox",  # Required
        "name": "dropbox",  # Required
        "description": "",  # Required
        "connection-types": [
            {"connection-type": "dropbox", "hook-class-name": "dropbox.hooks.dropbox.DropboxBaseHook"}
        ],
        "versions": [__version__],  # Required
    }