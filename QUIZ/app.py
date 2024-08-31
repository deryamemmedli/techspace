from flask import Flask, render_template
from models import db, Movie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


def setup_database(app):
    with app.app_context():
        db.create_all()
        if not Movie.query.first():
            movie_list = [
                Movie(title="The Shawshank Redemption", released="1994", director="Frank Darabont", genre="Drama"),
                Movie(title="Schindler's List", released="1993", director="Steven Spielberg", genre="Biography"),
                Movie(title="Forrest Gump", released="1994", director="Robert Zemeckis", genre="Drama")
            ]
            db.session.add_all(movie_list)
            db.session.commit()

setup_database(app)


@app.route('/movies/')
def movies():
    all_movies =Movie.query.all()
    return render_template('index.html', movies=all_movies)

@app.route('/movies/<int:movie_id>/')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('movie.html', movie=movie)
    

if __name__ == '__main__':
    app.run(debug=True)

