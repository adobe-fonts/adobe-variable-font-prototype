import pytest

import uharfbuzz as hb

DIGIT_BASE = ["zero", "one", "two", "three", "four",
              "five", "six", "seven", "eight", "nine"]


@pytest.mark.parametrize('features_on, result_suffix',
                         [[['onum'], '.tosf'],
                          [['pnum'], '.lf'],
                          [['pnum', 'onum'], '.osf'],
                          [['case'], '.cap']])
def test_sub_figs(otf_font, ttf_font, features_on, result_suffix):
    for font in (otf_font, ttf_font):
        buf = hb.Buffer()
        buf.add_str("0123456789")
        buf.guess_segment_properties()

        features = {feat: True for feat in features_on}
        hb.shape(font, buf, features)
        infos = buf.glyph_infos

        expected = [
            (f'{d}{result_suffix}', n) for n, d in enumerate(DIGIT_BASE)]

        actual = []
        for info in infos:
            gn = font.get_glyph_name(info.codepoint)
            actual.append((gn, info.cluster))

        assert actual == expected


def test_sub_liga(otf_font, ttf_font):
    for font in (otf_font, ttf_font):
        buf = hb.Buffer()
        buf.add_str("find flip aft")
        buf.guess_segment_properties()

        features = {"liga": True}
        hb.shape(font, buf, features)
        infos = buf.glyph_infos

        expected = [('f_i', 0), ('n', 2), ('d', 3), ('space', 4),
                    ('f_l', 5), ('i', 7), ('p', 8), ('space', 9),
                    ('a', 10), ('f_t', 11)]

        actual = []
        for info in infos:
            gn = font.get_glyph_name(info.codepoint)
            actual.append((gn, info.cluster))

        assert actual == expected


def test_sub_zero(otf_font, ttf_font):
    for font in (otf_font, ttf_font):
        buf = hb.Buffer()
        buf.add_str("90125")
        buf.guess_segment_properties()

        features = {"zero": True}
        hb.shape(font, buf, features)
        infos = buf.glyph_infos

        expected = [('nine', 0),
                    ('zero.slash', 1),
                    ('one', 2),
                    ('two', 3),
                    ('five', 4)]

        actual = []
        for info in infos:
            gn = font.get_glyph_name(info.codepoint)
            actual.append((gn, info.cluster))

        assert actual == expected
