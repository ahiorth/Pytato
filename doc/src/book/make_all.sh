function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}


system python -c "import scripts as s; s.make_links(); s.compile_chapters()"
system ./make.sh
system ./make_html.sh
