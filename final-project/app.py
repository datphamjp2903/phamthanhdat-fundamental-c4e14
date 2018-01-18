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

@app.route('/filter/<city>/<section>', methods=['GET', 'POST'])
def filter_both(city, section):
    if request.method == 'GET':
        edus = Edu.objects(city=city, section=section)
        return render_template('filter.html', edus=edus)
    if request.method == 'POST':
        form = request.form
        city = form.get("city")
        section = form.get("section")
        return redirect(url_for('filter_both', city=city, section=section))

@app.route('/filter/0/<section>', methods=['GET', 'POST'])
def filter_section(section):
    if request.method == 'GET':
        edus = Edu.objects(section=section)
        return render_template('filter.html', edus=edus)
    if request.method == 'POST':
        form = request.form
        city = form.get("city")
        section = form.get("section")
        return redirect(url_for('filter_both', city=city, section=section))

@app.route('/filter/<city>/0', methods=['GET', 'POST'])
def filter_city(city):
    if request.method == 'GET':
        edus = Edu.objects(city=city)
        return render_template('filter.html', edus=edus)
    if request.method == 'POST':
        form = request.form
        city = form.get("city")
        section = form.get("section")
        return redirect(url_for('filter_both', city=city, section=section))


if __name__ == "__main__":
  app.run(debug=True)
