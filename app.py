from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from datetime import date
from os import getenv
from dotenv import load_dotenv
from blog_post import BlogPost, db
from post_form import PostForm, ckeditor

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
Bootstrap5(app)
ckeditor.init_app(app=app)
# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new_post', methods=['GET', 'POST'])
def creat_post():
    form = PostForm()
    if form.validate_on_submit():
        post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=date.today().strftime('%B %d, %Y'),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data,
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    h1 = 'New Post'
    return render_template('make-post.html', form=form, h1=h1)


# TODO: edit_post() to change an existing blog post
@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    form = PostForm(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        body=post.body,
        img_url=post.img_url,
    )

    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.body = form.body.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))

    h1 = 'Edit Post'
    return render_template('make-post.html', form=form, h1=h1)


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
