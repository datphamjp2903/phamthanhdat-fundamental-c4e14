from flask import *
from models.edu import Edu

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
        phone = form['phone']
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

        new_edu = Edu(name = name,
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
                            website = website)
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
            phone = form['phone']
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

            edu.update(set__name = name,
                        set__phone = phone,
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
                        set__website = website)
            edu.reload()

            return redirect(url_for('admin'))

@app.route('/search/<edu_search>', methods=['GET', 'POST'])
def search(edu_search):
    if request.method == 'GET':
        edus = Edu.objects(search_name__contains=edu_search)
        return render_template('search.html', edus=edus)
    if request.method == 'POST':
        edu_search = request.form['search']
        return redirect(url_for('search', edu_search=convert(edu_search).lower()))

@app.route('/center/<edu_id>')
def center(edu_id):
    edu = Edu.objects().with_id(edu_id)
    return render_template('center.html', edu = edu)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('homepage.html')
    if request.method == 'POST':
        edu_search = request.form['search']
        return  redirect(url_for('search', edu_search = edu_search))

@app.route('/filter')
def filter_both():
    edus = Edu.objects()
    return render_template('filter.html', edus=edus)

@app.route('/login/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('admin-login.html')
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return 'NOT FOUND'

if __name__ == "__main__":
  app.run(debug=True)
