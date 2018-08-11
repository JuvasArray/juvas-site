import datetime
import re

from django.utils.html import strip_tags

def count_words(html_string):
    word_string = strip_tags(html_string)
    count = len(re.findall(r'\w+'), word_string)
    return count

def get_read_time(html_string):
    count = count_words(html_string)
    read_per_minute = count/200.0
    read_per_second = read_per_minute * 60
    read_time = str(datetime.timedelta(seconds=read_per_second))
    return read_time
