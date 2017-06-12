from .movie_theater_schedule import MovieTheaterSchedule
from .cinemark_schedule_entry import CinemarkScheduleEntry

class CinemarkSchedule(MovieTheaterSchedule):
    def __init__(self, soup, theater_name):
        MovieTheaterSchedule.__init__(self, soup, theater_name)

    def get_base_tag(self):
        return self.soup.select('div.section.times div.tabs-content > div.active')[0]

    def get_entries_tags(self):
        return self.base_tag.find_all('div', { 'class': 'theater' })

    def parse_entries(self):
        for entry in self.entries_tags:
            schedule_entry = CinemarkScheduleEntry(entry, self.theater_name)
            time_tags = schedule_entry.times_tags
            for time_tag in time_tags:
                schedule_entry.set_time_tag(time_tag)
                entry_data = schedule_entry.get_dict()
                self.add_entry(entry_data)
