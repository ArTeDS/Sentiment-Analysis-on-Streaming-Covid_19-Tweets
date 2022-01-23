# Sentiment-Analysis-on-Streaming-Covid_19-Tweets

**Semester project for my MSc in Data Science, Big Data course**  

![img1](https://user-images.githubusercontent.com/72740595/150700030-5facc46a-fb92-4c28-acb4-efe04b0171bd.jpg)  


### Contributors  

[Aris Terzidis](https://github.com/ArTeDS) and [Nick Fritzalas](https://github.com/NickFritzalas)

<br>

## Motivation  

Covid-19 has risen various reactions and arguments regarding several aspects of the pandemic
(e.g. vaccinations, the validity of the virus). Nowadays, social media platforms are a basic way of
expressing opinions and sentiments towards a subject and especially under the pandemic where
physical contact has been minimized. This creates a huge and constant flow of relevant data,
which need to be analyzed.

For example, depending on the news feed, the audiences’ attitude and sentiments may swift.
This results into the need of analyzing this attitude-sentiment fluctuation. Such an analysis is useful
in many ways. For instance, governments might be interested in the opinions, attitudes, and
sentiments of the public, after the announcement of a relevant policy.
<br>

## Project Objectives (Hypothesis)  

What is the general public consensus towards the pandemic and related news around the world.

## Data Sources  
  - Twitter will be the data source - Streaming data
  - Text messages directly from Twitter’s feed with hashtags such as covid, coronavirus etc
  - Covid-19 Tweets Dataset to pretrain a classifier

## Big Data Dimensions 
  - Volume – Thousands of tweets per minute
  - Velocity – Increased flow depending on the news
  - Veracity – Depending on the reliability of tweets’ source
  - Value – Critical information from the data can greatly help in various ways

## Solution Overview 
  - Sentiment analysis via Machine Learning and NLP.
  - Collecting tweets from the Twitter API in a streaming manner, storing and processing them
  with SPARK
  - An ML model will be trained on a labeled dataset after experimentation for creating a high
  performing algorithm
  - The pretrained model will be deployed in combination with SPARK, on real time data  

![img3](https://user-images.githubusercontent.com/72740595/150700369-a8322021-56c6-49c9-a4dd-e9792f0ea9b3.png)  

## Tools-Libraries  
  - Twitter API
  - Spark
  - Sklearn
  - Keras – Tensorflow
  - Nltk, pandas, numpy etc.

<br>

## In this project we have created the following  
1.  A program that does sentiment analysis on a live stream of tweets based in the keyword **covid*** and storing the findings in a file
2.  A program that counts the most popular hashtags in the above tweeter stream and ploting the count in a real time dashboard
3.  A program that classifies the tweets as fake or real, based on a classifier that we have pretrained with a tweeter dataset  
4.  Data analysis for our data  

<br>

![img2](https://user-images.githubusercontent.com/72740595/150700093-c7929be6-c810-4888-a724-66a0345b4ffe.png)


## References  

https://github.com/stamatelou/twitter_sentiment_analysis  
https://www.toptal.com/apache/apache-spark-streaming-twitter  
https://boundingbox.klokantech.com/  
https://developer.twitter.com/en/docs/tutorials/filtering-tweets-by-location  
