import json
from comments.comment_class import Comments


class CommentDAO:
    def __init__(self, path):
        self.path = path

    def _load_data(self):
        with open(self.path, encoding='utf-8') as file:
            data = json.load(file)
            instances = [Comments(**post_data) for post_data in data]
        return instances

    def get_all(self):
        """returns all the comments"""
        data = self._load_data()
        return data

    def get_by_post_id(self, post_id):
        """returns post comments by id"""
        comments_list = []
        is_exists = False
        for comment in self.get_all():
            if comment.post_id == post_id:
                is_exists = True
                comments_list.append(comment)
        if not is_exists:
                raise ValueError
        return comments_list



