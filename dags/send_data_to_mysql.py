def send_data_to_mysql():
    import pymysql
    import csv
    import pandas as pd

    input_file_path = "/opt/airflow/dags/data/advertising1.csv"

     # # Define MySQL connection parameters
    mysql_host = 8080
    mysql_port = 3306
    mysql_user = "root"
    mysql_password = "password"
    mysql_database = "mysql"
    mysql_table = "advertising1"

    # # Create a connection to MySQL
    connection = pymysql.connect(
        host=mysql_host,
        port=mysql_port,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database
    )
                                
   
    

    with connection.cursor() as cursor:
        query='''create table if not exists {mysql_table} (id varchar(200),
                                                            daily_time_spent varchar(200), 
                                                            age int, 
                                                            area_income decimal(10,2),
                                                            daily_internet_usage decimal(10,2),
                                                            topic varchar(200),
                                                            city varchar(200),
                                                            male int,
                                                            country varchar(200),
                                                            timestamp timestamp,
                                                            clicked int);'''
        
        cursor.execute(query)

        with open(input_file_path,"r") as csv_file:
            csv_reader=csv.reader(csv_file)
            next(csv_reader)

        for row in csv_reader:
            insert_query="insert into advertising1 values( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
            cursor.execute(insert_query,tuple(row))
        
        connection.commit()


        connection.close()
send_data_to_mysql()


