# Tweet @MEET Lab 1: Creating HTML templates

### 1. Intro
In this lab, we are going to create the different webpages in the Tweet @MEET web app.
Our main focus will be to make sure that the basic functionalities of each of the pages work *except for the links and the style*.
We will take care of these two points in one of the next lab.

### 2. Get familiar with the app

- Open the app folder <i>y2s17-d4-meet_tweets</i> and get familiar with the HTML Templates.

We have created 4 HTML files:
* `my_feed.html`
* `add_tweet.html`
* `edit_tweet.html`
* `delete_tweet.html`

Some of the templates are incomplete, let's fix them with the following exercises

### 3. Exercises
#### Exercise 1

In `add_tweet.html`, we've created a form but there's nothing inside. Please add the following input fields inside the form:
* A textarea, with `name="text"`, to enter the tweet's text (hint: textarea is its own tag)
* A text field, with `name="picture_url"`, to add a picture if needed. 
* A checkbox, with `name="show_location"`, `value="true"` and that is checked by default.
* A text field, with `name="location"` to enter the location.
* A submit button.

#### Exercise 2

Switch driver.
In `edit_tweet.html`, there is again an incomplete form that you need to add inputs to. 
Add the same inputs as for `add_tweet.html`. However, this time, we'll need to make some minor edits:

* For the textarea field, make the default text say `"{{ tweet.text }}"` by adding it between the `textarea` tags.
* For the picture_url text field, make the default text say `"{{ tweet.picture_url }}"` using the `value` attribute.
* For the location field, make the default value `"{{ tweet.location }}"` (again, use the HTML attribute `value`).

By adding these specific values, the form will be automatically filled out by the tweet's informations.
We will take care of the checkbox in one of the next labs.
