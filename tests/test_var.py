import pytest

import uharfbuzz as hb


@pytest.mark.parametrize('axis_dict,expected', [
                         ({}, [653, 618, 632, 234, 524, 511, 455, 234, 497, 497, 497]),  # noqa: E501
                         ({"wght": 200, "CNTR": 0}, [643, 594, 644, 248, 510, 482, 457, 248, 490, 490, 490]),  # noqa: E501
                         ({"wght": 200, "CNTR": 100}, [643, 594, 644, 248, 510, 482, 457, 248, 490, 490, 490]),  # noqa: E501
                         ({"wght": 900, "CNTR": 0}, [680, 660, 618, 206, 563, 543, 468, 206, 560, 560, 560]),  # noqa: E501
                         ({"wght": 900, "CNTR": 100}, [680, 660, 618, 206, 563, 543, 468, 206, 560, 560, 560]),  # noqa: E501
                         ])
def test_basic_var(otf_font, ttf_font, axis_dict, expected):
    """
    Check x_advances of each character in string at several variations.
    """
    for font in (otf_font, ttf_font):
        font.set_variations(axis_dict)
        buf = hb.Buffer()
        buf.add_str("ABC xyz 123")
        buf.guess_segment_properties()

        hb.shape(font, buf, None)
        positions = buf.glyph_positions

        actual = [pos.x_advance for pos in positions]

        assert actual == expected


@pytest.mark.parametrize('wght_val,expected', [
                         (200, ['dollar', 'space', 'cent']),
                         (689, ['dollar', 'space', 'cent']),
                         (690, ['dollar.nostroke', 'space', 'cent.nostroke']),
                         (900, ['dollar.nostroke', 'space', 'cent.nostroke']),
                         ])
def test_rvrn(otf_font, ttf_font, wght_val, expected):
    """
    Ensure that the 'rvrn' feature is activated/not activated at expected
    variations. The 'rvrn' feature of this font substitutes a design variation
    of '$' and '¢' at heavier weights.
    """
    for font in (otf_font, ttf_font):
        font.set_variations({"wght": wght_val})
        buf = hb.Buffer()
        buf.add_str("$ ¢")
        buf.guess_segment_properties()

        hb.shape(font, buf, None)
        infos = buf.glyph_infos

        actual = []
        for info in infos:
            gn = font.get_glyph_name(info.codepoint)
            actual.append(gn)

        assert actual == expected
