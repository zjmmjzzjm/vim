import os, zipfile, shutil, gzip, sys, platform


def unzip(zip_path, save_path):
    zipfile.ZipFile(zip_path).extractall(save_path)


def gunzip(gz_path, save_path):
    print (gz_path, save_path, os.getcwd())
    f = gzip.open(gz_path)
    dst = open(save_path, "wb")
    dst.write(f.read())
    f.close()
    dst.close()


def dir_copyTree(src, dst):
    print(src, dst)
    if not os.path.exists(src):
        print (' not a dir' )
        return
    names = os.listdir(src)
    print( names )
    if not os.path.exists(dst):
        os.mkdir(dst)
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        if os.path.isdir(srcname):
            dir_copyTree(srcname, dstname)
        else:
            if (not os.path.exists(dstname)
                or ((os.path.exists(dstname))
                    and
                    (os.path.getsize(dstname) != os.path.getsize(srcname)))):
                print (dstname)
                shutil.copy2(srcname, dst)


def install_zip_plugin(src, dst):
    os.chdir(src)
    filelist = os.listdir(src)
    for f in filelist:
        print ("Intallling vim plugin:" + f)
        unzip(f, dst)


def install_patches(patchdirs, dst):
    os.chdir(curdir + '/packages')
    for f in patchdirs:
        print ("Intalling patch " + f)
        dir_copyTree(f, vimroot + '/' + f)


def install_vimball_plugin(vimballdir, vimroot):
    os.chdir(vimballdir)
    filelist = os.listdir(vimballdir)
    for f in filelist:
        print ("Intallling vim plugin " + f)
        elems = os.path.splitext(f)
        suffix = elems[1][1:]
        vbaname = ''
        if suffix == 'gz':
            print (f + ' is gz format')
            vbaname = elems[0]
            gunzip(f, vbaname)
        else:
            print (f + ' is vba fomat')
            vbaname = f
        fullvbaname = vimballdir + vbaname
        cmd = VIM + ' "' + fullvbaname + '"  -c ":silent! so %" -c "<ESC>" -c ":q!"'
        os.system(cmd)
        if suffix == 'gz':
            os.remove(vbaname)


def install_helptags():
    cmd = 'vim  -c ":helptags ~/.vim/doc" -c ":q!"'
    os.system(cmd)


def install_vimrc(vimrc, vimroot):
    shutil.copy2(vimrc, vimroot);


print ('Begin setting up......................')
home = os.path.expanduser('~')
#home = os.getcwd() + "/test"
vimroot = home + '/vimfiles/'
curdir = sys.path[0]
print (curdir)
if os.path.exists(vimroot):
    print (vimroot + 'dir is present')
else:
    print ('Making dir ' + vimroot)
    os.makedirs(vimroot, 0o755)

VIM = 'vim'
print ('vimroot is ' + vimroot)
#os.makedirs(vimroot,0o777)

print ("Intall zip format....................")
zipdir = curdir + '/packages/zip/'
install_zip_plugin(zipdir, vimroot)

print ("Intall patch format....................")
zipdir = curdir + '/packages/zip/'
patchdirs = ['plugin', 'ftplugin', 'autoload', 'compiler', 'doc',
'indent', 'after', 'syntax']
install_patches(patchdirs, vimroot)

print ("Intall vimball format....................")
vimballdir = curdir + '/packages/vim_ball_format/'
install_vimball_plugin(vimballdir, vimroot)

print ("install help files.......................")
install_helptags()

print ('Install vimrc........................')
install_vimrc(curdir + '/.vimrc', home + '/.vimrc')
