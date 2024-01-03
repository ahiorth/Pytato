#!/bin/bash -x
# Compile a chapter as a stand-alone HTML document.
# See make.sh for variables.
#
# Run from subdirectory as
#
# bash -x ../make_html.sh main_chaptername --encoding=utf-8
set -x

mainname=$1
shift
args="$@"

CHAPTER=document
BOOK=document
APPENDIX=document

#LANG=Python
# mainname: main_chaptername
# nickname: chaptername
nickname=`echo $mainname | sed 's/main_//g'`

function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}

rm -fr tmp_*

# Spell checking: done in make.sh

preprocess -DFORMAT=html ../newcommands.p.tex > newcommands_keep.tex

opt="CHAPTER=$CHAPTER BOOK=$BOOK APPENDIX=$APPENDIX"
opt="LANG=$LANG"

if [ $mainname == "project3" ]; then
    BCOL=0.5412,0.118,0.118
else
    BCOL=0.988235,0.964706,0.862745
fi

style=bootswatch_readable
html=${nickname}-readable
system doconce format html $mainname $opt --html_style=$style --html_output=$html --html_code_style=inherit $args

system doconce replace 'width="400"' 'width="800"' $html.html
system doconce replace 'width=400' 'width=800' $html.html

system doconce split_html $html.html --nav_button=text


# Publish
dest=/some/repo/some/where
dest=../../../../pub/projects/V24/
if [ ! -d $dest ]; then
exit 0  # drop publishig
fi
dest=$dest/$nickname
if [ ! -d $dest ]; then
  mkdir $dest
  mkdir $dest/pdf
  mkdir $dest/html
fi
cp -r ${nickname}-*.html ._${nickname}-*.html $dest/html


# We need fig, mov in html publishing dir
rsync="rsync -rtDvz -u -e ssh -b --delete --force "
dirs="fig-$nickname mov-$nickname"
for dir in $dirs; do
  if [ -d $dir ]; then
    $rsync $dir $dest/html
  fi
done



