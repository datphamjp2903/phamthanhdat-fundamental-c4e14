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
    return render_template('admin.html', edus = Edu.objects())

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
                            photo1 = photo1,
                            photo2 = photo2,
                            photo3 = photo3,
                            website = website)
        new_edu.save()
        flash("Submitted!")
        return redirect(url_for('admin'))

@app.route('/search/<edu_search>', methods=['GET', 'POST'])
def search(edu_search):
    if request.method == 'GET':
        edus = Edu.objects(search_name__contains=edu_search)
        return render_template('search.html', edus=edus)
    if request.method == 'POST':
        edu_search = request.form['search']
        return redirect(url_for('search', edu_search=convert(edu_search).lower()))

@app.route('/center')
def center():
    return render_template('center.html')

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


if __name__ == "__main__":
  app.run(debug=True)
