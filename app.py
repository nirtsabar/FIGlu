import os
import time
from datetime import datetime

from flask import Flask, render_template, request, flash, session, g, redirect, url_for

import auth
import db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        EXPLAIN_TEMPLATE_LOADING=False,
        DATABASE=os.path.join(app.instance_path, 'FIGlu.sqlite'),
    )
    app.register_blueprint(auth.bp)

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

    @auth.login_required
    @app.route("/", methods=('GET', 'POST'))
    def home():
        auth.get_db()
        if request.method == 'POST':
            if g.user is None:
                return redirect(url_for('auth.login'))
            timestamp = datetime.now()
            username = session['username']
            print(username, ": ", request.form)
            glucose0 = request.form['glucose0']
            glucose1 = request.form['glucose1']
            glucose2 = request.form['glucose2']
            insulin0 = request.form['insulin0']
            insulin1 = request.form['insulin1']
            insulin_long = request.form['insulinLong']
            optimal_glucose = request.form['optimalGlucose']
            glucose_insulin_factor = request.form['glucose_Insulin_Factor']
            r_insulin0 = request.form['rInsulin0']
            r_insulin1 = request.form['rInsulin1']
            r_insulin2 = request.form['rInsulin2']
            comment = ""
            d_b = auth.get_db()
            error = None
            try:
                error = d_b.execute(
                    'INSERT INTO gluIns (username, sentTime, glucose0, glucose1, glucose2, insulin0, insulin1,'
                    ' insulinLong, optimalGlucose, glucose_Insulin_Factor, rInsulin0, rInsulin1,'
                    ' rInsulin2, comment) '
                    'VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                    (username, timestamp, glucose0, glucose1, glucose2, insulin0, insulin1,
                     insulin_long, optimal_glucose, glucose_insulin_factor, r_insulin0, r_insulin1,
                     r_insulin2, comment)
                )
            except:
                flash(error)
            else:
                d_b.commit()
        return render_template('index.html')

    @app.errorhandler(404)
    def not_found(error):
        return render_template('error.html'), 404

    db.init_app(app)

    return app


@auth.login_required  # content moved to create_app.home
def get_record():
    return


if __name__ == "__main__":
    IGlu_app = create_app()
    IGlu_app.run()
