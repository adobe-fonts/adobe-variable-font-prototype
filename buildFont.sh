#!/usr/bin/env sh

folder=RomanMasters
font=AdobeVFPrototype

# build the OTF version -- this requires the AFDKO toolkit
# which is available at https://github.com/adobe-type-tools/afdko
buildmasterotfs $folder/$font.designspace
buildcff2vf $folder/$font.designspace

# extract and subroutinize the CFF2 table
echo 'Subroutinizing' $folder/$font.otf
tx -cff2 +S +b -std $folder/$font.otf $folder/.tb_cff2 2> /dev/null

# replace CFF2 table with subroutinized version
sfntedit -a CFF2=$folder/.tb_cff2 $folder/$font.otf 1> /dev/null

# build the TTF version -- this requires a customized version of fontmake
# which is available at https://github.com/adobe-type-tools/fontmake
fontmake -m $folder/$font.designspace -o variable --production-names

# patch GSUB table, to add <FeatureVariations>
# this enables the transitional glyphs dollar and cent
ttx -o $folder/$font.ttf -m $folder/$font.ttf GSUB_patch.ttx

# use DSIG, name, OS/2, hhea, post, and STAT tables from OTF
sfntedit -x DSIG=$folder/.tb_DSIG,name=$folder/.tb_name,OS/2=$folder/.tb_os2,hhea=$folder/.tb_hhea,post=$folder/.tb_post,STAT=$folder/.tb_STAT $folder/$font.otf 1> /dev/null
sfntedit -a DSIG=$folder/.tb_DSIG,name=$folder/.tb_name,OS/2=$folder/.tb_os2,hhea=$folder/.tb_hhea,post=$folder/.tb_post,STAT=$folder/.tb_STAT $folder/$font.ttf 1> /dev/null

# use cmap, GDEF, GPOS, and GSUB tables from TTF
sfntedit -x cmap=$folder/.tb_cmap,GDEF=$folder/.tb_GDEF,GPOS=$folder/.tb_GPOS,GSUB=$folder/.tb_GSUB $folder/$font.ttf 1> /dev/null
sfntedit -a cmap=$folder/.tb_cmap,GDEF=$folder/.tb_GDEF,GPOS=$folder/.tb_GPOS,GSUB=$folder/.tb_GSUB $folder/$font.otf 1> /dev/null

# delete temporary files
rm */.tb_*

echo "Done"
