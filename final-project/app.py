from flask import *
from flask import Flask, render_template, request, json
from models.edu import Edu
from models.user_db import Acc
from mlab import mlab_connect
from convert import convert
app = Flask(__name__)


mlab_connect()
app.config['SECRET_KEY'] = 'asdasd asas asqafkigk'

mlab_connect()


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/admin')
def admin():
    if 'logged_in' in session and session['logged_in'] == True:
        return render_template('admin.html', edus = Edu.objects())
    else:
        return redirect(url_for('admin_login'))

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.route('/delete/<edu_id>')
def delete(edu_id):
    edu = Edu.objects().with_id(edu_id)
    if edu is None:
        return "Not found"
    else:
        edu.delete()
        return redirect(url_for('admin'))

@app.route('/new_edu', methods = ['GET', 'POST'])
def new_edu():
    if request.method == "GET":
        return render_template('new_edu.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        search_name = convert(name).lower()
        phone = form['phone']
        address = form['address']
        city = form['city']
        district = form['district']
        section = form['section']
        info = form['info']
        email = form['email']
        fee = form['fee']
        logo = form['logo']
        photo1 = form['photo1']
        photo2 = form['photo2']
        photo3 = form['photo3']
        website = form['website']
        hot = form['hot']

        new_edu = Edu(name = name,
                    search_name = search_name,
                    phone = phone,
                    city = city,
                    district = district,
                    section = section,
                    info = info,
                    email = email,
                    fee = fee,
                    logo = logo,
                    photo1 = photo1,
                    photo2 = photo2,
                    photo3 = photo3,
                    website = website,
                    hot = hot == '1')

        new_edu.save()
        flash("Submitted!")
        return redirect(url_for('admin'))

@app.route('/edit/<edu_id>', methods = ['GET', 'POST'])
def edit_edu(edu_id):
    edu = Edu.objects().with_id(edu_id)
    if edu is None:
        return "Not found"
    else:
        if request.method == "GET":
            return render_template('edit_edu.html', edu = edu)
        elif request.method == "POST":
            form = request.form
            name = form['name']
            search_name = convert(name).lower()
            phone = form['phone']
            address = form['address']
            city = form['city']
            district = form['district']
            section = form['section']
            info = form['info']
            email = form['email']
            fee = form['fee']
            logo = form['logo']
            photo1 = form['photo1']
            photo2 = form['photo2']
            photo3 = form['photo3']
            website = form['website']
            hot = form['hot']

            edu.update(set__name = name,
                        search_name = search_name,
                        set__phone = phone,
                        set__address = address,
                        set__city = city,
                        set__district = district,
                        set__section = section,
                        set__info = info,
                        set__email = email,
                        set__fee = fee,
                        set__logo = logo,
                        set__photo1 = photo1,
                        set__photo2 = photo2,
                        set__photo3 = photo3,
                        set__website = website,
                        set__hot = hot == '1')
            edu.reload()

            return redirect(url_for('admin'))

@app.route('/search/<edu_search>', methods=['GET', 'POST'])
def search(edu_search):
    if request.method == 'GET':
        edus = Edu.objects(search_name__contains=edu_search)
        return render_template('search.html', edus=edus, edu_search = edu_search)
    if request.method == 'POST':
        edu_search = request.form['search']
        if edu_search == '':
            return  redirect(url_for('filter_both'))
        else:
            return  redirect(url_for('search', edu_search = convert(edu_search).lower()))

@app.route('/center/<edu_id>', methods=['GET', 'POST'])
def center(edu_id):
    if request.method == 'GET':
        edu = Edu.objects().with_id(edu_id)
        return render_template('center.html', edu = edu)
    if request.method == 'POST':
        edu_search = request.form['search']
        if edu_search == '':
            return  redirect(url_for('filter_both'))
        else:
            return  redirect(url_for('search', edu_search = convert(edu_search).lower()))


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('homepage.html', edus = Edu.objects())
    if request.method == 'POST':
        edu_search = request.form['search']
        if edu_search == '':
            return  redirect(url_for('filter_both'))
        else:
            return  redirect(url_for('search', edu_search = convert(edu_search).lower()))


@app.route('/filter')
def filter_both():
    edus = Edu.objects()
    return render_template('filter.html', edus=edus)

@app.route('/login/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        # check trang thai log in
            # neu da login thi redirect ve 1 trang mong muon
            # neu chua thi render_template('login.html')
        # if 'logged_in' in session:
        #     return redirect(url_for("home"))
        return render_template('login.html')
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            if 'logged_in' in session and session['logged_in'] == True:
                return render_template('admin.html', edus = Edu.objects())
        else:
            return render_template('login.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def client_login():
    if request.method == 'GET':
        return render_template('client_login.html')
    if request.method == 'POST':
        form = request.form
        user_id = form['username']
        user_pass = form['password']
        accounts = Acc.objects(role=False)
        for acc in accounts:
            if user_id == acc['acc_id'] and user_pass == acc['acc_pass']:
                return redirect(url_for('home'))
        return redirect(url_for('client_login'))

@app.route('/signup',methods=['GET','POST'])
def signUp():
    if request.method == 'GET':
        # check trang thai log in
            # neu da login thi redirect ve 1 trang mong muon
            # neu chua thi render_template('login.html')
        # if 'logged_in' in session:
        #     return redirect(url_for("home"))
        return render_template('sign_up.html')
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        new_account = Acc(acc_id = username,
                          acc_pass = password,
                          role = False,
                          rate = [])
        new_account.save()
        return redirect(url_for('client_login'))


# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('You were logged out')
#     return redirect(url_for("home"))

if __name__ == "__main__":
  app.run(debug=True)
