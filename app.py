from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
import sys

# SQLAlchemy stuff
from model import Base, Tweet
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///tweetlab.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def my_feed():
    tweets = session.query(Tweet).all()
    return render_template('my_feed.html', tweets=tweets)


@app.route('/add', methods=['GET', 'POST'])
def add_tweet():
    return render_template('add_tweet.html')


@app.route('/BROKEN-ROUTE-FOR-YOU-TO-FIX')
def edit_tweet(tweet_id):
    tweet = # RETRIEVE TWEET THAT HAVE id=tweet_id FROM THE DATABASE
    return render_template('edit_tweet.html', tweet=tweet)


@app.route('/BROKEN-ROUTE-FOR-YOU-TO-FIX')
def delete_tweet(tweet_id):
    if request.method == 'GET':
      tweet = # RETRIEVE TWEET THAT HAVE id=tweet_id FROM THE DATABASE
      return render_template('delete_tweet.html', tweet=tweet)
    else:
      # DELETE TWEET THAT HAVE id=tweet_id FROM THE DATABASE
      return redirect(url_for('my_feed')) 