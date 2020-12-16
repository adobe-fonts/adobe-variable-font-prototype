import os

from fontTools.ttLib import TTFont
import pytest
import requests
import uharfbuzz as hb


REPO = 'https://github.com/adobe-fonts/adobe-variable-font-prototype/'
OTF_NAME = 'AdobeVFPrototype.otf'
TTF_NAME = 'AdobeVFPrototype.ttf'


@pytest.fixture(scope="session")
def latest_otf_path():
    """Retrieve and save the GitHub "latest" OTF"""

    p = os.path.join("RomanMasters", OTF_NAME.replace(".otf", "_latest.otf"))

    if not os.path.isfile(p):
        # download it if we don't have it
        url = REPO + 'releases/latest/download/' + OTF_NAME
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error retrieving latest {OTF_NAME} from GitHub.")

        with open(p, 'wb') as f:
            f.write(response.content)

    return p


@pytest.fixture(scope="session")
def latest_otf(latest_otf_path):
    """HB Font from latest OTF"""

    with open(latest_otf_path, 'rb') as font_file:
        font_data = font_file.read()
    face = hb.Face(font_data)
    font = hb.Font(face)
    upem = face.upem
    font.scale = (upem, upem)
    hb.ot_font_set_funcs(font)

    return font


@pytest.fixture(scope="session")
def latest_otf_ft(latest_otf_path):
    """FontTools Font for latest OTF"""
    font = TTFont(latest_otf_path)

    return font


@pytest.fixture(scope="session")
def latest_ttf_path():
    """Retrieve and save the GitHub "latest" TTF"""

    p = os.path.join("RomanMasters", TTF_NAME.replace(".ttf", "_latest.ttf"))

    if not os.path.isfile(p):
        # download it if we don't have it
        url = REPO + 'releases/latest/download/' + TTF_NAME
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error retrieving latest {TTF_NAME} from GitHub.")

        with open(p, 'wb') as f:
            f.write(response.content)

    return p


@pytest.fixture(scope="session")
def latest_ttf(latest_ttf_path):
    """HB Font from latest TTF"""

    with open(latest_ttf_path, 'rb') as font_file:
        font_data = font_file.read()
    face = hb.Face(font_data)
    font = hb.Font(face)
    upem = face.upem
    font.scale = (upem, upem)
    hb.ot_font_set_funcs(font)

    return font


@pytest.fixture(scope="session")
def latest_ttf_ft(latest_ttf_path):
    """FontTools Font for latest TTF"""
    font = TTFont(latest_ttf_path)

    return font


@pytest.fixture(scope="session")
def otf_path():
    return os.path.join('RomanMasters', OTF_NAME)


@pytest.fixture(scope="session")
def otf_font(otf_path):
    with open(otf_path, 'rb') as font_file:
        font_data = font_file.read()
    face = hb.Face(font_data)
    font = hb.Font(face)
    upem = face.upem
    font.scale = (upem, upem)
    hb.ot_font_set_funcs(font)

    return font


@pytest.fixture(scope="session")
def otf_ft_font(otf_path):
    font = TTFont(otf_path)

    return font


@pytest.fixture(scope="session")
def ttf_path():
    return os.path.join('RomanMasters', TTF_NAME)


@pytest.fixture(scope="session")
def ttf_font(ttf_path):
    with open(ttf_path, 'rb') as font_file:
        font_data = font_file.read()
    face = hb.Face(font_data)
    font = hb.Font(face)
    upem = face.upem
    font.scale = (upem, upem)
    hb.ot_font_set_funcs(font)

    return font


@pytest.fixture(scope="session")
def ttf_ft_font(ttf_path):
    font = TTFont(ttf_path)

    return font
