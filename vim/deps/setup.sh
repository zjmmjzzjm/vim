#!/bin/bash
WHO=`whoami`
is_install=0
case $1 in 
    "install" | "Install" )
        is_install=1;
        ;;
    * )
        echo "Just compile and wont install the programs";
        sleep 3;
esac
function do_make()
{
    make;
    return $?;
}

function do_install()
{
    if [ ${is_install} -eq 0 ];
    then
        return 0;
    else
        make install;
        return $?;
    fi
}
##################### compile cscope
echo "====================Begin compile ncurse========================m"
NCURSESOURCE="ncurses-5.9"
tar zxvf ${NCURSESOURCE}.tar.gz && cd ${NCURSESOURCE} && \
./configure --prefix=/home/$WHO/local/  && \
do_make && do_install || exit -1

################################## compile vim 
echo "====================Begin compile vi========================m"
VIMSOURCE="vim-7.3.tar.bz2"
VIMDIR=vim73
tar jxvf $VIMSOURCE && cd $VIMDIR && \
./configure --prefix=/home/$WHO/local/ --with-features=huge && \
do_make && do_install || exit -1

############################### compile cscope
echo "====================Begin compile cscope========================m"
CSCOPESOURCE="cscope-15.8a"
tar zxvf ${CSCOPESOURCE}.tar.gz && cd ${CSCOPESOURCE} && \
./configure --prefix=/home/$WHO/local/  &&  \
do_make && do_install || exit -1

############################### compile cscope
echo "====================Begin compile ctags========================m"
CTAGSSOURCE="ctags-5.8"
tar zxvf ${CTAGSSOURCE}.tar.gz && cd ${CTAGSSOURC} && \
./configure --prefix=/home/$WHO/local/ && \
do_make && do_install
