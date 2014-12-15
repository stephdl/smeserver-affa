function _affa()
{
    local cur; cur=${COMP_WORDS[$COMP_CWORD]}
    case $COMP_CWORD in
	# option
    1)  
	COMPREPLY=( $(/sbin/affa --_shorthelp | grep " affa $cur"|awk '{print $3}' ) )
	;;
	# job
    2)
	/sbin/affa --_shorthelp | grep -qs -- "${COMP_WORDS[1]}.*JOB"
	if [ "$?" == 0 ] ; then
		COMPREPLY=( $(/sbin/affa --_jobs | grep "^$cur" ) )
	fi
	;;
    esac
    return 0
}
complete -F _affa affa

