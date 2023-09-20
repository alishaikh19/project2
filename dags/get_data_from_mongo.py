def get_data_from_mongo():

   import pymongo
   import pandas as pd
   client=pymongo.MongoClient("mongodb+srv://shaikhmdali257:6QNQvKj0R4vHgEk4@cluster0.bl5rcx8.mongodb.net/?retryWrites=true&w=majority")
   db=client["mongodb"]
   collection=db["Advertisement"]

   data=[]
   for i in collection.find():
      data.append(i)

   df=pd.DataFrame(data)
   
   df.rename(columns={'_id':'id', 
            'Daily Time Spent on Site':'daily_time_spent_on_site', 
            'Area Income':'income', 
            'Daily Internet Usage':'daily_internet_usage',
            'Ad Topic Line':'topic',
            'Clicked on Ad':'clicked'}, inplace=True)

   df.to_csv('/opt/airflow/dags/data/advertising1.csv', index=False)

   print("this code is written by harry")

   print("this will load from mongodb avd 2")
   print("get data 1")

get_data_from_mongo()




