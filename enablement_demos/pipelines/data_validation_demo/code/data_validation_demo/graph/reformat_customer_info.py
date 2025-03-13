from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from data_validation_demo.config.ConfigStore import *
from data_validation_demo.functions import *

def reformat_customer_info(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("FirstName"), col("LastName"), col("Age"), col("Class"), col("Region").alias("City"))
