import re

from .movie_theater_schedule import MovieTheaterSchedule
from .cinepolis_schedule_entry import CinepolisScheduleEntry

class CinepolisSchedule(MovieTheaterSchedule):
    def __init__(self, soup, theater_name):
        MovieTheaterSchedule.__init__(self, soup, theater_name)

    def __row_has_movie(self, row):
        return row.find(attrs={ 'data-order': re.compile('\w+') })

    def get_base_tag(self):
        return self.soup.find('table', { 'class' : 'tabelahorarios' })

    def get_entries_tags(self):
        rows = self.base_tag.find_all('tr')

        return [row for row in rows if self.__row_has_movie(row)]

    def parse_entries(self):
        for entry in self.entries_tags:
            entry_data = CinepolisScheduleEntry(entry, self.theater_name).get_dict()
            self.add_entry(entry_data)
