import pytest
from posts.posts_dao import PostsDAO


@pytest.fixture()
def posts_dao():
    posts = PostsDAO("./data/posts.json")
    return posts


class TestPostDAO:

    def test_get_all(self, posts_dao):
        posts = posts_dao.get_all()
        assert type(posts) == list, 'wrong data type'
        assert len(posts) > 0, 'empty list'

    def test_get_by_pk(self, posts_dao):
        post = posts_dao.get_by_pk(1)
        assert post.pk == 1, 'wrong pk'

    def test_get_by_user(self, posts_dao):
        posts = posts_dao.get_posts_by_user('leo')
        for post in posts:
            assert post.poster_name == 'leo'

    def test_search_post(self, posts_dao):
        posts = posts_dao.search_for_posts('тарелка')
        for post in posts:
            assert 'тарелка' in post.content, 'no keyword in post'



