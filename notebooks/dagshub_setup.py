import dagshub
dagshub.init(repo_owner='mewawalaabdeali', repo_name='MLOperation', mlflow=True)

import mlflow

mlflow.set_tracking_uri("https://dagshub.com/mewawalaabdeali/MLOperation.mlflow")
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)