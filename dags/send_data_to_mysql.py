def send_data_to_mysql():
    import pymysql
    import csv

    input_path='/opt/airflow/dag/data/advertising1.csv'

    connection=pymysql.connect(host="mysql",user="root",password="password",db="mysql")
    
    
    with connection.cursor() as cursor:
        query="""create table advertising if not exists ((id varchar(200),
                                                                daily_time_spent varchar(200), 
                                                                age int, 
                                                                area_income decimal(10,2),
                                                                daily_internet_usage decimal(10,2),
                                                                topic varchar(200),
                                                                city varchar(200),
                                                                male int,
                                                                country varchar(200),
                                                                timestamp timestamp,
                                                                clicked int);"""
        cursor.execute(query)


        with open(input_path,"r") as csv_file:
            csv_data=csv.reader(csv_file)
            next(csv_data)
            for i in csv_data:
                insert_query="insert into advertising values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(insert_query,i)
    connection.commit()
    connection.close()

send_data_to_mysql()


