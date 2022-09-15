import logging
from flask import Flask, render_template, request, jsonify
from posts.posts_dao import PostsDAO
from comments.comments_dao import CommentDAO
PATH = 'data/posts.json'
posts = PostsDAO(PATH)
app = Flask(__name__)
comments = CommentDAO('data/comments.json')
app.config['JSON_AS_ASCII'] = False
logging.basicConfig(filename="api.log", level=logging.INFO)


@app.route('/')
def main_page():
    all_posts = posts.get_all()
    return render_template('index.html', posts=all_posts)


@app.route('/posts/<int:postid>')
def open_post(postid):
    post = posts.get_by_pk(postid)
    try:
        comment = comments.get_by_post_id(postid)
        comment_len = len(comment)
    except ValueError:
        comment = []
        return render_template('post.html', post=post, comment=comment)
    return render_template('post.html', post=post, comment=comment, comment_len=comment_len)


@app.route('/search')
def search_post():
    s = request.args['s']
    key_posts = posts.search_for_posts(s)
    return render_template('search.html', key_posts=key_posts)


@app.route('/users/<username>')
def user_posts(username):
    try:
        user_posts = posts.get_posts_by_user(username)
    except ValueError:
        user_posts = []
        return render_template('user-feed.html', posts=user_posts)
    return render_template('user-feed.html', posts=user_posts)


@app.route('/api/posts', methods=["GET"])
def read_posts():
    all_posts = posts.get_all()
    logging.info("Запрошен список постов")
    return jsonify([post.load_as_dict() for post in all_posts])


@app.route('/api/posts/<int:post_id>', methods=["GET"])
def read_post(post_id):
    post = posts.get_by_pk(post_id)
    logging.info(f"Запрошен пост по номеру {post_id}")
    return jsonify(post.load_as_dict())


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify(error=str(e)), 500


if __name__ == "__main__":
    app.run()
