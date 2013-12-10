#!/bin/bash
mkdir -p ~/.vim
cp -fv .vimrc ~/.vimrc || exit -1
packagedir="packages"
if [ ! -d $packagedir ] ; 
then 
	echo no package dir! 
	exit 1;
fi

#######################install vimball###################
#cd ~/.vim
#gunzip vimball.tar.gz 
#tar -oxvf vimball.tar 
#chmod a+r autoload/vimball.vim doc/pi_vimball.txt plugin/vimballPlugin.vim
#cd -

echo "=>install utilities in vim format"
plugdirs='plugin ftplugin autoload'
for d in $plugdirs;
do
	cp -rfa $packagedir/$d/* ~/.vim/$d/
done

echo "=>install utilities in zip format"
zip_files=$(ls ${packagedir}/zip/*zip)
for f in ${zip_files};
do
	echo " +=>intallling $f"
	unzip -o $f -d ~/.vim
done

#special plugins that should special methrods
#unzip -o ${packagedir}/load_template.zip -d ./.vim
cp -rvf ~/.vim/load_template/* ~/.vim/
rm -rf .vim


echo "=>install utilities in gz format"
vimballdir=$packagedir/vim_ball_format/
gz_files=$(ls $vimballdir/*gz)
for f in  ${gz_files};
do
	echo " +=>intall vim ball $f"
	gunzip -c $f > $f.vba
	vim $f.vba -c ':so %' -c ':q'
	rm -f $f.vba
done


vbafiles=$(ls $vimballdir/*vba)
for f in $vbafiles
do 
	echo "+=>install vim ball $f"
	vim $f -c ':so %' -c ':q'
done
	


echo "=>install help files"
vim $f -c ':helptags ~/.vim/doc' -c ':q!'
