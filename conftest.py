import os
import pytest
import uharfbuzz as hb


@pytest.fixture(scope="session")
def otf_font():
    otf_path = os.path.join('RomanMasters', 'AdobeVFPrototype.otf')
    with open(otf_path, 'rb') as font_file:
        font_data = font_file.read()
    face = hb.Face(font_data)
    font = hb.Font(face)
    upem = face.upem
    font.scale = (upem, upem)
    hb.ot_font_set_funcs(font)

    return font


@pytest.fixture(scope="session")
def ttf_font():
    otf_path = os.path.join('RomanMasters', 'AdobeVFPrototype.ttf')
    with open(otf_path, 'rb') as font_file:
        font_data = font_file.read()
    face = hb.Face(font_data)
    font = hb.Font(face)
    upem = face.upem
    font.scale = (upem, upem)
    hb.ot_font_set_funcs(font)

    return font
