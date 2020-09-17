import os
import pytest
import requests
import uharfbuzz as hb


REPO = 'https://github.com/adobe-fonts/adobe-variable-font-prototype/'
OTF_NAME = 'AdobeVFPrototype.otf'
TTF_NAME = 'AdobeVFPrototype.ttf'


@pytest.fixture(scope="session")
def latest_otf():
    """AdobeVFPrototype.otf from GitHub "latest" release"""
    url = REPO + 'releases/latest/download/' + OTF_NAME
    response = requests.get(url)
    if response.status_code == 200:
        face = hb.Face(response.content)
        font = hb.Font(face)
        upem = face.upem
        font.scale = (upem, upem)
        hb.ot_font_set_funcs(font)

        return font

    raise Exception(f"Error retrieving latest {OTF_NAME} from GitHub.")


@pytest.fixture(scope="session")
def latest_ttf():
    """AdobeVFPrototype.ttf from GitHub "latest" release"""
    url = REPO + 'releases/latest/download/' + TTF_NAME
    response = requests.get(url)
    if response.status_code == 200:
        face = hb.Face(response.content)
        font = hb.Font(face)
        upem = face.upem
        font.scale = (upem, upem)
        hb.ot_font_set_funcs(font)

        return font

    raise Exception(f"Error retrieving latest {TTF_NAME} from GitHub.")


@pytest.fixture(scope="session")
def otf_font():
    otf_path = os.path.join('RomanMasters', OTF_NAME)
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
    otf_path = os.path.join('RomanMasters', TTF_NAME)
    with open(otf_path, 'rb') as font_file:
        font_data = font_file.read()
    face = hb.Face(font_data)
    font = hb.Font(face)
    upem = face.upem
    font.scale = (upem, upem)
    hb.ot_font_set_funcs(font)

    return font
