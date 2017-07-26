MEET Friends Lab 3: Fixing some broken links
--------------------------------------------

**Important:** This lab relies on successfully completed code for [MEET Friends Lab 2](https://github.com/meet-projects/y2-meet-friends/blob/master/lab2.md). You should have a folder `y2-meet-friends`. Also, after running your Flask app, remember that you go to your Flask website by going to: `http://127.0.0.1:5000/`

As a reminder, if you have not set up Python using the commands below, please do so now:

```
wget http://tinyurl.com/MEETpythonY2
source MEETpythonY2
```

If you have already run the code above but you've opened a new terminal window, please run:

```
source ~/y2-venv/bin/activate
```

#### Exercise 1

In `web_app.py`, add the following two functions:

```
@app.route('/BROKEN-ROUTE-FOR-YOU-TO-FIX')
def edit_friend(person_id):
    friend = session.query(Person).filter_by(id=person_id).first()
    return render_template('edit_friend.html', friend=friend)


@app.route('/BROKEN-ROUTE-FOR-YOU-TO-FIX')
def delete_friend(person_id):
    friend = session.query(Person).filter_by(id=person_id).first()
    return render_template('delete_friend.html', friend=friend)
```

Where it says "BROKEN-ROUTE-FOR-YOU-TO-FIX", please change the route so that "/edit/5/" goes to page for editing a friend with `person_id=5`, and "/delete/2/" goes to the page for deleting a friend with `person_id=2`, etc. Your code should work for any id, not just 2 or 5!

Check your work by going to http://127.0.0.1:5000/edit/4/. Does it load the right information?

#### Exercise 2

Go through all four HTML files and fix all the broken links in the `<a>` tags. We highly recommend that you modify the HTML files in the following order:

1. `view_my_friends.html`
2. `add_friend.html`
3. `edit_friend.html`
4. `delete_friend.html`

After doing this exercise, all the links should work but the submit buttons should still be broken. For the "add friend" and "edit friend" pages, the "Cancel" link should go back to the webpage that views all the friends. For the "delete friend" page, the "Cancel" link should go back to the "edit friend" page.
