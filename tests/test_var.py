import pytest
import uharfbuzz as hb


@pytest.mark.parametrize('axis_dict', [
                         {},
                         {"wght": 200, "CNTR": 0},
                         {"wght": 200, "CNTR": 25},
                         {"wght": 200, "CNTR": 75},
                         {"wght": 200, "CNTR": 100},
                         {"wght": 400, "CNTR": 0},
                         {"wght": 400, "CNTR": 25},
                         {"wght": 400, "CNTR": 75},
                         {"wght": 400, "CNTR": 100},
                         {"wght": 900, "CNTR": 0},
                         {"wght": 900, "CNTR": 25},
                         {"wght": 900, "CNTR": 75},
                         {"wght": 900, "CNTR": 100},
                         ])
def test_basic_var(latest_otf, otf_font,
                   latest_ttf, ttf_font,
                   axis_dict):
    """
    Check x_advances of each character in string at several variations.
    """
    var_str = "Hello, World! 12345 ÀÉÏøÑ [({})]"

    for expected, actual in ((latest_otf, otf_font), (latest_ttf, ttf_font)):
        buf_expected = hb.Buffer()
        buf_expected.add_str(var_str)
        buf_expected.guess_segment_properties()

        buf_actual = hb.Buffer()
        buf_actual.add_str(var_str)
        buf_actual.guess_segment_properties()

        expected.set_variations(axis_dict)
        hb.shape(expected, buf_expected, None)
        infos_expected = buf_expected.glyph_infos
        positions_expected = buf_expected.glyph_positions

        actual.set_variations(axis_dict)
        hb.shape(actual, buf_actual, None)
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


@pytest.mark.parametrize('wght_val',
                         [200, 300, 400, 500, 600, 689, 690, 700, 800, 900])
def test_rvrn(latest_otf, otf_font,
              latest_ttf, ttf_font,
              wght_val):
    """
    Ensure that the 'rvrn' feature is activated/not activated at expected
    variations. The 'rvrn' feature of this font substitutes a design variation
    of '$' and '¢' at heavier weights.
    """
    test_str = "$2.00 5¢"

    for expected, actual in ((latest_otf, otf_font), (latest_ttf, ttf_font)):
        buf_expected = hb.Buffer()
        buf_expected.add_str(test_str)
        buf_expected.guess_segment_properties()

        buf_actual = hb.Buffer()
        buf_actual.add_str(test_str)
        buf_actual.guess_segment_properties()

        expected.set_variations({"wght": wght_val})
        hb.shape(expected, buf_expected, None)
        infos_expected = buf_expected.glyph_infos

        actual.set_variations({"wght": wght_val})
        hb.shape(actual, buf_actual, None)
        infos_actual = buf_actual.glyph_infos

        assert len(infos_actual) == len(infos_expected)

        for i in range(len(infos_expected)):
            gn_expected = expected.get_glyph_name(infos_expected[i].codepoint)
            gn_actual = actual.get_glyph_name(infos_actual[i].codepoint)

            assert gn_actual == gn_expected
