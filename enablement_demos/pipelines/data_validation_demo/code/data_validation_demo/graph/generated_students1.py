from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from data_validation_demo.config.ConfigStore import *
from data_validation_demo.functions import *

def generated_students1(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("dbfs:/demos/datadiff/students1parq/")
