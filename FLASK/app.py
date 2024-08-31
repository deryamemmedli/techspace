from flask import Flask, render_template

app = Flask(__name__)
# app = Flask(__name__,template_folder='htmls')
# app = Flask('app')



blog_list = [
        {
            'id': 1,
            'title': 'Blog 1',
            'content': 'This is the content of Blog 1',
            'author': 'Author 1'
        },
        {
            'id': 2,
            'title': 'Blog 2' ,
            'content': 'This is the content of Blog 2',
            'author': 'Author 2'
        },
        {
            'id': 3,
            'title': 'Blog 3',
            'content': 'This is the content of Blog 3',
            'author': 'Author 3'
        },
        {
            'id': 4,
            'title': 'Blog 4',
            'content': 'This is the content of Blog 4',
            'author': 'Author 4'
        }
    ]


@app.route('/')
@app.route('/home/')
def index():
    return render_template('index.html')



@app.route('/about/')
def about():
    return 'About Page!'


@app.route('/blogs/')
def blogs():
    return render_template('blog.html', blogs=blog_list, page_name='Blogs')


@app.route('/blogs/<int:blog_id>/')
def blog_detail(blog_id):
    # if blog_id <= len(blog_list) and blog_id > 0:
    return blog_list[blog_id-1]
    # else:
    #     return 'No blog found'



# @app.route('/blogs/<string:blog_id>/')
# def blog_detail_with_string(blog_id):
#     return f"Blog with id {blog_id}"
   

# import elemek olmasin deye
if __name__ == '__main__':
    app.run(debug=True)





