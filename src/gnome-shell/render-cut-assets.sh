#! /bin/bash

INKSCAPE="/usr/bin/inkscape"
OPTIPNG="/usr/bin/optipng"

SRC_FILE="shell-assets.svg"
ASSETS_DIR="assets"
INDEX="shell-assets.txt"

#for i in `cat $INDEX | grep -v '^#\|^\!'`
#  do
#    echo Exporting $ASSETS_DIR/$i.svg
#    $INKSCAPE --export-id=$i \
#              --export-id-only \
#              --export-plain-svg=$ASSETS_DIR/$i.svg $SRC_FILE >/dev/null #\

#    echo Removing path with object sizing from $ASSETS_DIR/$i.svg
#    sed -i '/<path/ {:n; N; /\/>/ {/fill\:none.*stroke\:none/ {d; q}; b}; bn}' $ASSETS_DIR/$i.svg
#done

for i in `cat $INDEX | grep '^\!' | sed s/\!//`
  do
    echo Rendering $ASSETS_DIR/$i.png
    $INKSCAPE --export-id=$i \
              --export-id-only \
              --export-png=$ASSETS_DIR/$i.png $SRC_FILE >/dev/null #\
done

exit 0
