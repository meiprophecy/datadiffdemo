from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from data_validation_demo.config.ConfigStore import *
from data_validation_demo.functions import *

def fixed_data(spark: SparkSession, in0: DataFrame):
    in0.write.format("parquet").mode("overwrite").save("dbfs:/demos/datadiff/fixed")

    def generated():
        return spark.read.format("parquet").load("dbfs:/demos/datadiff/fixed")

    def expected():
        return spark.read.parquet('dbfs:/demos/datadiff/students1parq/')

    DataFrameDiff.create_diff(
        expected_df = expected(), 
        generated_df = generated(), 
        key_columns = ["FirstName", "LastName"], 
        diff_key = "fixed_data"
    )
