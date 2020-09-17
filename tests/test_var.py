import pytest

import uharfbuzz as hb


@pytest.mark.parametrize('axis_dict,expected', [
                         ({}, [('A', 653), ('B', 618), ('C', 632), ('space', 234), ('x', 524), ('y', 511), ('z', 455), ('space', 234), ('zero', 497), ('one', 497), ('two', 497), ('three', 497)]),  # noqa: E501
                         ({"wght": 200, "CNTR": 0}, [('A', 643), ('B', 594), ('C', 644), ('space', 248), ('x', 510), ('y', 482), ('z', 457), ('space', 248), ('zero', 490), ('one', 490), ('two', 490), ('three', 490)]),  # noqa: E501
                         ({"wght": 200, "CNTR": 100}, [('A', 643), ('B', 594), ('C', 644), ('space', 248), ('x', 510), ('y', 482), ('z', 457), ('space', 248), ('zero', 490), ('one', 490), ('two', 490), ('three', 490)]),  # noqa: E501
                         ({"wght": 900, "CNTR": 0}, [('A', 680), ('B', 660), ('C', 618), ('space', 206), ('x', 563), ('y', 543), ('z', 468), ('space', 206), ('zero', 560), ('one', 560), ('two', 560), ('three', 560)]),  # noqa: E501
                         ({"wght": 900, "CNTR": 100}, [('A', 680), ('B', 660), ('C', 618), ('space', 206), ('x', 563), ('y', 543), ('z', 468), ('space', 206), ('zero', 560), ('one', 560), ('two', 560), ('three', 560)]),  # noqa: E501
                         ])
def test_basic_var(otf_font, ttf_font, axis_dict, expected):
    """
    Check x_advances of each character in string at several variations.
    """
    for font in (otf_font, ttf_font):
        font.set_variations(axis_dict)
        buf = hb.Buffer()
        buf.add_str("ABC xyz 0123")
        buf.guess_segment_properties()

        hb.shape(font, buf, None)
        infos = buf.glyph_infos
        positions = buf.glyph_positions

        actual = []
        for info, pos in zip(infos, positions):
            gn = font.get_glyph_name(info.codepoint)
            actual.append((gn, pos.x_advance))

        assert actual == expected


@pytest.mark.parametrize('wght_val,expected', [
                         (200, ['dollar', 'two', 'space', 'nine', 'cent']),
                         (689, ['dollar', 'two', 'space', 'nine', 'cent']),
                         (690, ['dollar.nostroke', 'two', 'space', 'nine', 'cent.nostroke']),  # noqa: E501
                         (900, ['dollar.nostroke', 'two', 'space', 'nine', 'cent.nostroke']),  # noqa: E501
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
        buf.add_str("$2 9¢")
        buf.guess_segment_properties()

        hb.shape(font, buf, None)
        infos = buf.glyph_infos

        actual = []
        for info in infos:
            gn = font.get_glyph_name(info.codepoint)
            actual.append(gn)

        assert actual == expected
