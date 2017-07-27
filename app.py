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


@app.route('/edit/<int:tweet_id>', methods=['GET', 'POST'])
def edit_tweet(tweet_id):
    # RETRIEVE TWEET THAT HAVE id=tweet_id FROM THE DATABASE
    tweet = session.query(Tweet).filter_by(id=tweet_id).first()
    if request.method == 'GET':
        return render_template("edit_tweet.html", tweet=tweet)
    else:
      # read form data
      new_text          = request.form.get('text')
      new_picture_url   = request.form.get('picture_url')
      new_show_location = request.form.get('show_location')
      new_location      = request.form.get('location')

      # MISSING CODE HERE FOR UPDATING THE TWEET
      tweet.text=new_text
      tweet.picture_url=new_picture_url
      tweet.show_location=new_show_location
      tweet.location=new_location
      # redirect user to the page that views all tweets
      return redirect(url_for('my_feed'))


@app.route('/delete/<int:tweet_id>', methods=['GET', 'POST'])
def delete_tweet(tweet_id):
    tweet = session.query(Tweet).filter_by(id=tweet_id).first()# RETRIEVE TWEET THAT HAVE id=tweet_id FROM THE DATABASE
    return render_template('delete_tweet.html', tweet=tweet)