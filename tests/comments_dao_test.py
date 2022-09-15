import pytest
from comments.comments_dao import CommentDAO


@pytest.fixture()
def comment_dao():
    comments = CommentDAO("./data/comments.json")
    return comments


class TestCommentDAO:

    def test_get_all(self, comment_dao):
        comments = comment_dao.get_all()
        assert type(comments) == list, 'wrong data type'
        assert len(comments) > 0, 'empty list'

    def test_get_by_postid(self, comment_dao):
        comments = comment_dao.get_by_post_id(1)
        for comment in comments:
            assert comment.post_id == 1, 'wrong post id'
