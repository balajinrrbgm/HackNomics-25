import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import *
from datetime import datetime

# Initialize Glue context
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Data sources configuration
economic_data_path = "s3://econosense-data/raw-data/economic/"
news_data_path = "s3://econosense-data/raw-data/news/"
processed_data_path = "s3://econosense-data/processed-data/"

# Read economic indicators data
economic_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [economic_data_path]},
    format="csv"
)

# Read news data
news_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [news_data_path]},
    format="json"
)

# Transform economic data
economic_df = economic_dyf.toDF()
economic_df = economic_df.withColumn("timestamp", to_timestamp("date"))
economic_df = economic_df.dropDuplicates(["indicator", "timestamp"])

# Transform news data
news_df = news_dyf.toDF()
news_df = news_df.withColumn("publish_date", to_timestamp("publishDate"))
news_df = news_df.dropDuplicates(["title", "publish_date"])

# Join datasets where applicable
combined_df = economic_df.join(
    news_df,
    economic_df.timestamp.cast("date") == news_df.publish_date.cast("date"),
    "outer"
)

# Write processed data back to S3
processed_dyf = DynamicFrame.fromDF(combined_df, glueContext, "processed_data")
glueContext.write_dynamic_frame.from_options(
    frame=processed_dyf,
    connection_type="s3",
    connection_options={
        "path": processed_data_path,
        "partitionKeys": ["indicator"]
    },
    format="parquet"
)

# Commit the job
job.commit()