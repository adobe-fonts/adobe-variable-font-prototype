
from fontTools.varLib import build

ds_path = 'AdobeVFPrototype.designspace'
vf_path = 'AdobeVFPrototype.ttf'

finder = lambda s: s.replace('.ufo', '.ttf')

varfont, _, _ = build(ds_path, finder)
varfont.save(vf_path)
