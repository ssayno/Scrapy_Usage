#! /bin/bash
FILENAME=$1
for symbol in "#" "%" "~" "_"; do
    echo $symbol
    sed -i "s/$symbol/\\\\$symbol/g" $FILENAME
done
sed -i 's/[$]/\\$/g' $FILENAME
sed -i 's/&/ /g' $FILENAME 
sed -i 's/\^/\\^/g' $FILENAME 
