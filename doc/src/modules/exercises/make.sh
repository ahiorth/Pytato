# Use a common ../make.sh file or do customized build here.
function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}

system bash -x ../make.sh main_exercises "$@" 
#system bash -x ../make.sh decline
system bash -x ../make_html.sh main_exercises "$@" 
system bash -x ../clean.sh
