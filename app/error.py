from app import app
from flask import render_template

@app.errorhandler(404)
def four_ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('404.html'), 404
