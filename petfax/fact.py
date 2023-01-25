from flask import ( Blueprint, render_template ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new_fact')
def new(): 
    return render_template('facts/new_fact.html')