function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}


system cd doc/src
system python -c "import scripts as s; s.compile_chapters()"

