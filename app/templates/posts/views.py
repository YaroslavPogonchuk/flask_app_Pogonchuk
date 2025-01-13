from . import post_bp
from flask import render_template, abort, flash, redirect, url_for, session
from .forms import PostForm
from .functions import read_posts, write_posts, get_new_id




@post_bp.route('/')
def get_posts():
    posts = read_posts()
    return render_template("posts.html", posts=posts)


@post_bp.route('/<int:id>')
def detail_post(id):
    posts = read_posts()
    post = next((post for post in posts if post["id"] == id), None)

    if post is None:
        abort(404)

    return render_template("detail_post.html", post=post)


@post_bp.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = {
            "id": get_new_id(),
            "title": form.title.data,
            "content": form.content.data,
            "category": form.category.data,
            "is_active": form.is_active.data,
            "publication_date": form.publish_date.data.strftime('%Y-%m-%d'),
            "author": session.get('username', 'Unknown')
        }

        posts = read_posts()
        posts.append(new_post)
        write_posts(posts)

        flash('Post added successfully!', 'success')
        return redirect(url_for('posts.get_posts'))

    return render_template('add_post.html', form=form)


