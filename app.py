from data import app, db
from data.models import Admin

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        new_admin = Admin(username='jayphil', email='nyameget@gmail.com' )
        new_admin.password = '1567Tay*'
        db.session.add(new_admin)
        new_admin_ = Admin(username='desmond', email='desmondeshun134@gmail.com' )
        new_admin_.password = 'desmond134'
        db.session.add(new_admin_)
        db.session.commit()
    app.run(debug=True)
