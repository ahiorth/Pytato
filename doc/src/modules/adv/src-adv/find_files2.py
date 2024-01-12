#%%
#content of find_files2.py
import pathlib as pt 
import sys
def find_files_of_type(dir='.',extensions=['.xlsx','.txt','.INC']):
    """
    return a list files of type defined in extensions
    """
    p=pt.Path(dir)
    files=[]
    for ext in extensions:
        for x in p.rglob("*"+ext):
            if x.is_file():
                files.append(x.absolute())
    return files
if __name__ == '__main__':
    dir='.'
    if len(sys.argv) > 1:
        dir=sys.argv[1]
    files=find_files_of_type(dir=dir)
    for f in files:
        print(f)
# %%
