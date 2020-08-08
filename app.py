from flask import Flask, redirect, url_for, render_template
import auth
import db
import os


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app


app = create_app()


app.register_blueprint(auth.bp)


@app.route("/")
def home():
    db.init_db()
    auth.get_db()
    return render_template("index.html", nav1='התחלה')


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


if __name__ == "__main__":
    app.run()
