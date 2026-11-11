from flask import Flask

app = Flask(__name__)

# Car models currently available in the Flatiron Cars fleet.
existing_models = ["Beedle", "Crossroads", "M2", "Panique"]


@app.route("/")
def index():
    """Return the welcome message for the default route."""
    return "Welcome to Flatiron Cars"


@app.route("/<model>")
def show_model(model):
    """Return whether the requested model exists in the fleet."""
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"

    return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(port=5555, debug=True)