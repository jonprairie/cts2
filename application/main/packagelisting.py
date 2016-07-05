import os


def ListPackages(pth):
    current_path = os.getcwd()
    root = GetRoot(pth)
    try:
        path_to_root = FindNodeInPath(current_path, root)
        return filter(
            lambda x: x.find('__init__.py') is -1,
            os.listdir(
                os.path.join(path_to_root, pth)
            )
        )
    except:
        raise


def GetRoot(pth):
    base, node = os.path.split(pth)
    if base == "":
        return node
    else:
        return GetRoot(base)


def FindNodeInPath(pth, node):
    pth2, nde = os.path.split(pth)
    if node.upper() == nde.upper():
        return pth2
    elif pth2 in ["", pth]:
        raise Exception(
            'ListPackages: Folder ' + node +
            ' not found'
        )
    else:
        return FindNodeInPath(pth2, node)
