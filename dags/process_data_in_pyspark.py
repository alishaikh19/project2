from pyspark.sql import SparkSession

def process_data_in_pyspark():
    # Create a Spark session
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col,when

    spark=SparkSession.builder.appName("advertisement").getOrCreate()

    jdbc_url="jdbc:mysql://mysql:3306/mysql"

    connection_properties={"user": "mysql",
    "password": "password",
    "driver": "com.mysql.jdbc.Driver"}

    df=spark.read.jdbc(url=jdbc_url,table='advertising',properties=connection_properties)

    df=df.withColumn("age_level",when(col("age").between(10,20),1)
                                .when(col("age").between(21,30),2)
                                .when(col("age").between(31,40),3)
                                .when(col("age").between(41,50),4)
                                .otherwise(5)
                                )
    
    df=df.withColumn("date",col('timestamp').cast('date'))

    df=df.withColumn("usage_level",when(col('daily_time_spent_on_site')/col('daily_internet_usage')<0.2,"low")
                                .when(col('daily_time_spent_on_site')/col('daily_internet_usage')<0.3,"medium")
                                .otherwise("high"))

    df.write.jdbc(url=jdbc_url,table='advertising',mode='append',properties=connection_properties)

process_data_in_pyspark()