from pyspark.sql import SparkSession

def process_data_in_pyspark():
    # Create a Spark session

    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, when, expr, avg
    from pyspark.sql.types import StringType
    
    spark = SparkSession.builder.appName("RetailDataTransformation").getOrCreate()
     # Read the CSV file into a DataFrame
    mysql_host = 8080
    mysql_port = 3306
    mysql_user = "root"
    mysql_password = "password"
    mysql_database = "mysql"
    mysql_table = "advertising1" 

    df = spark.read \
    .format("jdbc") \
    .option("url", f"jdbc:mysql://{mysql_host}:{mysql_port}/{mysql_database}") \
    .option("dbtable", mysql_table) \
    .option("user", mysql_user) \
    .option("password", mysql_password) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .load() 


    df=df.withcolumn("age_level",when(col("age").between(10,20),1)
                                .when(col("age").between(21,30),2)
                                .when(col("age").between(31,40),3)
                                .when(col("age").between(41,50),4).otherwise(5))
    
    df=df.withcolumn("date",col("timestamp").cast("date"))

    df=df.withcolumn("usage_level",when(col("daily_time_spent")/col("daily_internet_usage")<0.2,"Low")
                                .when(col("daily_time_spent")/col("daily_internet_usage")<0.3,"Medium")
                                .otherwise("high") )

      # Establish MySQL connection
    mysql_host = 8080
    mysql_port = 3306
    mysql_user = "root"
    mysql_password = "password"
    mysql_database = "mysql"
    mysql_table = "advertising_transformed"

    # Write the transformed data to MySQL
    df.write \
        .format("jdbc") \
        .mode("append") \
        .option("url", f"jdbc:mysql://{mysql_host}:{mysql_port}/{mysql_database}") \
        .option("dbtable", mysql_table) \
        .option("user", mysql_user) \
        .option("password", mysql_password) \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .save()
process_data_in_pyspark()