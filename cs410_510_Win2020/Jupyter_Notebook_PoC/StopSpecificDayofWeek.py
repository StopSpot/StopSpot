#!/usr/bin/env python
# coding: utf-8

# # initial aggregate time analysis

# In[2]:


import pandas as pd
import psycopg2 #communicate with postgresdb
import sqlalchemy #generage SQL statements
import plotly as py
import plotly.graph_objs as go
import plotly.tools as tl
import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)


# In[3]:


from sqlalchemy import create_engine

POSTGRES_PORT = 5432
POSTGRES_ADDRESS = '35.247.104.201'
POSTGRES_USERNAME = 'postgres'
POSTGRES_PASSWORD = 
POSTGRES_DBNAME = 'postgres'
postgres_login = f'postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_ADDRESS}:{POSTGRES_PORT}/{POSTGRES_DBNAME}'
connection = create_engine(postgres_login)#connect to db


# In[4]:


df = pd.read_sql_query('''SELECT route_number, COUNT(route_number) as count FROM stop_instance WHERE location_id is not NULL AND door = 1 AND location_distance > 98.4252 GROUP BY route_number;''', connection)




# In[5]:


fig2 = go.Figure()
fig2.add_trace(go.Bar(x=df['route_number'],y=df['count'],name='out of bounds stops'))
fig2.update_traces(opacity=.50)
fig2.show()


# In[35]:



fig3 = go.Figure()
fig3.add_trace(go.Bar(x=dz.service_date,y=dz['count'],name='out of bounds stops'))
fig3.add_trace(go.Bar(x=dy.service_date,y=dy['count'],name='in bounds stops'))
fig3.update_layout(
    barmode='overlay', 
    title='Out of bound vs in bound stops by day of week',
    xaxis_title='day of week',
    yaxis_title='number of stop instances'
    )
fig3.update_traces(opacity=.50)
fig3.show()


# In[8]:


top = pd.read_sql_query('''SELECT location_id, COUNT(location_id) as count FROM stop_instance WHERE location_id is not NULL AND door = 1 AND location_distance > 98.4252 GROUP BY location_id ORDER BY count DESC LIMIT 10;''', connection)

for (location_id, data) in top.iterrows():
    out_b = f'SELECT location_id, service_date FROM stop_instance WHERE location_id = {data.location_id} AND door = 1 AND location_distance > 98.4252;'
    in_b = f'SELECT location_id, service_date FROM stop_instance WHERE location_id = {data.location_id} AND door = 1 AND location_distance <= 98.4252;'
    o = pd.read_sql_query(''+out_b+'',connection)
    i = pd.read_sql_query(''+in_b+'',connection)
    o['service_date']= pd.to_datetime(o['service_date'])
    o['service_date']= o.service_date.dt.dayofweek
    do = o.groupby('service_date').service_date.agg('count').to_frame('count').reset_index()
    i['service_date']= pd.to_datetime(i['service_date'])
    i['service_date']= i.service_date.dt.dayofweek
    di = i.groupby('service_date').service_date.agg('count').to_frame('count').reset_index()
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(x=do.service_date,y=do['count'],name='out of bounds stops'))
    fig4.add_trace(go.Bar(x=di.service_date,y=di['count'],name='in bounds stops'))
    fig4.update_layout(
        barmode='overlay', 
        title='Out of bound vs in bound stops by day of week '+str(data.location_id),
        xaxis_title='day of week',
        yaxis_title='number of stop instances'
    )
    fig4.update_traces(opacity=.50)
    fig4.show()


# In[ ]:




