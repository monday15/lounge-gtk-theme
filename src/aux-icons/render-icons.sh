#!/bin/bash

INK="/usr/bin/inkscape"
LIST="aux-iconslist"
SRC="aux-icons-symbolic.svg"
SIZE="16 24 32 48 64 96"

for i in $SIZE
do
mkdir -p "$i"x"$i"/actions
done

mkdir -p scalable/actions

for j in `cat $LIST | grep -v '^#'`
do
  for i in $SIZE
  do
    echo Rendering $j $i
    $INK --export-id=$j \
         --export-id-only \
         --export-width=$i \
         --export-height=$i \
         --export-png="$i"x"$i"/actions/$j.symbolic.png $SRC >/dev/null
  done

echo Rendering $j svg
$INK --export-id=$j \
     --export-id-only \
     --export-plain-svg=scalable/actions/$j.svg.temp $SRC >/dev/null

sed -e '/\<rect/,+6d' scalable/actions/$j.svg.temp > scalable/actions/$j.svg
rm scalable/actions/$j.svg.temp

done
exit 0
