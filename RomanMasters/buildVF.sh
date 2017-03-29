#!/bin/sh

# build VF from master.ttf files
python build_vf.py

# patch GSUB table to add <FeatureVariations>
ttx -o AdobeVFPrototype.ttf -m AdobeVFPrototype.ttf GSUB_patch.ttx

# patch HVAR table to add one more entry to <AdvWidthMap>
ttx -o AdobeVFPrototype-HVAR_patched.ttf -m AdobeVFPrototype.ttf HVAR_patch.ttx
