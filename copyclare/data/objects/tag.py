"""
Contributors: Adi Bozzhanov

"""

class Tag:
    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __repr__(self):
        return f"<Tag: {self.tag_name}>"

    def get_sql_tuple(self):
        return (self.tag_name, )
