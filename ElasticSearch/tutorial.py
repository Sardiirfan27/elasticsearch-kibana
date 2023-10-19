import psycopg2 as db
from elasticsearch import Elasticsearch
import pandas as pd


# conn_string="dbname='postgres' host='localhost' user='postgres' password='12345678'"
# conn=db.connect(conn_string)

# df=pd.read_sql("select * from car_assignment", conn)
# df.to_csv('postgresqldata.csv')
# print("-------Data Saved------")

es = Elasticsearch(hosts="http://localhost:9200") 
df=pd.read_csv('postgresqldata.csv')
for i,r in df.iterrows():
	doc=r.to_json()
	res=es.index(index="frompostgresql", body=doc)
	print(res)