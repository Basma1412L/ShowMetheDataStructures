## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    paths=[]
    if (os.path.isfile(path)):
        if (path.endswith(suffix)):
            paths.append(path)
            return paths
    else:
        paths=(append_path(suffix, path,paths))
    return paths

def append_path(suffix, path,paths):
    if (path==None):
        return None
    if (os.path.isfile(path)):
        if (path.endswith(suffix)):
            paths.append(path)
            return paths
    else:
        if ((os.path.isdir(path))):
            subs = (os.listdir(path))
            for x in subs:
                append_path(suffix, os.path.join(path,x), paths)
    return paths


# Let us print the files in the directory in which you are running this script
print (os.listdir("./testdir"))
# Let us check if this file is indeed a file!
print(find_files(".c","./testdir"))


assert (os.path.isfile("./ex.py")==False)
assert ("./ex.py".endswith(".py")==True)
