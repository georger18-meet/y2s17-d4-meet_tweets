# Tweet @MEET Lab 4: Fixing some broken links

### 1. Exercises

#### Exercise 1

We added new routes to `app.py` but forgot some code.

In `edit_tweet()` and `delete_tweet()`, add the query that allows us to retrieve the tweet with `id=tweet_id`. Hint: use `filter_by`


#### Exercise 2

In `app.py`, change the routes `"BROKEN-ROUTE-FOR-YOU-TO-FIX"` so that "/edit/5/" goes to the page for editing the tweet with `tweet_id=5`, and "/delete/2/" goes to the page for deleting the tweet with `tweet_id=2`, etc. Your code should work for any id, not just 2 or 5!

Check your work by running the next command and going to http://127.0.0.1:5000/:
```
flask run
```

#### Exercise 3

Go through all four HTML files and fix all the broken links in the `<a>` tags. We highly recommend that you modify the HTML files in the following order:

1. `my_feed.html`
2. `add_tweet.html`
3. `edit_tweet.html`
4. `delete_tweet.html`

After doing this exercise, all the links should work but the submit buttons should still be broken. For the "add tweet" and "edit tweet" pages, the "Cancel" link should go back to the webpage that views all the tweets. For the "delete tweet" page, the "Cancel" link should go back to the "edit tweet" page.
