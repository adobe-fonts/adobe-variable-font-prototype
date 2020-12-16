#!/usr/bin/env sh

# exit script if any command results in an error
set -e

# get absolute path to bash script; this allows to call it from any directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

folder=$DIR/RomanMasters
font=AdobeVFPrototype

otf_file=$folder/$font.otf
ttf_file=$folder/$font.ttf
dsp_file=$folder/$font.designspace

# build the OTF version -- this requires the AFDKO toolkit
# which is available at https://github.com/adobe-type-tools/afdko
buildmasterotfs -d "$dsp_file"
buildcff2vf -k -d "$dsp_file"

# extract and subroutinize the CFF2 table
echo 'Subroutinizing' "$otf_file"
tx -cff2 +S +b -std "$otf_file" "$folder/.tb_cff2" 2> /dev/null

# replace CFF2 table with subroutinized version
sfntedit -a CFF2="$folder/.tb_cff2" "$otf_file" 1> /dev/null

# TEMP HACK until fontTools.feaLib supports STAT
# comment out STAT feature file which cannot be digested by fontmake
sed -i '' 's/^/#/' $folder/STAT.fea

# set +e so we have the opportunity to un-hack STAT.fea before exiting if
# there's a problem with fontmake.
set +e 
# build TTF with fontmake
fontmake -m "$dsp_file" -o variable --production-names --output-path "$ttf_file"
fm_status=$?

# undo changes to STAT feature file
sed -i '' 's/#//' $folder/STAT.fea

if [ $fm_status -ne 0 ]
then
    exit $fm_status
fi

# return to exit-on-fail mode
set -e


# use DSIG, name, OS/2, hhea, post, and STAT tables from OTF
sfntedit -x DSIG="$folder/.tb_DSIG",name="$folder/.tb_name",OS/2="$folder/.tb_os2",hhea="$folder/.tb_hhea",post="$folder/.tb_post",STAT="$folder/.tb_STAT" "$otf_file" 1> /dev/null
sfntedit -a DSIG="$folder/.tb_DSIG",name="$folder/.tb_name",OS/2="$folder/.tb_os2",hhea="$folder/.tb_hhea",post="$folder/.tb_post",STAT="$folder/.tb_STAT" "$ttf_file" 1> /dev/null

# use cmap, GDEF, GPOS, and GSUB tables from TTF
sfntedit -x cmap="$folder/.tb_cmap",GDEF="$folder/.tb_GDEF",GPOS="$folder/.tb_GPOS",GSUB="$folder/.tb_GSUB" "$ttf_file" 1> /dev/null
sfntedit -a cmap="$folder/.tb_cmap",GDEF="$folder/.tb_GDEF",GPOS="$folder/.tb_GPOS",GSUB="$folder/.tb_GSUB" "$otf_file" 1> /dev/null

# delete temporary files
rm "$folder"/.tb_*
rm "$folder"/master_*/*.otf

echo "Done"
