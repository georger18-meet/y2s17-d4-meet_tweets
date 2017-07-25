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
    tweets = [] # CHANGE THIS TO READ YOUR TWEETS FROM THE DATABASE
    return render_template('my_feed.html', tweets=tweets)


@app.route('/add', methods=['GET', 'POST'])
def add_tweet():
    return render_template('add_tweet.html')
