import json
from posts.post_class import Post


class PostsDAO:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, encoding='utf-8') as file:
            data = json.load(file)
            instances = [Post(**post_data) for post_data in data]
        return instances

    def get_all(self):
        """returns all the posts"""
        data = self.load_data()
        return data

    def get_posts_by_user(self, user_name):
        """returns posts by username"""
        post_list = []
        is_exists = False
        for post in self.get_all():
            if post.poster_name == user_name:
                is_exists = True
                post_list.append(post)
        if not is_exists:
            raise ValueError
        return post_list

    def search_for_posts(self, query):
        """returns post list by the keyword"""
        post_list = []
        for post in self.get_all():
            if query in post.content:
                post_list.append(post)
            if query not in post.content:
                pass
        return post_list

    def get_by_pk(self, pk):
        """returns post by pk"""
        for post in self.get_all():
            if post.pk == pk:
                return post



