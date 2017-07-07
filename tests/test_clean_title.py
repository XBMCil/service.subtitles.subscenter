# -*- coding: utf-8 -*-
import test_helpers
from unittest import TestCase
from resources.lib.SUBUtilities import clean_title

class TestClean_title(TestCase):

    def test_escape_path_from_title(self):
        filename = 'FB13.1080p.BRRip.x264-YIFY.mp4'
        item = {'title': '/Videos/Movies/Free.Birds.2013.1080p.BRRip.x264-YIFY/' + filename, 'tvshow': ''}
        clean_title(item)
        self.assertEqual(item["title"], filename)

    def test_should_not_change_if_not_contains_path_title(self):
        filename = 'FB13.1080p.BRRip.x264-YIFY.mp4'
        item = {'title': filename, 'tvshow': ''}
        clean_title(item)
        self.assertEqual(item["title"], filename)

    def test_escape_path_from_tvshow(self):
        filename = 'FB13.1080p.BRRip.x264-YIFY.mp4'
        item = {'tvshow': '/Videos/Movies/Free.Birds.2013.1080p.BRRip.x264-YIFY/' + filename, 'title': ''}
        clean_title(item)
        self.assertEqual(item["tvshow"], filename)

    def test_should_not_change_if_not_contains_path_tvshow(self):
        filename = 'FB13.1080p.BRRip.x264-YIFY.mp4'
        item = {'title': '', 'tvshow': filename}
        clean_title(item)
        self.assertEqual(item["tvshow"], filename)

    def test_remove_country_id_from_title(self):
        title = 'Zombies(US)'
        item = {'title': title, 'tvshow': ''}
        clean_title(item)
        self.assertEqual(item["title"], 'Zombies')

    def test_remove_country_id_from_tvshow(self):
        title = 'Shameless (US)'
        item = {'title': '', 'tvshow': title}
        clean_title(item)
        self.assertEqual(item["tvshow"], 'Shameless')
