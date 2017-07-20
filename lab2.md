MEET Friends Lab 2: Building the Flask backend for viewing friends
------------------------------------------------------------------

**Important:** This lab relies on successfully completed code for [MEET Tweets Lab 1](https://github.com/meet-projects/y2s17-d4-meet_tweets/blob/master/lab1.md). You should have a folder `y2s17-d4-meet_tweets`.

#### Exercise 1

In `templates/my_feed.html`, notice that we've actually omitted something important: we need to have a for loop that goes through all the tweets! Modify the file so that the table row (not the table header but the row that actually has columns that say `{{ tweet.favorite_count }}`, `{{ tweet.location }}`, etc) is within a for loop. Remember that for how Flask templates work, the end of a for loop has to use the syntax `{% endfor %}`.

#### Exercise 2

In terminal, go to the folder `y2s27-d4-meet_tweets`, enter the virtual environment with `virtualenv venv', and execute the command `flask run`. This should run without error. Leave this continuously running (it's a server!).

Now open your browser and go to `http://127.0.0.1:5000/` (this is the default URL for where Flask runs your web app) and you should see the content that is in `my_feed.html` (but notice how `my_feed.html` doesn't appear anywhere in the URL!). Similarly, if you go to `http://127.0.0.1:5000/add` in your browser, you should see the content that is in `add_tweet.html`.

#### Exercise 3

We've already imported the relevant portions of SQLAlchemy for you into the Python file `app.py`.

In the function `my_feed()`, change the first line so that it actually reads all the tweets from the database into the variable `tweets`. After completing this exercise, when you go to `http://127.0.0.1:5000/` in your web browser, you should see a list of all the tweets you added to the database earlier.
