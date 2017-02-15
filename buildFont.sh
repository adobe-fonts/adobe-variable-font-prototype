buildMasterOTFs RomanMasters/AdobeVFPrototype.designspace
buildCFF2VF RomanMasters/AdobeVFPrototype.designspace  AdobeVFPrototype.otf
ttx -o AdobeVFPrototype.otf -m AdobeVFPrototype.otf name_GSUB_changes.ttx

rm RomanMasters/master_*/current.fpr
