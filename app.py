from flask import Flask, redirect, render_template
import sys
import config as c
from mock import mock_data as mdata
import random
from db import db, Expense
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://' \
    f'{os.environ.get("EXTRAAPP_MYSQL_USER", c.mysql_user)}:' \
    f'{os.environ.get("EXTRAAPP_MYSQL_PASS", c.mysql_pass)}@' \
    f'{os.environ.get("EXTRAAPP_MYSQL_HOST", c.mysql_host)}/' \
    f'{os.environ.get("EXTRAAPP_MYSQL_DB", c.mysql_db)}'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 28800
app.config['SQLALCHEMY_POOL_SIZE'] = 20
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
with app.app_context():
    db.init_app(app)
    db.create_all()


@app.route("/")
def index():
    to_out = []
    for expense in Expense.query.all():
        to_out.append({d.name: getattr(expense, d.name) for d in expense.__table__.columns})
    return render_template('base.html', data=to_out)


@app.route("/generate", methods=['POST'])
def generate():
    catid = random.randrange(0, len(mdata)-1)
    expid = random.randrange(0, len(mdata[catid]['list'])-1)
    try:
        db.session.add(Expense(category=mdata[catid]['cat'], amount=random.randrange(100,500),
                               comment=mdata[catid]['list'][expid]))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f'DB ERROR : {str(e)}', file=sys.stderr)
    return redirect('/')


if __name__ == "__main__":
    app.run(host=os.environ.get("EXTRAAPP_IP", c.app_ip),
            port=os.environ.get("EXTRAAPP_PORT", c.app_port),
            debug=os.environ.get("EXTRAAPP_DEBUG_MODE", c.app_debug_mode))
