MEET Friends Lab 4: Handling forms
----------------------------------

**Important:** This lab relies on successfully completed code for [MEET Friends Lab 3](https://github.com/meet-projects/y2-meet-friends/blob/master/lab3.md). You should have a folder `y2-meet-friends`. Also, after running your Flask app, remember that you go to your Flask website by going to: `http://127.0.0.1:5000/`

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

Modify your `edit_friend` function so that it says:

```
@app.route("/edit/<int:person_id>", methods=['GET', 'POST'])
def edit_friend(person_id):
    friend = session.query(Person).filter_by(id=person_id).first()
    if request.method == 'GET':
        return render_template("edit_friend.html", friend=friend)
    else:
        # read form data
        new_name = request.form['name']
        new_gender = request.form['gender']
        new_nationality = request.form['nationality']
        new_hometown = request.form['hometown']
        
        # MISSING CODE HERE FOR UPDATING THE FRIEND
        
        # redirect user to the page that views all friends
        return redirect(url_for('view_my_friends'))
```

Add code where it says `# MISSING CODE HERE FOR UPDATING THE FRIEND` that updates the database, changing the friend to have the new name, gender, nationality, and hometown provided.

#### Exercise 2

Modify your code for `add_friend` and `delete_friend` so that they can add and delete friends from the database and then redirect the user back to the page that views all friends.
