
from airflow.plugins_manager import AirflowPlugin
from BQCustomPlugin.operators.custom_gcs_to_bq import GoogleCloudStorageToBigQueryOperator

class BQCustomPlugin(AirflowPlugin):
    name = "BQCustomPlugin"
    operators = [GoogleCloudStorageToBigQueryOperator]
    # Leave in for explicitness
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []