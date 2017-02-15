buildMasterOTFs RomanMasters/AdobeVFPrototype.designspace
buildCFF2VF RomanMasters/AdobeVFPrototype.designspace  RomanMasters/AdobeVFPrototype.otf
ttx -o RomanMasters/AdobeVFPrototype.otf -m RomanMasters/AdobeVFPrototype.otf name_GSUB_changes.ttx

rm RomanMasters/master_*/current.fpr
