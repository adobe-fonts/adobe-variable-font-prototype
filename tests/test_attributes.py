
def test_tables_present(latest_otf_ft, otf_ft_font,
                        latest_ttf_ft, ttf_ft_font):

    for kind, expected, actual in (("OTF", latest_otf_ft, otf_ft_font),
                                   ("TTF", latest_ttf_ft, ttf_ft_font)):

        etables = set(expected.reader.tables)
        atables = set(actual.reader.tables)

        # only check for missing tables in new font. Extras OK/not checked.
        missing = etables - atables
        assert not missing, f"Missing tables in new {kind} font: {missing}"


def test_os2_metrics(latest_otf_ft, otf_ft_font,
                     latest_ttf_ft, ttf_ft_font):

    for kind, expected, actual in (("OTF", latest_otf_ft, otf_ft_font),
                                   ("TTF", latest_ttf_ft, ttf_ft_font)):
        e_os2 = expected['OS/2']
        a_os2 = actual['OS/2']

