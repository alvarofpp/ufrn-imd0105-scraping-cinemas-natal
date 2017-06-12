import abc

class MovieTheaterScheduleEntry(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, base_tag, theater_name):
        self.base_tag = base_tag
        self.theater_name = theater_name

    @abc.abstractproperty
    def category(self):
        return 'set category property value'

    @abc.abstractproperty
    def content_rating(self):
        return 'set content_rating property value'

    @abc.abstractproperty
    def movie_theater(self):
        return 'set movie_theater property value'

    @abc.abstractproperty
    def movie_url(self):
        return 'set movie_url property value'

    @abc.abstractproperty
    def room(self):
        return 'set room property value'

    @abc.abstractproperty
    def schedules(self):
        return 'set schedules property value'

    @abc.abstractproperty
    def tags(self):
        return 'set tags property value'

    @abc.abstractproperty
    def title(self):
        return 'set title property value'

    def get_dict(self):
        return {
            'category': self.category,
            'content_rating': self.content_rating,
            'movie_theater': self.movie_theater,
            'movie_url': self.movie_url,
            'room': self.room,
            'schedules': self.schedules,
            'tags': self.tags,
            'title': self.title
        }
