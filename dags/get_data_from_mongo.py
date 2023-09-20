def get_data_from_mongo():
    # import pymongo
    from pymongo import MongoClient
    import pandas as pd

    # Replace <your_connection_string> with your actual connection string
    client = MongoClient("mongodb+srv://shaikhmdali257:6QNQvKj0R4vHgEk4@cluster0.bl5rcx8.mongodb.net/?retryWrites=true&w=majority")

    db=client["mongodb"]

    collection=db["Advertisement"]

    
      
    data=[]
    for i in collection.find():
        # print(i)
        data.append(i)
    # print(data)

    df=pd.DataFrame(data)
    print(df)
    df.rename(columns={'_id':'id', 
            'Daily Time Spent on Site':'daily_time_spent_on_site', 
            'Area Income':'income', 
            'Daily Internet Usage':'daily_internet_usage',
            'Ad Topic Line':'topic',
            'Clicked on Ad':'clicked'}, inplace=True)
    df.to_csv('/opt/airflow/dags/data/advertising1.csv', index=False)
get_data_from_mongo()





