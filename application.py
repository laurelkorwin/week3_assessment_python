from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Show application form and collect user input"""

    return render_template("application-form-2.html")


@app.route("/application", methods=['POST'])
def show_application():
    """Show application with user input collected from form"""

    print "I'm in the application!!!"

    first_name = request.form.get('first_name')
    print first_name
    last_name = request.form.get('last_name')
    print last_name
    desired_role = request.form.get('desired_role')
    print desired_role
    salary = request.form.get('salary')
    print salary
    # return "My name is {} {} and I want to be a {} getting paid {}".format(first_name, last_name, desired_role, salary)

    return render_template("applicationresponse2.html", first_name=first_name, last_name=last_name, desired_role=desired_role, salary=salary)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
