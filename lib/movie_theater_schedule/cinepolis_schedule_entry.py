import re
from .movie_theater_schedule_entry import MovieTheaterScheduleEntry

class CinepolisScheduleEntry(MovieTheaterScheduleEntry):
    def __init__(self, base_tag, theater_name):
        MovieTheaterScheduleEntry.__init__(self, base_tag, theater_name)

    @property
    def category(self):
        return self.base_tag.find("td", { "class" : "horarios" }).find('span').get('aria-label')

    @property
    def content_rating(self):
        return self.base_tag.find_all('td')[2].find('img').get('alt')

    @property
    def movie_theater(self):
        return self.theater_name

    @property
    def movie_url(self):
        tag = self.base_tag.find_all(href=re.compile('http://www.cinepolis.com.br/filmes/filme.php'))[0]
        return tag.get('href').split('&cc=')[0]

    @property
    def room(self):
        return self.base_tag.find_all('td')[0].text

    @property
    def schedules(self):
        schedules_tags = self.base_tag.find("td", { "class" : "horarios" }).select("span + span, a")
        return ' / '.join([s.text for s in schedules_tags])

    @property
    def tags(self):
        tags = []
        if(self.base_tag.find("a", { "class" : "icovip" })):
                tags.append('VIP')
        if(self.base_tag.find("a", { "class" : "icomacroxe" })):
                tags.append('MacroXE')
        if(self.base_tag.find("a", { "class" : "ico3d" })):
                tags.append('3D')
        return ' / '.join(tags)

    @property
    def title(self):
        tag = self.base_tag.find_all(href=re.compile('http://www.cinepolis.com.br/filmes/filme.php'))[0]
        return tag.text
