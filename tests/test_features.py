import pytest

import uharfbuzz as hb

DIGIT_BASE = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


@pytest.mark.parametrize('features_on, result_suffix',
                         [[['onum'], '.tosf'],
                          [['pnum'], '.lf'],
                          [['pnum', 'onum'], '.osf'],
                          [['case'], '.cap']])
def test_figs_regression(latest_otf, otf_font,
                         latest_ttf, ttf_font,
                         features_on, result_suffix):
    """Compare figure/digit substitutions against latest release."""
    digit_str = "0123456789"
    features = {feat: True for feat in features_on}

    for expected, actual in ((latest_otf, otf_font), (latest_ttf, ttf_font)):
        buf_expected = hb.Buffer()
        buf_expected.add_str(digit_str)
        buf_expected.guess_segment_properties()

        buf_actual = hb.Buffer()
        buf_actual.add_str(digit_str)
        buf_actual.guess_segment_properties()

        hb.shape(expected, buf_expected, features)
        infos_expected = buf_expected.glyph_infos

        hb.shape(actual, buf_actual, features)
        infos_actual = buf_actual.glyph_infos

        assert len(infos_expected) == len(infos_actual)

        for i in range(len(infos_expected)):
            gn_expected = expected.get_glyph_name(infos_expected[i].codepoint)
            gn_actual = actual.get_glyph_name(infos_actual[i].codepoint)

            assert gn_actual == gn_expected

            cl_expected = infos_expected[i].cluster
            cl_actual = infos_actual[i].cluster

            assert cl_actual == cl_expected


def test_liga_regression(latest_otf, otf_font,
                         latest_ttf, ttf_font):
    liga_str = "find flip aft"
    features = {"liga": True}

    for expected, actual in ((latest_otf, otf_font), (latest_ttf, ttf_font)):
        buf_expected = hb.Buffer()
        buf_expected.add_str(liga_str)
        buf_expected.guess_segment_properties()

        buf_actual = hb.Buffer()
        buf_actual.add_str(liga_str)
        buf_actual.guess_segment_properties()

        hb.shape(expected, buf_expected, features)
        infos_expected = buf_expected.glyph_infos

        hb.shape(actual, buf_actual, features)
        infos_actual = buf_actual.glyph_infos

        assert len(infos_expected) == len(infos_actual)

        for i in range(len(infos_expected)):
            gn_expected = expected.get_glyph_name(infos_expected[i].codepoint)
            gn_actual = actual.get_glyph_name(infos_actual[i].codepoint)

            assert gn_actual == gn_expected

            cl_expected = infos_expected[i].cluster
            cl_actual = infos_actual[i].cluster

            assert cl_actual == cl_expected


def test_zero_regression(latest_otf, otf_font,
                         latest_ttf, ttf_font):
    zero_str = "90125"
    features = {"zero": True}

    for expected, actual in ((latest_otf, otf_font), (latest_ttf, ttf_font)):
        buf_expected = hb.Buffer()
        buf_expected.add_str(zero_str)
        buf_expected.guess_segment_properties()

        buf_actual = hb.Buffer()
        buf_actual.add_str(zero_str)
        buf_actual.guess_segment_properties()

        hb.shape(expected, buf_expected, features)
        infos_expected = buf_expected.glyph_infos

        hb.shape(actual, buf_actual, features)
        infos_actual = buf_actual.glyph_infos

        assert len(infos_expected) == len(infos_actual)

        for i in range(len(infos_expected)):
            gn_expected = expected.get_glyph_name(infos_expected[i].codepoint)
            gn_actual = actual.get_glyph_name(infos_actual[i].codepoint)

            assert gn_actual == gn_expected

            cl_expected = infos_expected[i].cluster
            cl_actual = infos_actual[i].cluster

            assert cl_actual == cl_expected


@pytest.mark.parametrize('use_kerning, string', [
                         (False, 'AVANTAT Äva'),
                         (True, 'AVANTAT Äva'),
                         (False, 'Ta Te To Pê Pò'),
                         (True, 'Ta Te To Pê Pò'),
                         ])
def test_kern_regression(latest_otf, otf_font,
                         latest_ttf, ttf_font,
                         string, use_kerning):

    for expected, actual in ((latest_otf, otf_font), (latest_ttf, ttf_font)):
        features = {"kern": use_kerning}

        buf_expected = hb.Buffer()
        buf_expected.add_str(string)
        buf_expected.guess_segment_properties()

        buf_actual = hb.Buffer()
        buf_actual.add_str(string)
        buf_actual.guess_segment_properties()

        hb.shape(expected, buf_expected, features)
        infos_expected = buf_expected.glyph_infos
        positions_expected = buf_expected.glyph_positions

        hb.shape(actual, buf_actual, features)
        infos_actual = buf_actual.glyph_infos
        positions_actual = buf_actual.glyph_positions

        assert len(infos_expected) == len(infos_actual)

        for i in range(len(infos_expected)):
            gn_expected = expected.get_glyph_name(infos_expected[i].codepoint)
            gn_actual = actual.get_glyph_name(infos_actual[i].codepoint)

            assert gn_actual == gn_expected

            pos_expected = positions_expected[i].x_advance
            pos_actual = positions_actual[i].x_advance

            assert pos_actual == pos_expected
