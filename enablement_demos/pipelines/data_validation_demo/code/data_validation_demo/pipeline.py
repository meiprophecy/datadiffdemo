from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from data_validation_demo.config.ConfigStore import *
from data_validation_demo.functions import *
from prophecy.utils import *
from data_validation_demo.graph import *

def pipeline(spark: SparkSession) -> None:
    df_generated_students1 = generated_students1(spark)
    expected_students(spark, df_generated_students1)
    df_expected_students2 = expected_students2(spark)
    df_reformat_customer_info = reformat_customer_info(spark, df_expected_students2)
    fixed_data(spark, df_reformat_customer_info)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("data_validation_demo").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/data_validation_demo")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/data_validation_demo", config = Config)(pipeline)

if __name__ == "__main__":
    main()
