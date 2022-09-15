class Comments:
    def __init__(self, post_id=0, commenter_name='', comment='', pk=0):
        self.post_id = post_id
        self.commenter_name = commenter_name
        self.comment = comment
        self.pk = pk

    def load_as_dict(self, path):
        comment_dict = {
            "post_id": self.post_id,
            "commenter_name": self.commenter_name,
            "comment": self.comment,
            "pk": self.pk
        }
        return comment_dict

    def __repr__(self):
        return self.comment