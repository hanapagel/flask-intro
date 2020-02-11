"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


AWFULNESS = [
    'terrible', 'no-good', 'rotten', 'abominable', 'horrific', 'atrocious']

@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html>This is the Home Page!<a href="localhost:5000/hello">Hello</a></html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">

          How are you feeling?

          <label>Awesome</label>
          <input type="checkbox" name="compliment" value="awesome"</input>

          <label>Terrific</label>
          <input type="checkbox" name="compliment" value="terrific"</input>

          <label>Fantastic</label>
          <input type="checkbox" name="compliment" value="fantastic"</input>

          <label>Neato</label>
          <input type="checkbox" name="compliment" value="neato"</input>

          <input type="submit" value="Submit">

        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


# @app.route("/diss")
# def insult_person():
#     """Insult the user by name."""

#     player = request.args.get("person")

#     insult = choice(AWFULNESS)

#     return """
#     <!doctype html>
#     <html>
#         <head>
#             <title> Hello! </title>
#         </head>
#         <body>
#             Hi, {}! I think you're {}!
#         </body>
#     </html>
#     """.format(player, insult)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
