#! /bin/bash

INKSCAPE="/usr/bin/inkscape"
ZOPFLIPNG="/usr/bin/zopflipng"

SRC_FILE="xfwm4-assets.svg"
ASSETS_DIR="assets"
INDEX="xfwm4-assets.txt"

for i in `cat $INDEX | grep -v '^#'`
do
    echo Rendering $ASSETS_DIR/$i.png
    $INKSCAPE --export-id=$i \
              --export-id-only \
              --export-png=$ASSETS_DIR/$i.png $SRC_FILE >/dev/null \
    && $ZOPFLIPNG -ym $ASSETS_DIR/$i.png $ASSETS_DIR/$i.png
done
exit 0
