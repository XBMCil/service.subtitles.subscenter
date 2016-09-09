# -*- coding: utf-8 -*-
import test_helpers
from unittest import TestCase
from resources.lib.SUBUtilities import parse_rls_title

class TestParse_rls_title(TestCase):
    def test_parse_tvshow_from_title(self):
        item = {'title': 'Two.and.a.Half.Men.S11E13.480p.HDTV.X264-DIMENSION', 'tvshow': ''}
        parse_rls_title(item)

        self.assertEqual(item['tvshow'], 'Two and a Half Men')
        self.assertEqual(item['season'], '11')
        self.assertEqual(item['episode'], '13')

    def test_parse_tvshow_with_year_from_title(self):
        item = {'title': 'The.Flash.2014.S02E05.480p.HDTV.X264-DIMENSION.mkv', 'tvshow': ''}
        parse_rls_title(item)

        self.assertEqual(item['tvshow'], 'The Flash')
        self.assertEqual(item['season'], '2')
        self.assertEqual(item['episode'], '5')
        self.assertEqual(item['year'], '2014')


    def test_parse_tvshow_with_year_from_tvshow(self):
        item = {'title': '', 'tvshow': 'The.Flash.2014.S02E05.480p.HDTV.X264-DIMENSION.mkv'}
        parse_rls_title(item)

        self.assertEqual(item['tvshow'], 'The Flash')
        self.assertEqual(item['season'], '2')
        self.assertEqual(item['episode'], '5')
        self.assertEqual(item['year'], '2014')


    def test_parse_title_with_year_from_title(self):
        item = {'title': 'London.Has.Fallen.2016.1080p.WEB-DL.H264.AC3-EVO', 'tvshow': ''}
        parse_rls_title(item)

        self.assertEqual(item['title'], 'London Has Fallen')
        self.assertEqual(item['year'], '2016')
