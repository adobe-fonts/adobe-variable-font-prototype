#!/bin/env sh

# build the TTF version -- this requires a customized version of fontmake which
# is available at https://github.com/adobe-type-tools/fontmake
fontmake -m RomanMasters/AdobeVFPrototype.designspace -o variable --production-names
mv RomanMasters/AdobeVFPrototype-Variable.ttf AdobeVFPrototype.ttf

# patch GSUB table, to add <FeatureVariations>
# this enables the transitional glyphs dollar and cent
ttx -o AdobeVFPrototype.ttf -m AdobeVFPrototype.ttf GSUB_patch.ttx

# build the OTF version -- this requires an experimental build of the AFDKO which
# is available at http://www.adobe.com/devnet/opentype/afdko/AFDKO-Variable-Font-Support.html
buildMasterOTFs RomanMasters/AdobeVFPrototype.designspace
buildCFF2VF RomanMasters/AdobeVFPrototype.designspace  AdobeVFPrototype.otf
rm RomanMasters/master_*/current.fpr

# replace the name, GPOS and GSUB tables in the OTF font by the ones from the TTF
sfntedit -x name=.tb_name,GPOS=.tb_GPOS,GSUB=.tb_GSUB AdobeVFPrototype.ttf
sfntedit -a name=.tb_name,GPOS=.tb_GPOS,GSUB=.tb_GSUB AdobeVFPrototype.otf

# copy the DSIG table in the OTF font into the TTF
sfntedit -x DSIG=.tb_DSIG AdobeVFPrototype.otf
sfntedit -a DSIG=.tb_DSIG AdobeVFPrototype.ttf

# delete temporary files
rm .tb_*
