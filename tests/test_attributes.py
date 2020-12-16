from math import isclose


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

    os2_attrs = ('version', 'xAvgCharWidth', 'usWeightClass', 'usWidthClass',
                 'fsType', 'ySubscriptXSize', 'ySubscriptYSize',
                 'ySubscriptXOffset', 'ySubscriptYOffset', 'ySuperscriptXSize',
                 'ySuperscriptYSize', 'ySuperscriptXOffset',
                 'ySuperscriptYOffset', 'yStrikeoutSize', 'yStrikeoutPosition',
                 'sFamilyClass', 'panose', 'ulUnicodeRange1',
                 'ulUnicodeRange2', 'ulUnicodeRange3', 'ulUnicodeRange4',
                 'achVendID', 'fsSelection', 'usFirstCharIndex',
                 'usLastCharIndex', 'sTypoAscender', 'sTypoDescender',
                 'sTypoLineGap', 'usWinAscent', 'usWinDescent',
                 'ulCodePageRange1', 'ulCodePageRange2', 'sxHeight',
                 'sCapHeight', 'usDefaultChar', 'usBreakChar', 'usMaxContext',
                 'usLowerOpticalPointSize', 'usUpperOpticalPointSize')

    panose_attrs = ('bFamilyType', 'bSerifStyle', 'bWeight', 'bProportion',
                    'bContrast', 'bStrokeVariation', 'bArmStyle',
                    'bLetterForm', 'bMidline', 'bXHeight')

    for kind, expected, actual in (("OTF", latest_otf_ft, otf_ft_font),
                                   ("TTF", latest_ttf_ft, ttf_ft_font)):
        exp_os2 = expected['OS/2']
        act_os2 = actual['OS/2']

        for attr in os2_attrs:

            exp_attr = getattr(exp_os2, attr, None)
            act_attr = getattr(act_os2, attr, None)

            # allow for transition of v1.004 -> v1.005
            # should remove this after v1.005 release.
            if attr == 'usWeightClass':
                fv = expected['head'].fontRevision
                if isclose(fv, 1.004, abs_tol=0.0001):
                    exp_attr = 389

            if attr == 'panose':
                for pattr in panose_attrs:
                    exp_p = getattr(exp_attr, pattr, None)
                    act_p = getattr(act_attr, pattr, None)

                    msg = (f"{kind} OS/2.panose.{pattr} was {act_p} "
                           f"(expected {exp_p}).")

                    assert act_p == exp_p, msg

            else:
                msg = (f"{kind} OS/2.{attr} was {act_attr} "
                       f"(expected {exp_attr})")

                assert act_attr == exp_attr, msg
