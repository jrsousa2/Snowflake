# Video by Adam Marczak
# Databricks notebook source
blob_account_name = "azureopendatastorage"
blob_container_name = "citydatacontainer"
blob_relative_path = "Safety/Release/city=Boston"
blob_sas_token = r"?st=2019-02-26T02%3A34%3A32Z&se=2119-02-27T02%3A34%3A00Z&sp=rl&sv=2018-03-28&sr=c&sig=XlJVWA7fMXCSxCKqJm8psMOh0W4h7cSYO28coRqF2fs%3D"

# COMMAND ----------

wasbs_path = 'wasbs://%s@%s.blob.core.windows.net/%s' % (blob_container_name, blob_account_name, blob_relative_path)
spark.conf.set('fs.azure.sas.%s.%s.blob.core.windows.net' % (blob_container_name, blob_account_name), blob_sas_token)
print('Remote blob path: ' + wasbs_path)

# COMMAND ----------

# A Parquet file in Azure Databricks is a columnar storage file format commonly 
# used for storing large-scale data efficiently.

# Below will read the file from Azure blob storage as a parquet file into Databricks
df = spark.read.parquet(wasbs_path)
print('Register the DataFrame as a SQL temporary view: source')
df.createOrReplaceTempView('source')

# COMMAND ----------

df.count()

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT * FROM source LIMIT 10

# After the view is created, we can switch languages from Python to SQL for example
# This would give 10 lines of the view table we just created
%sql
select *
from source
limit 10
