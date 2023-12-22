#!/bin/bash -x
# Compile the book to LaTeX/PDF.
#
# Usage: make.sh [nospell]
#
# With nospell, spellchecking is skipped.
set -x

name=book
CHAPTER=chapter
BOOK=book
APPENDIX=appendix

function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}

preprocess -DFORMAT=html ../chapters/newcommands.p.tex > newcommands_keep.tex

opt="CHAPTER=$CHAPTER BOOK=$BOOK APPENDIX=$APPENDIX"
opt="$opt --exercise_numbering=chapter"

# Compile HTML Bootstrap book
html_style=bootswatch_journal
#html_style=bootswatch_readable
system doconce format html $name $opt --html_style=$html_style  --html_code_style=inherit --html_output=$name
#system doconce format html $name $opt --html_style=solarized_dark --html_code_style=inherit --html_output=$name
#system doconce replace '\\\]' '\\]' $name.html
system doconce replace 'width=400' 'width=800' $name.html
system doconce replace 'width=\"400\"' 'width=\"800\"' $name.html
system doconce split_html $name.html

# Compile standard sphinx
theme=alabaster
#theme=scipy_lectures
#theme=uio
system doconce format sphinx $name $opt --sphinx_keep_splits
system doconce replace 'width=400' 'width=800' $name.html
system doconce split_rst $name
system doconce  sphinx_dir theme=$theme dirname=sphinx-${theme} $name
# Change logo
#doconce replace _static/uio_logo.png https://raw.githubusercontent.com/CINPLA/logo/master/brain/cinpla_logo_transparent.png sphinx-${theme}/_themes/uio/layout.html

##---removed
#system python my_automake_sphinx.py



#html_files="._book001.html ._book002.html ._book003.html ._book004.html ._book005.html"
#for htmf in $html_files; do
#    dir=sphinx-${theme}/_build/html/
#    # slash important for copying files in links to dirs
#    if [ -d $dir ]; then
#	doconce replace "\\\]" "\\]" $dir/$htmf
#    fi
#done
## --removed finished
# Publish
dest=../../pub/html
if [ ! -d $dest ]; then
    #exit 0  # drop publishing
  mkdir $dest
fi

cp -v $name.html ._${name}*.html $dest
figdirs="fig-* mov-*"
for figdir in $figdirs; do
    if [ ! -d $dest ]; then
	#exit 0  # drop publishing
	mkdir $dest
    fi
    # slash important for copying files in links to dirs
    if [ -d $figdir/ ]; then
        cp -r $figdir/ $dest/$figdir/
    fi
done

#dest=../../pub
#rm -rf $dest/sphinx
#rm -rf $dest/sphinx-runestone
#cp -r sphinx-${theme}/_build/html/ $dest/sphinx


#dest= ../../../../CompEngineering/pub/
#rm -rf $dest/sphinx
#cp -r sphinx-${theme}/_build/html/ $dest/sphinx

#cp -v $name.html ._${name}*.html $dest
#figdirs="fig-* mov-*"
#for figdir in $figdirs; do
    # slash important for copying files in links to dirs
#    if [ -d $figdir/ ]; then
#        cp -r $figdir/ $dest/$figdir
#    fi
#done

#cp -r runestone/RunestoneTools/build $dest/sphinx-runestone

system doconce clean
