import shutil
import os

path = "C:\\Users\\RedDr\\OneDrive\\Desktop"
destinationdir = "C:\\Users\\RedDr\\OneDrive\\Desktop\\Destination"
textdir = "C:\\Users\\RedDr\\OneDrive\\Desktop\\Text"
exedir = "C:\\Users\\RedDr\\OneDrive\\Desktop\\Launchers"
imagedir = "C:\\Users\\RedDr\\OneDrive\\Desktop"


file = os.listdir(path)
file2 = os.listdir(destinationdir)

for f in file:

    if not f.startswith ('DesktopCleaner'):

        if not f.startswith ('Destination') and not f.endswith ('.dir'):

            if not f.startswith ('Text') and not f.endswith ('.dir'):

                if not f.startswith ('Launchers') and not f.endswith ('.dir'):
                    src_path = os.path.join(path, f)
                    dst_path = os.path.join(destinationdir, f)
                    shutil.move(src_path, dst_path) 
                    break
for f in file2:
    print('1')
    if f.endswith ('.txt'):
        print('2')
        dst_path = os.path.join(destinationdir, f)
        txt_path = os.path.join(textdir, f)
        shutil.move(dst_path, txt_path)
        print('3') 
    elif f.endswith ('.lnk'): 
        print('4')  
        dst_path = os.path.join(destinationdir, f)
        exe_path = os.path.join(exedir, f)
        shutil.move(dst_path, exe_path) 
    elif f.endswith ('.png'):
        dst_path = os.path.join(destinationdir, f)
        img_path = os.path.join(imagedir, f)
        shutil.move(dst_path, img_path)
