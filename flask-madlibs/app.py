from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
"""starts server"""
app.config["SECRET_KEY"] = "madlib-key"
debug = DebugToolbarExtension(app)


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
)


@app.route("/")
def render_homepage():

    return render_template("homepage.html")


@app.route("/story")
def display_story():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adj = request.args["adjective"]
    drink = request.args["drink"]
    story = request.args["story"]

    return render_template("story.html", place=place, noun=noun, verb=verb, adj = adj, drink = drink, story = story)
