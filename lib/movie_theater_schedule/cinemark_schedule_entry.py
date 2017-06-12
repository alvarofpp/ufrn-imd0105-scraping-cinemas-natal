import requests
from bs4 import BeautifulSoup

from .movie_theater_schedule_entry import MovieTheaterScheduleEntry

class CinemarkScheduleEntry(MovieTheaterScheduleEntry):
    def __init__(self, base_tag, theater_name):
        MovieTheaterScheduleEntry.__init__(self, base_tag, theater_name)

    @property
    def times_tags(self):
        return self.base_tag.select('ul.theater-times > li')

    @property
    def category(self):
        category = ''
        if(self.time_tag.find('span', { 'class' : 'label-leg' })):
            category = 'Legendado'
        if(self.time_tag.find('span', { 'class' : 'label-dub' })):
            category = 'Dublado'
        if(self.time_tag.find('span', { 'class' : 'label-orig' })):
            category = 'Original'
        return category

    @property
    def content_rating(self):
        movie_response = requests.get(self.movie_url)
        movie_soup = BeautifulSoup(movie_response.content, 'html.parser')
        detail_items = movie_soup.find_all('div', { 'class' : 'detail-title' })

        has_content_rating_data = lambda tag : 'Classificação' in tag.select('strong')[0].text

        content_rating_tag = [item for item in detail_items if has_content_rating_data(item)][0]
        return content_rating_tag.get_text().split('Classificação: ')[1].strip()

    @property
    def movie_theater(self):
        return self.theater_name

    @property
    def movie_url(self):
        title_tag = self.base_tag.select('h3.title > a')[0]
        return 'https://www.cinemark.com.br' + title_tag.get('href')

    @property
    def room(self):
        return self.time_tag.find('span', { 'class' : 'times-auditorium' }).text

    @property
    def schedules(self):
        schedules_tags = self.time_tag.find('ul', { 'class' : 'times-options' }).select('li > span')
        return ' / '.join([s.text for s in schedules_tags])

    @property
    def tags(self):
        tags = []
        if(self.time_tag.find('span', { 'class' : 'label-dbox' })):
            tags.append('DBOX')
        if(self.time_tag.find('span', { 'class' : 'label-3d' })):
            tags.append('3D')
        return ' / '.join(tags)

    @property
    def title(self):
        return self.base_tag.select('h3.title > a')[0].text

    def set_time_tag(self, time_tag):
        self.time_tag = time_tag
