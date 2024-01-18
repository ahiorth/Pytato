#!/bin/bash -x
# Script for compiling a single chapter as an individual document.
set -x

# Note that latex refs to other chapters do not work if the other
# chapters are not compiled. Therefore all chapters must first be
# compiled. Then an individual chapter can be compiled.
# Note that generalized doconce refs must be used: ref[][][] if one
# refers to material in a different chapter (only necessary when
# compiling individual chapters, the book will work with standard refs).

mainname=$1
shift
args="$@"

# Strip off main_ in $mainname to get the nickname
nickname=`echo $mainname | sed 's/main_//'`

# Individual chapter documents will have formulations like
# "In this ${BOOK}" or "in this ${CHAPTER}" to be transformed
# to "In this document" when the chapter stands on its own, while
# for a book we want "In this book" and "in this chapter".
CHAPTER=document
BOOK=document
APPENDIX=document

LANG=Python

# Function for running operating system commands. The script aborts
# if the execution is unsuccessful. All doconce, latex, etc. commands
# in this script are run with the system function such that the script
# stops when the first error is encountered.
function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}
#BLOOD=0.5412,0.118,0.118

if [ $mainname == "project3" ]; then
    BCOL=0.5412,0.118,0.118
else
    BCOL=0.988235,0.964706,0.862745
fi

rm -fr tmp_*
# Perform spell checking
system doconce spellcheck -d .dict4spell.txt *.do.txt

# Copy common newcommands
system preprocess -DFORMAT=pdflatex ../newcommands.p.tex > newcommands_keep.tex
# Copy ptex2tex configuration file if not using the newer --latex_code_style=...
#cp ../.ptex2tex.cfg .

opt="CHAPTER=$CHAPTER BOOK=$BOOK APPENDIX=$APPENDIX"
#opt="LANG=$LANG"

# Paper version (--device=paper)
# blood = (rgb)=0.5412,0.118,0.118
system doconce format pdflatex ${mainname} $opt --device=paper --latex_admon_color=$BCOL --latex_admon=mdfbox $args --latex_list_of_exercises=toc --latex_table_format=left "--latex_code_style=default:lst[style=blue1]@pypro:lst[style=blue1bar]@dat:lst[style=gray]@sys:vrb[frame=lines,label=\\fbox{{\tiny Terminal}},framesep=2.5mm,framerule=0.7pt]"
# code style: blue boxes, darker-color frame for complete boxs, and terminal
# style for sys
# alternative code style: blue boxes with plain verbatim for all code, special
# terminal style for sys (gives larger colored framed than the lst-style above)
#"--latex_code_style=default:vrb-blue1@sys:vrb[frame=lines,label=\\fbox{{\tiny Terminal}},framesep=2.5mm,framerule=0.7pt]"
# Auto-editing of .tex file (tailored adjustments)
#doconce replace 'linecolor=black,' 'linecolor=darkblue,' ${mainname}.tex
#doconce subst 'frametitlebackgroundcolor=.*?,' 'frametitlebackgroundcolor=blue!5,' ${mainname}.tex

#system doconce replace '{rgb}{0.87843, 0.95686, 1.0}' '{rgb}{0.988235,0.964706,0.862745}' $name.tex
#system doconce replace '{rgb}{0.7,     0.95686, 1}' '{rgb}{0.988235,0.964706,0.862745}' $name.tex
#system doconce replace '{cbg_blue1}' '{cbg_yellow1}' ${mainname}.tex
#system doconce replace '{bar_blue1}' '{bar_yellow1}' ${mainname}.tex
#system doconce replace '\definecolor{mdfbox_block_background}{rgb}{1,1,1}' '\definecolor{mdfbox_block_background}{rgb}{0.5412,0.118,0.118}' ${mainname}.tex 
rm -rf ${mainname}.aux ${mainname}.ind ${mainname}.idx ${mainname}.bbl ${mainname}.toc ${mainname}.loe
system pdflatex ${mainname}
bibtex ${mainname}
makeindex ${mainname}
system pdflatex ${mainname}
system pdflatex ${mainname}
mv -f ${mainname}.pdf ${nickname}-4print.pdf  # drop main_ prefix in PDF

# Electronic version
system doconce format pdflatex ${mainname} $opt --device=screen --latex_admon_color=$BCOL --latex_admon=mdfbox $args --latex_list_of_exercises=toc --latex_table_format=left "--latex_code_style=default:vrb-blue1@sys:vrb[frame=lines,label=\\fbox{{\tiny Terminal}},framesep=2.5mm,framerule=0.7pt]"
# Auto-editing of .tex file (tailored adjustments)
#doconce replace 'linecolor=black,' 'linecolor=darkblue,' ${mainname}.tex
#doconce subst 'frametitlebackgroundcolor=.*?,' 'frametitlebackgroundcolor=blue!5,' ${mainname}.tex
#system doconce replace '{cbg_blue1}' '{cbg_yellow1}' ${mainname}.tex
#system doconce replace '{bar_blue1}' '{bar_yellow1}' ${mainname}.tex
#system doconce replace '\definecolor{mdfbox_block_background}{rgb}{0.988235,0.964706,0.862745}' '\definecolor{mdfbox_block_background}{rgb}{0.5412,0.118,0.118}' ${mainname}.tex 
system pdflatex ${mainname}
bibtex ${mainname}
makeindex ${mainname}
system pdflatex ${mainname}
system pdflatex ${mainname}
mv -f ${mainname}.pdf ${nickname}.pdf  # drop main_ prefix in PDF

# Publish
dest=/some/repo/some/where
dest=../../../../pub/projects/V24
if [ ! -d $dest ]; then
  mkdir $dest
#exit 0  # drop publishing
fi
dest=$dest/$nickname
if [ ! -d $dest ]; then
  mkdir $dest
  mkdir $dest/pdf
  mkdir $dest/html
  mkdir $dest/notebook
fi
cp -v ${nickname}*.pdf $dest/pdf/

doconce format ipynb ${mainname}
cp ${mainname}.ipynb $dest/notebook/
if [ -e ipynb-${mainname}*.tar.gz ]; then
  tar xvfz ipynb-${mainname}*.tar.gz  -C $dest/notebook/
  cp ipynb*.tar.gz  $dest/notebook/
fi


datadir=data/
if [ -d $datadir ]; then
    if [ ! -d $dest/$datadir ]; then
	mkdir $dest/data
    fi
        cp -rv $datadir* $dest/data
fi





# If published in an external repo and the current writing repo is
# private, all the source files for programs need to be copied to
# the publishing repo as well.

# Could make other versions, A4, 2 pages per sheet, etc.bash 
