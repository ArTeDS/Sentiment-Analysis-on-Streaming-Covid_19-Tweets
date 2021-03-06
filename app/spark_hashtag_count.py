#!/usr/bin/env python
# coding: utf-8

# https://www.toptal.com/apache/apache-spark-streaming-twitter

# In[1]:


# import os
# os.environ['SPARK_HOME'] = 'E:\spark\spark-3.2.0-bin-hadoop3.2'
# os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jdk1.8.0_311'
# os.environ['HADOOP_HOME'] = 'C:\hadoop'

import findspark
findspark.init()

# import necessary packages
import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.sql.functions import desc
from pyspark.sql import SparkSession
from pyspark.sql import Row
import sys
import requests


# create spark configuration
conf = SparkConf()
conf.setAppName("big_data_project_covid19_sentiment")

# create spark context with the above configuration
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

# initiate the StreamingContext with 10 second batch interval
ssc = StreamingContext(sc, 10)

# setting a checkpoint to allow RDD recovery
ssc.checkpoint("checkpoint_big_data_project_covid19_sentiment")

# initiate streaming text from a TCP (socket) source:
socket_stream = ssc.socketTextStream("127.0.0.1", 4444)

def aggregate_tags_count(new_values, total_sum):
    return sum(new_values) + (total_sum or 0)

def send_df_to_dashboard(df):
    # extract the hashtags from dataframe and convert them into array
    top_tags = [str(t.hashtag) for t in df.select("hashtag").collect()]
    # extract the counts from dataframe and convert them into array
    tags_count = [p.hashtag_count for p in df.select("hashtag_count").collect()]
    # initialize and send the data through REST API
    url = 'http://localhost:5000/updateData'
    request_data = {'label': str(top_tags), 'data': str(tags_count)}
    response = requests.post(url, data=request_data)

def get_sql_context_instance(spark_context):
    if ('sqlContextSingletonInstance' not in globals()):
        globals()['sqlContextSingletonInstance'] = SparkSession.builder.getOrCreate()
    return globals()['sqlContextSingletonInstance']

def process_rdd(time, rdd):
    print("----------- %s -----------" % str(time))
    try:
        # Get spark sql singleton context from the current context
        sql_context = get_sql_context_instance(rdd.context)
        # convert the RDD to Row RDD
        row_rdd = rdd.map(lambda w: Row(hashtag=w[0], hashtag_count=w[1]))
        # create a DF from the Row RDD
        hashtags_df = sql_context.createDataFrame(row_rdd)
        # Register the dataframe as table
        hashtags_df.createOrReplaceTempView("hashtags")
        # get the top 10 hashtags from the table using SQL and print them
        hashtag_counts_df = sql_context.sql("select hashtag, hashtag_count from hashtags order by hashtag_count desc limit 10")
        hashtag_counts_df.show()
        # call this method to prepare top 10 hashtags DF and send them
        send_df_to_dashboard(hashtag_counts_df)
    except:
        e = sys.exc_info()[0]
        print("Error: %s" % e)

# split each tweet into words
words = socket_stream.flatMap(lambda line: line.split(" "))
# filter the words to get only hashtags, lower case the word and then map each hashtag to be a pair of (hashtag,1)
hashtags = words.filter(lambda w: '#' in w).map(lambda x: (x.lower(), 1))
# adding the count of each hashtag to its last count
tags_totals = hashtags.updateStateByKey(aggregate_tags_count)
# do processing for each RDD generated in each interval
tags_totals.foreachRDD(process_rdd)

# start the streaming computation
ssc.start()
# wait for the streaming to finish
ssc.awaitTermination(900)