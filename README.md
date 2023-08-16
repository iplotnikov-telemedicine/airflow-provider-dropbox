<img src="https://i.ibb.co/Cv0yxLn/0-sesfl3-V6mvw-VQUb1.png" width="100" height="100"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://i.ibb.co/0QbntmD/dropbox-clipart-removebg-preview.png" width="100" height="100"/> 

# Airflow Provider for Dropbox

The Airflow Provider for Dropbox is a plugin that enables seamless communication between the Dropbox API and Apache Airflow, allowing you to integrate Dropbox functionality into your Airflow workflows. This provider simplifies the process of interacting with Dropbox, enabling you to easily perform actions like uploading files, downloading files, and managing Dropbox resources directly from your Airflow DAGs (Directed Acyclic Graphs).

## Features

- Authenticate with your Dropbox account using OAuth 2.0.
- Upload files to your Dropbox account.
- Download files from your Dropbox account.
- List files and folders in your Dropbox account.
- Delete files and folders from your Dropbox account.

## Installation

You can install the Airflow Provider for Dropbox using pip:

```python
pip install airflow-provider-dropbox
```


## Getting Started
1. First, you need to set up your Dropbox API credentials:

Go to the Dropbox App Console.
Create a new app and choose the appropriate access level (Full Dropbox or App Folder).
Generate an access token for your app.

2. Add the Dropbox connection to your Airflow connections:

In the Airflow UI, navigate to Admin > Connections.
Click the "Create" button to add a new connection.
Choose Dropbox as the Conn Type.
Enter your access token in the Login field.
Save the connection.

3. Start using the Dropbox operators in your DAGs:

```python
from airflow import DAG
from airflow.providers.dropbox.operators.dropbox import DropboxFileUploadOperator

default_args = {
   'owner': 'airflow',
   'depends_on_past': False,
   'start_date': datetime(2023, 8, 1),
}

with DAG('dropbox_dag', default_args=default_args, schedule_interval=None) as dag:
   upload_task = DropboxFileUploadOperator(
       task_id='upload_file',
       local_path='/path/to/local/file.txt',
       remote_path='/path/in/dropbox/file.txt',
       dropbox_conn_id='your_dropbox_conn',
   )
```

## Contributing
Contributions are welcome! If you'd like to contribute to the Airflow Provider for Dropbox, please follow the guidelines in CONTRIBUTING.md.

## License
This project is licensed under the Apache License 2.0.

Disclaimer: This project is not affiliated with or endorsed by Dropbox Inc.
