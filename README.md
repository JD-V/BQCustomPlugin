# BQCustomPlugin
custom GCS to BQ operator with bug fix
https://stackoverflow.com/questions/55300785/google-cloud-composer-bigquery-operator-get-jobs-api-httperror-404

Keep this BQCustomPlugin folder as it is in your plugins folder.
jsut change import statement in your dag to this,

 from BQCustomPlugin.operators.custom_gcs_to_bq import GoogleCloudStorageToBigQueryOperator
 
 
