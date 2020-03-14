#!/usr/bin/env python
# coding: utf-8

# # initial aggregate time analysis

# In[1]:


import pandas as pd
import psycopg2 #communicate with postgresdb
import sqlalchemy #generage SQL statements
import plotly as py
import plotly.graph_objs as go
import plotly.tools as tl
import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)


# In[2]:


from sqlalchemy import create_engine

POSTGRES_PORT = 5432
POSTGRES_ADDRESS = '35.247.104.201'
POSTGRES_USERNAME = 'postgres'
POSTGRES_PASSWORD = 
POSTGRES_DBNAME = 'postgres'
postgres_login = f'postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_ADDRESS}:{POSTGRES_PORT}/{POSTGRES_DBNAME}'
connection = create_engine(postgres_login)#connect to db


# In[3]:


top = pd.read_sql_query('''SELECT location_id, COUNT(location_id) as count FROM stop_instance WHERE location_id is not NULL AND door = 1 AND location_distance > 98.4252 GROUP BY location_id ORDER BY count DESC LIMIT 10;''', connection)

for (location_id, data) in top.iterrows():
    out_b = f'SELECT location_id, (leave_time/60.0/60.0) as leave_time FROM stop_instance WHERE location_id = {data.location_id} AND door = 1 AND location_distance > 98.4252;'
    in_b = f'SELECT location_id, (leave_time/60.0/60.0) as leave_time FROM stop_instance WHERE location_id = {data.location_id} AND door = 1 AND location_distance <= 98.4252;'
    o = pd.read_sql_query(''+out_b+'',connection)
    i = pd.read_sql_query(''+in_b+'',connection)
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=o.leave_time,name='out of bounds stops'))
    fig.add_trace(go.Histogram(x=i.leave_time,name='in bounds stops'))
    fig.update_traces(opacity=.50)
    fig.update_layout(
        title='In/Out of bounds by hour location_id '+str(data.location_id),
        xaxis_title='hour of day',
        yaxis_title='number of stop instances',
        barmode = 'overlay'
    )
    fig.show()


# In[4]:


pd.read_sql_query('''SELECT location_id, COUNT(location_id) as count FROM stop_instance WHERE location_id is not NULL AND door = 1 AND location_distance > 98.4252 GROUP BY location_id ORDER BY count DESC LIMIT 10;''', connection)


# In[5]:


pd.read_sql_query('''SELECT location_distance FROM stop_instance WHERE location_id = 6137 AND door = 1;''', connection)


# In[6]:


top1= pd.read_sql_query('''SELECT (location_distance * .3048) as location_distance FROM stop_instance WHERE location_id = 6137 AND door = 1;''', connection)

fig2 = go.Figure()
fig2.add_trace(go.Box(y=top1.location_distance, name='6137'))

fig2.show()


# In[7]:


top10 = pd.read_sql_query('''SELECT location_id, COUNT(location_id) as count FROM stop_instance WHERE location_id is not NULL AND door = 1 AND location_distance > 98.4252 GROUP BY location_id ORDER BY count DESC LIMIT 10;''', connection)

for (location_id, data) in top10.iterrows():
    bounds = pd.read_sql_query(f'SELECT (location_distance * .3048) as location_distance FROM stop_instance WHERE location_id ={data.location_id} AND door = 1;',connection)
    fig3 = go.Figure()
    fig3.add_trace(go.Box(x=bounds.location_distance, name=str(data.location_id)))
    fig3.update_layout(
        title='Box Plot '+str(data.location_id),
        xaxis_title='location_distance in meters',
        yaxis_title='location_id',
    )
    fig3.show()


# In[ ]:


top1= pd.read_sql_query('''SELECT (location_distance * .3048) as location_distance FROM stop_instance WHERE location_id = 6137 AND door = 1;''', connection)

fig2 = go.Figure()
fig2.add_trace(go.Box(y=top1.location_distance, name='6137'))

fig2.show()

