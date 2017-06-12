import abc
import pandas as pd

class MovieTheaterSchedule(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, soup, theater_name):
        self.soup = soup
        self.theater_name = theater_name
        self.entries_list = []
        self.base_tag = self.get_base_tag()
        self.entries_tags = self.get_entries_tags()
        self.parse_entries()

    @abc.abstractmethod
    def get_base_tag(self):
        """implement get_base_tag"""
        return

    @abc.abstractmethod
    def get_entries_tags(self):
        """implement get_entries_tags"""
        return

    @abc.abstractmethod
    def parse_entries(self):
        """implement parse_entries"""
        return

    def add_entry(self, entry):
        self.entries_list.append(entry)

    def get_dataframe(self):
        return pd.DataFrame(self.entries_list)
